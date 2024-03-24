from fastapi import FastAPI

import httpx

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Status": "OK"}

@app.get("/cep/{cep}")
async def fetch_cep(cep: str):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        if response.status_code == 200:
            return response.json()
        
        response = await client.get('https://opencep.com/v1/{}'.format(cep))
        if response.status_code == 200:
            return response.json()
        
        return {"error": "CEP not found"}
