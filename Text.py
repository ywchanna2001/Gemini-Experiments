import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv("API_KEY")

######################################

from google import genai

client = genai.Client(api_key= API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="what is Gemini 2.0 flash"
)
print(response.text)