from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from langchain_openai import ChatOpenAI
from config import ENV_VARIABLES



app = FastAPI()

class StringRequest(BaseModel):
    name: str
    question: str

@app.post("/greet")
async def greet(name_request: StringRequest):
    name = name_request.name
    return {"message": f"Hello {name}"}


@app.post("/chat")
async def chat(request: StringRequest):
    name = request.name
    question = request.question
    llm = ChatOpenAI(api_key= ENV_VARIABLES["IGERENICA_ALEGION_API"], model_name="gpt-3.5-turbo")
    response = llm.invoke(question)

    return {"response":f"Hi {name} this is your response: {response.content}"}



# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)