from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ✅ Tea model
class Tea(BaseModel):
    id: int
    name: str
    flavor: str

# ✅ In-memory list of teas
teas = [
    Tea(id=1, name="Green Tea", flavor="Mint"),
    Tea(id=2, name="Black Tea", flavor="Lemon"),
]

# ✅ PUT: Update a tea by ID
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

# ✅ DELETE: Delete a tea by ID
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"error": "Tea not found"}
