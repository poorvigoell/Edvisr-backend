import os
import google.generativeai as genai

# Load API key from environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment.")

genai.configure(api_key=api_key)

def generate_what_if_question(topic):
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"""Generate one creative "What If?" question based on the topic "{topic}".
    The question should challenge students to think about an alternate reality where something did not happen or happened differently.
    Just return a single engaging question. No explanation needed."""

    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=200
        )
    )

    return response.text if response else "No response from Gemini"
