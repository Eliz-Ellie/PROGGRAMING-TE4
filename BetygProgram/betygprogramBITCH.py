from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# GRADE SCALE
GRADE_SCALE = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "F": 0}

# Database MODELS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    subjects = db.relationship("SubjectGrade", backref="user", lazy=True)

class SubjectGrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    subject_name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    required_for_graduation = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text, nullable=True)

class GraduationRequirements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    min_merit = db.Column(db.Integer, default=2250)
    min_passed_subjects = db.Column(db.Integer, default=12)

with app.app_context():
    db.create_all()

# LOGIN MANAGER
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# FUNCTIONS
def calculate_average(user_id):
    subjects = SubjectGrade.query.filter_by(user_id=user_id).all()
    if not subjects:
        return 0
    total_points = sum(GRADE_SCALE.get(s.grade.upper(), 0) for s in subjects)
    return round(total_points / len(subjects), 2)

def calculate_merit(user_id):
    subjects = SubjectGrade.query.filter_by(user_id=user_id).all()
    if not subjects:
        return 0
    total = sum(GRADE_SCALE.get(s.grade.upper(), 0) * s.points for s in subjects)
    return total

def average_to_letter(avg):
    if avg >= 20: return "A"
    if avg >= 17.5: return "B"
    if avg >= 15: return "C"
    if avg >= 12.5: return "D"
    if avg >= 10: return "E"
    return "F"

def check_graduation(user_id):
    subjects = SubjectGrade.query.filter_by(user_id=user_id).all()
    if not subjects:
        return False

    # hämta användarens krav eller skapa default
    req = GraduationRequirements.query.filter_by(user_id=user_id).first()
    if not req:
        req = GraduationRequirements(user_id=user_id)
        db.session.add(req)
        db.session.commit()

    for s in subjects:
        if s.required_for_graduation and GRADE_SCALE.get(s.grade.upper(), 0) == 0:
            return False

    if calculate_merit(user_id) < req.min_merit:
        return False

    approved = sum(1 for s in subjects if GRADE_SCALE.get(s.grade.upper(), 0) > 0)
    if approved < req.min_passed_subjects:
        return False

    return True

# ROUTES
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        if User.query.filter_by(username=username).first():
            flash("Användaren finns redan!")
            return redirect(url_for("register"))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registrering lyckades! Logga in.")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("index"))
        flash("Fel användarnamn eller lösenord")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        ämne = request.form["ämne"].strip()
        betyg = request.form["betyg"].upper()
        points = int(request.form["points"])
        required_for_graduation = "required_for_graduation" in request.form
        notes = request.form.get("notes", "")

        if betyg not in GRADE_SCALE:
            return jsonify({"error": "Ogiltigt betyg"}), 400

        if SubjectGrade.query.filter_by(subject_name=ämne, user_id=current_user.id).first():
            return jsonify({"error": f"Ämnet '{ämne}' finns redan."}), 400

        new_entry = SubjectGrade(
            subject_name=ämne,
            grade=betyg,
            points=points,
            required_for_graduation=required_for_graduation,
            notes=notes,
            user_id=current_user.id
        )
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({
            "id": new_entry.id,
            "subject_name": new_entry.subject_name,
            "grade": new_entry.grade,
            "points": new_entry.points,
            "required_for_graduation": new_entry.required_for_graduation,
            "notes": new_entry.notes
        })

    all_subjects = SubjectGrade.query.filter_by(user_id=current_user.id).all()
    medel = calculate_average(current_user.id)
    return render_template(
        "index.html",
        all_subjects=all_subjects,
        medel=medel,
        medel_letter=average_to_letter(medel),
        merit=calculate_merit(current_user.id),
        examen=check_graduation(current_user.id),
        requirements=GraduationRequirements.query.filter_by(user_id=current_user.id).first()
    )

@app.route("/update/<int:subject_id>", methods=["POST"])
@login_required
def update_subject(subject_id):
    subject = SubjectGrade.query.filter_by(id=subject_id, user_id=current_user.id).first_or_404()

    ämne = request.form["ämne"].strip()
    betyg = request.form["betyg"].upper()
    points = int(request.form["points"])
    notes = request.form.get("notes", "")
    required_for_graduation = "required_for_graduation" in request.form

    if betyg not in GRADE_SCALE:
        return jsonify({"error": "Ogiltigt betyg"}), 400

    existing = SubjectGrade.query.filter_by(subject_name=ämne, user_id=current_user.id).first()
    if existing and existing.id != subject.id:
        return jsonify({"error": f"Ämnet '{ämne}' finns redan."}), 400

    subject.subject_name = ämne
    subject.grade = betyg
    subject.points = points
    subject.required_for_graduation = required_for_graduation
    subject.notes = notes

    db.session.commit()

    return jsonify({
        "id": subject.id,
        "subject_name": subject.subject_name,
        "grade": subject.grade,
        "points": subject.points,
        "required_for_graduation": subject.required_for_graduation,
        "notes": subject.notes
    })

@app.route("/delete/<int:subject_id>", methods=["POST"])
@login_required
def delete_subject(subject_id):
    subject = SubjectGrade.query.filter_by(id=subject_id, user_id=current_user.id).first_or_404()
    db.session.delete(subject)
    db.session.commit()
    return ("", 204)

@app.route("/stats")
@login_required
def stats():
    avg = calculate_average(current_user.id)
    return jsonify({
        "medel": avg,
        "medel_letter": average_to_letter(avg),
        "merit": calculate_merit(current_user.id),
        "examen": check_graduation(current_user.id)
    })

@app.route("/requirements", methods=["POST"])
@login_required
def update_requirements():
    req = GraduationRequirements.query.filter_by(user_id=current_user.id).first()
    if not req:
        req = GraduationRequirements(user_id=current_user.id)
        db.session.add(req)

    req.min_merit = int(request.form["min_merit"])
    req.min_passed_subjects = int(request.form["min_passed_subjects"])
    db.session.commit()

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
