
# YouTube Comment Sentiment Analysis

## Overview
This project is a web application built with Flask that performs sentiment analysis on YouTube video comments. It uses Google's YouTube Data API to fetch comment threads for a given video and Hugging Face's Transformers library to analyze the sentiment of each comment. The sentiment analysis results are then displayed on a web page along with the total count of positive and negative comments.

## Features
- Fetches comment threads from YouTube video using the YouTube Data API.
- Performs sentiment analysis on each comment using a pre-trained model from Hugging Face's Transformers library.
- Displays sentiment analysis results on a web page, highlighting positive and negative comments in different colors.
- Provides total counts of positive and negative comments.
- Simple and intuitive web interface for easy interaction.

## Results
Here are some sample screenshots showcasing the sentiment analysis results:

![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png)

You can view more screenshots in the [screenshots](screenshots/) directory.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/youtube-comment-sentiment-analysis.git
   ```
2. Navigate to the project directory:
   ```
   cd youtube-comment-sentiment-analysis
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Set up environment variables:
   Create a `.env` file in the root directory and add your YouTube Data API key:
   ```
   API_KEY=your_api_key_here
   ```
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open your web browser and go to `http://localhost:5000` to access the application.
5. Enter the YouTube video URL in the provided input field and submit the form.
6. The sentiment analysis results will be displayed along with the total counts of positive and negative comments.

## Technologies Used
- Python
- Flask
- Google API Client Library
- Hugging Face Transformers

## Credits
- [Flask](https://flask.palletsprojects.com/)
- [Google API Client Library](https://github.com/googleapis/google-api-python-client)
- [Hugging Face Transformers](https://huggingface.co/transformers/)

## License
This project is licensed under the [MIT License](LICENSE).


