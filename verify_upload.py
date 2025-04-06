import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
GOOGLE_API_KEY = os.getenv("API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=GOOGLE_API_KEY)

#######################################################

import time

def upload_video(video_file_name):
  video_file = client.files.upload(file=video_file_name)  #sends local video file to Google

  while video_file.state == "PROCESSING":
      print('Waiting for video to be processed.')
      time.sleep(10)
      video_file = client.files.get(name=video_file.name)

  if video_file.state == "FAILED":
    raise ValueError(video_file.state)
  print(f'Video processing complete: ' + video_file.uri)

  return video_file

pottery_video = upload_video('GreatRedSpot.mp4')
