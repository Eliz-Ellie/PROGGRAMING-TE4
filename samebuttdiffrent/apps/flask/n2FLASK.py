from flask import Flask, request, render_template_string
from datetime import date
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path(__file__).resolve().parent.parent / 'data' / 'flask.db'
UPSERT_SQL = """
INSERT INTO names(name, count) VALUES(?, 1)
ON CONFLICT(name) DO UPDATE SET count = count + 1
"""

def record_name(name: str):
    conn = sqlite3.connect(DB)
    try:
        conn.execute(UPSERT_SQL, (name,))
        conn.commit()
        cur = conn.execute("SELECT count FROM names WHERE name = ?", (name,))
        row = cur.fetchone()
        return row[0] if row else 0
    finally:
        conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    name = request.form.get("name", "")
    today = date.today().strftime("%Y-%m-%d")
    count = None
    if name:
        count = record_name(name)
    html = """
    <form method="POST">
      <input type="text" name="name" placeholder="Ditt namn">
      <button>Skicka</button>
    </form>
    {% if name %}
      <p>Hej {{ name }}! Idag är det {{ today }}.</p>
      <p>Antal gånger skickat: {{ count }}</p>
    {% endif %}
    """
    return render_template_string(html, name=name, today=today, count=count)

if __name__ == "__main__":
    app.run(debug=True)
