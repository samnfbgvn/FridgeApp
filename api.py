from fastapi import FastAPI, HTTPException
from Fridge import Fridge 
from models import GroceryIn
from models import GroceryRename
from fastapi import status
from FridgeManager import get_fridge, FRIDGE_FILES
from pathlib import Path



app = FastAPI(title="Fridge API", version="0.1.0")


@app.get("/fridges/{fridge_id}/groceries", status_code=status.HTTP_200_OK)
def list_groceries(fridge_id: str):
    fridge = get_fridge(fridge_id)
    return {"groceries": fridge.groceries}

@app.post("/fridges/{fridge_id}/groceries", status_code=status.HTTP_201_CREATED)
def add_grocery(fridge_id: str, item: GroceryIn):
   
    filename = FRIDGE_FILES.get(fridge_id)
    if not filename:
        raise HTTPException(status_code=404, detail=f"Fridge {fridge_id} not found")

    # 2) ensure parent folder exists (optional; needed only if you use subfolders)
    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    # 3) load current state (if file doesn't exist, get_fridge returns empty fridge)
    fridge = get_fridge(fridge_id)

    # 4) normalize + add
    name = item.name.strip().title()
    count = item.count
    fridge.add_item(name, count)

    # 5) persist (this will CREATE the file if it doesn't exist)
    try:
        fridge.save_to_json(filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Saving failed: {e}")

    return {"groceries": fridge.groceries}
   
@app.delete("/fridges/{fridge_id}/groceries/{item}", status_code=status.HTTP_200_OK)
def delete_grocery(fridge_id: str, grocery: GroceryIn):
    filename = FRIDGE_FILES.get(fridge_id)
    if not filename:
        raise HTTPException(status_code=404, detail=f"Fridge {fridge_id} not found")

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


@app.put("/fridges/{fridge_id}/groceries/{old_name}", status_code=status.HTTP_200_OK)
def update_grocery(fridge_id: str, old_name: str, rename: GroceryRename):
    filename = FRIDGE_FILES.get(fridge_id)
    if not filename:
        raise HTTPException(status_code=404, detail=f"Fridge {fridge_id} not found")

    fridge = get_fridge(fridge_id)

    # Normalize names
    old_name = old_name.title()
    count = fridge.groceries[old_name]
    new_name = rename.new_name.strip().title()
    

    if old_name not in fridge.groceries:
        raise HTTPException(status_code=404, detail=f"Grocery '{old_name}' not found in fridge {fridge_id}")

    fridge.remove_item(old_name, fridge.groceries[old_name])


    fridge.rename_item(old_name, new_name)
    fridge.add_item(new_name, count)
    fridge.save_to_json(filename)
    return {
        "detail": f"Grocery '{old_name}' updated to '{new_name}' with {count} units in fridge {fridge_id}."
    }
