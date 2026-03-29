# app/social_media.py
import tweepy
import praw
from app.config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

# Set up Twitter API (Tweepy)
def fetch_twitter_data(keyword, count=100):
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    # Get tweets related to the keyword
    tweets = api.search(q=keyword, count=count, lang="en")
    return [tweet.text for tweet in tweets]

# Set up Reddit API (PRAW)
def fetch_reddit_data(keyword, limit=100):
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)
    
    # Search posts from Reddit
    posts = reddit.subreddit('all').search(keyword, limit=limit)
    return [post.title + " " + post.selftext for post in posts]