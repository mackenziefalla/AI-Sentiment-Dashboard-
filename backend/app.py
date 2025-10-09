from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from evaluate import analyze_prompt

app = FastAPI()

app.add_middleware(
    #allowing everything until app is hosted
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.post("/api/generate")
def generate(prompt: Prompt):
    result = analyze_prompt(prompt.prompt)
    return {"sentiment": result}