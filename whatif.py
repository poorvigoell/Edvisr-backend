import os
from google import genai

# Create Gemini client using API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_what_if_question(topic: str) -> str:
    """
    Generates one creative "What If?" question based on the given topic.
    """

    prompt = f"""
    Generate one creative "What If?" question based on the topic "{topic}".

    The question should:
    - Explore an alternate reality where something important changed
    - Encourage critical and imaginative thinking
    - Be suitable for students

    Return ONLY one engaging question.
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
