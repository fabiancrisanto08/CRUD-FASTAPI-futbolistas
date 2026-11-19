import json
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
app = FastAPI()

ARCHIVO = "futbolistas.json"

class Futbolista(BaseModel):
    nombre: str
    equipo: str
    posicion: str

def leer():
    with open(ARCHIVO, encoding="utf-8") as f:
        return json.load(f)


def guardar(futbolistas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(futbolistas, f, indent=2, ensure_ascii=False)


@app.get("/")
def inicio():
    return {"mensaje": "Hola, FastAPI"}


@app.get("/futbolistas")
def listar():
    return leer()


@app.get("/futbolistas/{id}")
def buscar_futbolista(id: int):
    futbolistas = leer()
    for futbolista in futbolistas:
        if futbolista.get("id") == id:
            return futbolista
    raise HTTPException(status_code=404, detail="Futbolista no encontrado")

@app.post("/futbolistas")
def agregar(futbolista: Futbolista):
    futbolistas = leer()
    id_mas_alto = 0
    for f in futbolistas:
        if f["id"] > id_mas_alto:
            id_mas_alto = f["id"]
    nuevo = {
        "id": id_mas_alto + 1,
        "nombre": futbolista.nombre,
        "equipo": futbolista.equipo,
        "posicion": futbolista.posicion,
    }
    futbolistas.append(nuevo)
    guardar(futbolistas)
    return nuevo

@app.put("/futbolistas/{id}")
def editar(id: int, datos: Futbolista):
    futbolistas = leer()
    for futbolista in futbolistas:
        if futbolista["id"] == id:
            futbolista["nombre"] = datos.nombre
            futbolista["equipo"] = datos.equipo
            futbolista["posicion"] = datos.posicion
            guardar(futbolistas)
            return futbolista
    raise HTTPException(status_code=404, detail="Ese futbolista no existe")

@app.delete("/futbolistas/{id}")
def borrar(id: int):
    futbolistas = leer()
    for futbolista in futbolistas:
        if futbolista["id"] == id:
            futbolistas.remove(futbolista)
            guardar(futbolistas)
            return {"mensaje": "Futbolista borrado"}
    raise HTTPException(status_code=404, detail="Ese futbolista no existe")