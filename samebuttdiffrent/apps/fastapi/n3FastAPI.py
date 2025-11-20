from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from datetime import date
import sqlite3
from pathlib import Path

app = FastAPI()
DB = Path(__file__).resolve().parent.parent / 'data' / 'fastapi.db'
UPSERT_SQL = """
INSERT INTO names(name, count) VALUES(?, 1)
ON CONFLICT(name) DO UPDATE SET count = count + 1
"""

def record_name(name: str) -> int:
    conn = sqlite3.connect(DB)
    try:
        conn.execute(UPSERT_SQL, (name,))
        conn.commit()
        cur = conn.execute("SELECT count FROM names WHERE name = ?", (name,))
        row = cur.fetchone()
        return row[0] if row else 0
    finally:
        conn.close()

@app.get("/", response_class=HTMLResponse)
async def form_page():
    return """
    <form action="/" method="post">
      <input type="text" name="name" placeholder="Ditt namn">
      <button>Skicka</button>
    </form>
    """

@app.post("/", response_class=HTMLResponse)
async def greet_user(name: str = Form(...)):
    today = date.today().strftime("%Y-%m-%d")
    count = record_name(name)
    return f"<p>Hej {name}! Idag är det {today}.</p><p>Antal gånger skickat: {count}</p>"
