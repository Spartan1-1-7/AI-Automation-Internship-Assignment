import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from the .env file
load_dotenv()

# YouTube API Key
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Set up the YouTube API client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_youtube(query):
    # Perform the search on YouTube
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=5,  # You can adjust the number of results
        videoDuration="medium",  # Filter for videos of 4-20 minutes
    )
    
    response = request.execute()

    # Extract video details
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    else:
        return None
