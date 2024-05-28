from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.post("/greet")
async def greet(name_request: NameRequest):
    name = name_request.name
    return {"message": f"Hello {name}"}
