import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv("API_KEY")

from google import genai
from google.genai import types

import PIL.Image

image = PIL.Image.open('dog.jpeg')

client = genai.Client(api_key=API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is this image? Is this dog has rabies?"
    "give the probability of this dog having rabies", image])

print(response.text)

