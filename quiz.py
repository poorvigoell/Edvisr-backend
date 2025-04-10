import os
import google.generativeai as genai

# Fetch API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set. Run the command to set it in Colab first.")

genai.configure(api_key=api_key)

def generate_questions(grade, topic, difficulty):
    """
    Generates MCQ and theory questions based on the specified topic, grade, and difficulty level.
    """
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"""
    Generate multiple-choice questions (MCQs) and theory questions for NCERT Class {grade} on the topic "{topic}".
    Ensure the questions match the {difficulty} difficulty level.
    Analyze past year questions (PYQs) to maintain relevance and standard difficulty.
    Provide the correct answers for MCQs.

    **Multiple Choice Questions (MCQs) - {difficulty.capitalize()} Level:**

    1. Question 1
       a) Option a
       b) Option b
       c) Option c
       d) Option d
       Answer: [Correct answer]

    2. Question 2
       ...

    **Theory Questions - {difficulty.capitalize()} Level:**

    1. Question 1
    2. Question 2
    ...
    """

    response = model.generate_content(prompt)
    return response.text if response else "No response from API."
