from fastapi import FastAPI, HTTPException
from Fridge import Fridge 
from models import GroceryIn
from fastapi import status


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


@app.get("/fridges/{fridge_id}/groceries", status_code=status.HTTP_200_OK)
def list_groceries(fridge_id: str):
    fridge = get_fridge(fridge_id)
    return {"groceries": fridge.groceries}

@app.post("/fridges/{fridge_id}/groceries")
def add_grocery(fridge_id: str, item: GroceryIn, status_code: int = status.HTTP_201_CREATED):
    filename = FRIDGE_FILES[fridge_id]
    fridge = get_fridge(fridge_id)

    # normalizace jména (stejně jako v CLI → Title Case)
    name = item.name.strip().title()
    count = item.count

    # přidej do lednice
    fridge.add_item(name, count)

    # ulož zpět
    fridge.save_to_json(filename)

    return {"groceries": fridge.groceries}

@app.delete("/fridges/{fridge_id}/groceries/{item}", status_code=status.HTTP_204_NO_CONTENT)
def delete_grocery(fridge_id: str, item: str):
    filename = FRIDGE_FILES[fridge_id]
    fridge = get_fridge(fridge_id)
    
    name = item.name.strip().title()

    if name not in fridge.groceries:
        raise HTTPException(status_code=404, detail=f"Grocery '{name}' not found in fridge {fridge_id}")

    count = fridge.groceries[name]
    fridge.remove_item(name)

        
    fridge.save_to_json(filename)

    return {"detail": f"Grocery '{name}' removed from fridge {fridge_id}"}
