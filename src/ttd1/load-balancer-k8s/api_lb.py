from typing import Optional

from fastapi import FastAPI

import requests as rq

app = FastAPI()


@app.get("/")
def read_root():
    x = rq.get("http://10.106.2.177:5000")
    return {"FASTAPI_LB": f"{x.json()}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
