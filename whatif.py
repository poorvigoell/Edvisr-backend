import os
from google import genai

# Create Gemini client using API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_what_if_question(topic: str) -> str:
    """
    Generates one creative "What If?" question based on the given topic.
    """

    prompt = f"""
        You are an expert educator and question designer.

        Create ONE thought-provoking “What if?” question based on the topic: "{topic}".

        Rules:
        - The question must explore a realistic alternate scenario where a key event, concept, or assumption changes
        - It should encourage critical, causal, or imaginative thinking
        - It must be age-appropriate and suitable for students
        - Do NOT include explanations, answers, or extra text

        Output format:
        - A single sentence phrased as a question
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 1.0,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 200,
        },
    )

    return response.text
