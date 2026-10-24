import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.8-flash"


def ask_ai(prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    if not response.text:
        raise ValueError("The AI returned an empty response.")

    return response.text


def ask_ai_safe(prompt, retries=3):
    for attempt in range(retries):
        try:
            return ask_ai(prompt)

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < retries - 1:
                time.sleep(2 ** attempt)

    return "Sorry, the AI service is not available right now."


if __name__ == "__main__":
    answer = ask_ai_safe(
        "Explain what an API is in two simple sentences."
    )

    print(answer)