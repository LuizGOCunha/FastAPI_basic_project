from fastapi import FastAPI, Path
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
    return inventory[item_id]

@app.get("/get-name")
def get_item(nome: Optional[str]):
    for item_id in inventory:
        if inventory[item_id].nome == nome:
            return inventory[item_id]
    return {"Data" : "Not Found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exist"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item Id does not exist"}
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
        return {"Error": "ID does not exist"}
    del inventory[item_id]
    return{"Success": "Item terminated"}













