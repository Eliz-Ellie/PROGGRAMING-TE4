# app.py
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Demo API")

# Pydantic model for request/response
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    tags: list[str] = []

# A simple dependency
def get_token(token: Optional[str] = None):
    if token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

@app.post("/items", response_model=Item)
def create_item(item: Item, _=Depends(get_token)):
    # Here you’d persist to DB; we just echo back the validated model
    return item