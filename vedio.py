import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv("API_KEY")

################################################

from google import genai

client = genai.Client(api_key=API_KEY)

print("Uploading file....")
video_file = client.files.upload(file="GreatRedSpot.mp4")
print(f"Completed upload: {video_file.uri}")


# import time

# # Check whether the file is ready to be used.
# while video_file.state.name == "PROCESSING":
#     print('.', end='')
#     time.sleep(1)
#     video_file = client.files.get(name=video_file.name)

# if video_file.state.name == "FAILED":
#   raise ValueError(video_file.state.name)

# print('Done')

