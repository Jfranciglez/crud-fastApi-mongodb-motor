from datetime import datetime, date
from fastapi import FastAPI, HTTPException
import os
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List

# --- Modelo Pydantic ---
class Producto(BaseModel):
    codigo: int
    nombre: str
    categoria: str
    stock: int
    fecha_cad: date  # formato: YYYY-MM-DD

# --- Configuración FastAPI ---
app = FastAPI(
    title="API de Almacén",              
    description="Gestión de productos, stock y categorías del almacén.",
    version="1.0.0"                      # versión de la API
)


# --- Conexión a MongoDB ---
MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:admin@mongo:27017/")
client = AsyncIOMotorClient(MONGO_URL)
db = client["almacen"]

# --- Endpoint raíz ---
@app.get("/")
async def root():
    return {"ok": True, "colecciones": await db.list_collection_names()}


# --- Crear producto con validación de duplicado ---
@app.post("/producto", response_description="Agrega un nuevo producto", response_model=Producto)
async def create_producto(producto: Producto):
    existente = await db["producto"].find_one({"codigo": producto.codigo})
    if existente:
        raise HTTPException(status_code=400, detail=f"El producto con código {producto.codigo} ya existe.")

    try:
        producto_dict = producto.dict()

        if isinstance(producto_dict["fecha_cad"], date):
            producto_dict["fecha_cad"] = datetime.combine(producto_dict["fecha_cad"], datetime.min.time())

        await db["producto"].insert_one(producto_dict)
        return producto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al insertar producto: {str(e)}")



# --- Listar productos ---
@app.get("/producto", response_description="Lista de productos", response_model=List[Producto])
async def list_producto():
    productos = await db["producto"].find().to_list(100)
    for p in productos:
        p["_id"] = str(p["_id"])  # evitar error de ObjectId
    return productos


# --- Obtener producto por código ---
@app.get("/producto/{codigo}", response_description="Obtener un producto específico", response_model=Producto)
async def find_by_codigo_producto(codigo: int):
    producto = await db["producto"].find_one({"codigo": codigo})
    if not producto:
        producto = await db["producto"].find_one({"codigo": str(codigo)})  # fallback si se guardó como texto

    if producto:
        producto["_id"] = str(producto["_id"])
        return producto
    else:
        raise HTTPException(status_code=404, detail=f"Producto con código {codigo} no encontrado.")


# --- Borrar producto por código ---
@app.delete("/producto/{codigo}", response_description="Borra un producto con el código")
async def delete_codigo(codigo: int):
    delete_result = await db["producto"].delete_one({"codigo": codigo})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"Producto con código {codigo} no encontrado.")
    return {"message": f"Producto con código {codigo} borrado con éxito."}
