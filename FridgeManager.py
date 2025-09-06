from fastapi import  HTTPException
from Fridge import Fridge

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
