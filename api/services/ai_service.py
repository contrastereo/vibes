import os
import openai

from api.exceptions.api_exceptions import MissingParameterError

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_haiku():
    """
    Generate a haiku using OpenAI GPT.
    """
    if not openai.api_key:
        raise MissingParameterError("OPENAI_API_KEY environment variable not set")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative poet specializing in haiku."},
            {"role": "user", "content": "Please write a haiku."}
        ],
        temperature=0.7,
        max_tokens=60,
        n=1,
    )
    haiku = response.choices[0].message.content.strip()
    return haiku 