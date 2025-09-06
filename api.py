from fastapi import FastAPI, HTTPException
from Fridge import Fridge 
from models import GroceryIn
from fastapi import status
from FridgeManager import get_fridge, FRIDGE_FILES


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

@app.delete("/fridges/{fridge_id}/groceries/{item}", status_code=status.HTTP_200_OK)
def delete_grocery(fridge_id: str, grocery: GroceryIn):
    filename = FRIDGE_FILES[fridge_id]
    fridge = get_fridge(fridge_id)
    
    name = grocery.name.title()

    if name not in fridge.groceries:
        raise HTTPException(status_code=404, detail=f"Grocery '{name}' not found in fridge {fridge_id}")

    if fridge.groceries[name] < grocery.count:
        raise HTTPException(status_code=400, detail=f"Not enough '{name}' in fridge {fridge_id}")

    fridge.remove_item(name, grocery.count)
    
    fridge.save_to_json(filename)

    return {
        "detail": f"{grocery.count} units of '{name}' removed from fridge {fridge_id}. {fridge.groceries[name]} units remaining."
    }
