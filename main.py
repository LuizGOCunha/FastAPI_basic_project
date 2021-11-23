from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    altura: float
    idade: int
    genero: Optional[str] = None

class UpdateItem(BaseModel):
    nome: Optional[str]
    altura: Optional[float]
    idade: Optional[int]
    genero: Optional[str]


app = FastAPI()

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="ID not found")
    return inventory[item_id]


@app.get("/get-name")
def get_item(nome: Optional[str]):
    for item_id in inventory:
        if inventory[item_id].nome == nome:
            return inventory[item_id]
    raise HTTPException(status_code= 404, detail="item name not found")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code= 400, detail="ID already exists")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code= 404, detail="ID not found")
    if item.nome is not None:
        inventory[item_id].nome = item.nome
    if item.idade is not None:
        inventory[item_id].idade = item.idade
    if item.altura is not None:
        inventory[item_id].altura = item.altura
    if item.genero is not None:
        inventory[item_id].genero = item.genero

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code= 404, detail="ID not found")
    del inventory[item_id]
    return{"Success": "Item terminated"}













