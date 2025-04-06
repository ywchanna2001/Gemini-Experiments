import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv("API_KEY")

################################################

from google import genai

client = genai.Client(api_key=API_KEY)

from IPython.display import Markdown

# Pass the video file reference like any other media part.
video_file = 'video2.py'
response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=[
        video_file,
        "Summarize this video. Then create a quiz with answer key "
        "based on the information in the video."])

# Print the response, rendering any Markdown
Markdown(response.text)