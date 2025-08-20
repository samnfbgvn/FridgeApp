from fastapi import FastAPI, HTTPException
from Fridge import Fridge 
import json

FRIDGE_FILES = {
    "1": "first_fridge.json",
    "2": "second_fridge.json"
}


def get_fridge(fridge_id: str) -> Fridge:
    if fridge_id not in FRIDGE_FILES:
        raise HTTPException(status_code=404, detail=f"Fridge {fridge_id} not found")

    filename = FRIDGE_FILES[fridge_id]
    fridge = Fridge(groceries={})
    try:
        fridge.load_from_json(filename)
    except FileNotFoundError:
        fridge.groceries = {}
    return fridge



app = FastAPI(title="Fridge API", version="0.1.0")


@app.get("/fridges/{fridge_id}/groceries")
def list_groceries(fridge_id: str):
    fridge = get_fridge(fridge_id)
    return {"groceries": fridge.groceries}
