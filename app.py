import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()  # This loads the environment variables from .env

app = Flask(__name__)

API_KEY = os.environ.get('YOUTUBE_API_KEY')
if not API_KEY:
    raise ValueError("No API Key set for YouTube API")

youtube = build('youtube', 'v3', developerKey=API_KEY)

@app.route('/')
def index():
    return render_template('index.html', app_name="TuneQuest")

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    music_results = search_music(query)
    album_results = search_albums(query)
    return jsonify({
        'music': music_results,
        'albums': album_results
    })

def search_music(query, max_results=10):
    try:
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=max_results,
            videoCategoryId='10'  # Music category
        ).execute()

        videos = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append({
                    'title': search_result['snippet']['title'],
                    'video_id': search_result['id']['videoId'],
                    'thumbnail': search_result['snippet']['thumbnails']['high']['url']
                })
        
        return videos
    except HttpError as e:
        print(f'An error occurred: {e}')
        return []

def search_albums(query, max_results=10):
    try:
        search_response = youtube.search().list(
            q=query,
            type='playlist',
            part='id,snippet',
            maxResults=max_results
        ).execute()

        albums = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#playlist':
                albums.append({
                    'title': search_result['snippet']['title'],
                    'playlist_id': search_result['id']['playlistId'],
                    'thumbnail': search_result['snippet']['thumbnails']['high']['url']
                })
        
        return albums
    except HttpError as e:
        print(f'An error occurred: {e}')
        return []

if __name__ == '__main__':
    app.run(debug=True)