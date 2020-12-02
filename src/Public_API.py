"""
This holds the Restful API endpoints and API documentation. It also starts the API Server.
"""
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
import uvicorn

import json
from pprint import pprint



app = FastAPI(
    title="UVAPI - Unreal Vault API",
    description="Unofficial, personalized Epic Games Vault REST API.",
    version="v1",

)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

j = json.load(open('data/dump.json'))

@app.get('/api/v1/vault')
def get(page: Optional[int] = None):
    """Get all vault items. Pagination is (somewhat) supported.

    Args:
        page (int, optional): page index. Starts with 0. Defaults to None.

    Returns:
        Personal Vault items.
    """
    if page:
        return j[page]
    else:
        return j

# TODO
@app.get('/api/v1/vault/sortbyrating')
def get():
    results = []
    """
    i page  (if pages[0] -> list of vault items and k will be vault item)
    j pages (0 -> page)
    k list of vault items
    l vault item
    """
    page_one = j[0]
    for i in page_one: # for testing: get only first page
        for k in i: # select list of 
                newlist = sorted(i, key=lambda k: k['amount_of_ratings']) 
    return 

# TODO
@app.get('/api/v1/vault/filter')
def get(publisher: Optional[str] = None):
    results = []
    if publisher:
            for i in j[0]:
                for k in j:
                    for l in k:
                        if (l['publisher'] == publisher+"\u00a0"):
                            results.append(l)
    return results

@app.get('/api/v1/vault/first')
def get():
    return j[0]

@app.get('/api/v1/vault/last')
def get():
    return j[-1]


uvicorn.run(app, host='localhost', port=8000)

# Churn Section **************************************************************************************************
# for i in j: # i is a page of items. The first items are the items that the user has added most early.
#     pprint(i)
# Churn Section **************************************************************************************************