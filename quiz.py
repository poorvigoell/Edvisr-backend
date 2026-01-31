import os
from google import genai

# Create client using API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_questions(grade, topic, difficulty):
    """
    Generates MCQ and theory questions based on the specified topic,
    grade, and difficulty level.
    """

    prompt = f"""
    Generate multiple-choice questions (MCQs) and theory questions for NCERT Class {grade}
    on the topic "{topic}".

    Difficulty level: {difficulty}

    Instructions:
    - Generate 5 MCQs with 4 options each
    - Clearly mention the correct answer
    - Then generate 3 theory questions
    - Keep NCERT / PYQ relevance

    Format the response clearly.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
