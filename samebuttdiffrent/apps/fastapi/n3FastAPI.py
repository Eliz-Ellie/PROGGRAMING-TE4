from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from datetime import date

app = FastAPI()

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
    return f"<p>Hej {name}! Idag är det {today}.</p>"

# Körs via: uvicorn app:app --reload
