import requests 
import os
from bs4 import BeautifulSoup
from newsapi import NewsApiClient

# Retrieve the API key from the environment variable
api_key = os.getenv('NEWS_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please set the NEWS_API_KEY environment variable.")

# Initialize the NewsAPI client
newsapi = NewsApiClient(api_key=api_key)

# Function to get national news
def get_national_news(country):
    try:
        # Fetch top headlines in the specified country
        top_headlines = newsapi.get_top_headlines(country=country.lower())
        if top_headlines['articles']:
            return [article['title'] for article in top_headlines['articles']]
        else:
            return ["No national news found for this country."]
    except Exception as e:
        return [f"Error fetching national news: {str(e)}"]

# Function to get global news
def get_global_news():
    try:
        # Fetch all articles globally
        all_articles = newsapi.get_everything(q='news')
        if all_articles['articles']:
            return [article['title'] for article in all_articles['articles'][:5]]  # Limit to 5 articles
        else:
            return ["No global news found."]
    except Exception as e:
        return [f"Error fetching global news: {str(e)}"]

# Main program
print("Welcome to the General News Program")
country = input("Please enter your country (e.g., 'us' for USA): ")

national_news = get_national_news(country)
print("\nNational News:")
for news in national_news:
    print(f"- {news}")

global_news = get_global_news()
print("\nGlobal News:")
for news in global_news:
    print(f"- {news}")