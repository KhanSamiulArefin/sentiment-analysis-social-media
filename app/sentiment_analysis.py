# app/sentiment_analysis.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Initialize VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    # Using VADER for sentiment analysis
    score = vader_analyzer.polarity_scores(text)
    return score['compound']  # Returns compound score (-1 to 1)

def get_sentiment_textblob(text):
    # Using TextBlob for sentiment analysis (optional alternative)
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns polarity score (-1 to 1)