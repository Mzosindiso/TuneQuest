# TuneQuest

TuneQuest is a web application that allows users to search for and explore music and albums using the YouTube Data API. It provides a simple and intuitive interface for discovering and playing music videos and playlists.
![image](https://github.com/user-attachments/assets/e67ff485-a0c5-4e03-a3d5-018a17b7e061)



## Features

- Search for music videos and albums
- Display search results in a user-friendly list
- Play selected music videos directly in the application
- Switch between music and album search results
- View video/playlist details including thumbnail and title

## How It Works

1. Users enter a search query in the search bar.
2. The application sends a request to the YouTube Data API to fetch relevant music videos and playlists.
3. Search results are displayed in two categories: Music and Albums.
4. Users can click on a search result to view more details and play the video (for music results).
5. The selected video is played using the YouTube Player API embedded in the application.

## Technologies Used

- Backend: Python with Flask framework
- Frontend: HTML, CSS, and JavaScript
- YouTube Data API v3 for searching videos and playlists
- YouTube Player API for embedding and playing videos

## Setup and Installation

1. Clone the repository
2. Install the required Python packages: `pip install flask google-api-python-client`
3. Set up a YouTube Data API key:
   - Create a project in the [Google Developers Console](https://console.developers.google.com/)
   - Enable the YouTube Data API v3
   - Create credentials (API Key)
   - Create a `.env` file in the project root and add your API key:
     ```
     YOUTUBE_API_KEY=your_api_key_here
     ```
   - Make sure to add `.env` to your `.gitignore` file to prevent accidentally committing it
4. Run the application: `python app.py`
5. Open a web browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py`: Main Flask application file
- `templates/index.html`: HTML template for the web interface
- `static/styles.css`: CSS styles for the application

## Note

This project is for educational purposes and uses the YouTube API. Make sure to comply with YouTube's terms of service and API usage guidelines when using this application.
