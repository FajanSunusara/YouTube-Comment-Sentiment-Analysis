from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import googleapiclient.discovery
from transformers import pipeline
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Load the zero-shot classifier pipeline
classifier = pipeline("zero-shot-classification")

# Load environment variables from .env file
load_dotenv()

async def fetch_comment_threads(video_link, api_key):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    video_id = video_link.split("v=")[1]
    request = youtube.commentThreads().list(part="snippet", maxResults=100, videoId=video_id)
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        response = await loop.run_in_executor(executor, request.execute)
    return response

def process_sentiment(comment):
    text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
    result = classifier(text, candidate_labels=["positive", "negative"], multi_label=False)
    label = result['labels'][0]
    score = result['scores'][0]
    sentiment = label.capitalize() if label in ["positive", "negative"] else 'Neutral'
    return {'comment': text, 'score': score, 'sentiment': sentiment}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_link = request.form['video_link']
    api_key = os.getenv("API_KEY")
    try:
        comment_threads_response = asyncio.run(fetch_comment_threads(video_link, api_key))
        sentiment_results = [process_sentiment(comment) for comment in comment_threads_response.get('items', [])]
        positive_count = sum(1 for result in sentiment_results if result['sentiment'] == 'Positive')
        negative_count = sum(1 for result in sentiment_results if result['sentiment'] == 'Negative')
    except Exception as e:
        # Handle API request or sentiment analysis errors
        return render_template('error.html', error=str(e))
    return render_template('results.html', results=sentiment_results, positive_count=positive_count, negative_count=negative_count)

if __name__ == "__main__":
    app.run(debug=True)
