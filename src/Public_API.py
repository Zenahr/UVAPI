"""
This holds the Restful API endpoints and API documentation. It also starts the API Server.
"""
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional

from fastapi import FastAPI
import uvicorn

import json
from pprint import pprint

app = FastAPI(
    title="UVAPI - Unreal Vault API",
    description="Unofficial, personalized Epic Games Vault REST API.",
    version="v1",

)
j = json.load(open('data/dump.json'))

@app.get('/api/v1/vault')
def get(page: Optional[int] = None):
    if page:
        return j[page]
    else:
        return j

@app.get('/api/v1/vault/first')
def get():
    return j[0]
    
@app.get('/api/v1/vault/last')
def get():
    return j[-1]


# uvicorn.run(app, host='localhost', port=8000)

# Churn Section **************************************************************************************************
for i in j: # i is a page of items. The first items are the items that the user has added most early.
    pprint(i)

# Churn Section **************************************************************************************************