from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from evaluate import analyze_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows frontend to talk to backend
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
