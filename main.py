from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import traceback
from fastapi.middleware.cors import CORSMiddleware

# Load env vars
load_dotenv()

# Import original logic without modifying it
from quiz import generate_questions
from whatif import generate_what_if_question

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://edvisr.netlify.app/"],  # 👈 Allow all origins (frontend domains)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input models
class QuizInput(BaseModel):
    grade: str
    topic: str
    difficulty: str

class WhatIfInput(BaseModel):
    topic: str

@app.post("/generate-quiz")
def quiz_api(data: QuizInput):
    questions = generate_questions(data.grade, data.topic, data.difficulty)
    return {"questions": questions}

@app.post("/generate-whatif")
def whatif_api(data: WhatIfInput):
    try:
        result = generate_what_if_question(data.topic)
        return {"what_if_question": result.strip()}
    except Exception as e:
        print("\n--- ERROR IN GENERATE-WHATIF ---")
        print(traceback.format_exc())  # Show full error in terminal
        return {"error": "Something went wrong on the server."}