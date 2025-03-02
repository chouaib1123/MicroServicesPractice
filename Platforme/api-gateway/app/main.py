from fastapi import FastAPI, HTTPException, Request
import httpx
import os 

app = FastAPI()

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL")


@app.get("/products" )
async def get_all_products():
    async with httpx.AsyncClient() as client :
        response = await client.get(f"{PRODUCT_SERVICE_URL}/products")
        return response.json()

@app.get("/products/{id}")
async def get_product(id:str):
    async with httpx.AsyncClient() as client :
        response = await client.get(f"{PRODUCT_SERVICE_URL}/products/{id}")
        return response.json()

@app.post("/products")
async def add_product(request : Request):
    body = await request.json()
    async with httpx.AsyncClient() as client :
        response = await client.post(f"{PRODUCT_SERVICE_URL}/products" , json=body)
        return response.json()

@app.patch("/products/{id}")
async def update_product(id:str , request : Request):
    body = await request.json()
    async with httpx.AsyncClient() as client :
        response = await client.patch(f"{PRODUCT_SERVICE_URL}/products/{id}" , json=body)
        return response.json()

@app.delete("/products/{id}")
async def delete_product(id:str):
     async with httpx.AsyncClient() as client :
        response = await client.delete(f"{PRODUCT_SERVICE_URL}/products/{id}" )
        return response.json()
