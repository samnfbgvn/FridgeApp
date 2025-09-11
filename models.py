from pydantic import BaseModel, conint, constr

# název: jen písmena + mezery, nesmí být prázdný
Name = constr(strip_whitespace=True, min_length=1, pattern=r"^[A-Za-z\s]+$")

class GroceryRename(BaseModel):
    new_name: constr(strip_whitespace=True, min_length=1, pattern=r"^[A-Za-z\s]+$")

class GroceryIn(BaseModel):
    name: Name
    count: conint(gt=0)  # > 0
