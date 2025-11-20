from flask import Flask, request, render_template_string
from datetime import date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    name = request.form.get("name", "")
    today = date.today().strftime("%Y-%m-%d")
    html = """
    <form method="POST">
      <input type="text" name="name" placeholder="Ditt namn">
      <button>Skicka</button>
    </form>
    {% if name %}
      <p>Hej {{ name }}! Idag är det {{ today }}.</p>
    {% endif %}
    """
    return render_template_string(html, name=name, today=today)

if __name__ == "__main__":
    app.run(debug=True)
