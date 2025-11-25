from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EcoModel(BaseModel):
    message: str
    value: int | None = None

@app.get("/status")
def get_status():
    return {"status": "ok"}

@app.post("/eco")
def post_eco(data: EcoModel):
    return data
