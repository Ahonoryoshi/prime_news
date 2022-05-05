from typing import NewType
from app import app
import urllib.request,json

from app.models.news_article import News_article
from .models import news
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
#base_url = app.config['NEWS_API_BASE_URL']
base_url=  "https://newsapi.org/v2/sources?apiKey=367d2b9d52254328a2263a46260220e4"

def get_news():
    """
    Function to get news to display on homepage
    """
    #news_url = base_url.format(api_key)
    news_url = base_url

    with urllib.request.urlopen(news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['sources']: #making sure to return non-empty results
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results
    
def process_results(news_list):
    """
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of movie objects

    """
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        url = news_item.get('url')
        country = news_item.get('country')
        description = news_item.get('description')
        published = news_item.get('publishedAt')
        
        if description:
            new_news = News(id, name, url, country, description, published)
            news_results.append(new_news)

    return news_results
TOP_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=367d2b9d52254328a2263a46260220e4'
def get_articles(source_id):
    get_articles_url = TOP_URL.format(source_id)
    with urllib.request.urlopen(get_articles_url) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)

        news_article_object = None
        if news_articles_response:
            source = news_articles_response.get('source')
            author = news_articles_response.get('author')
            title = news_articles_response.get('title')
            description = news_articles_response.get('description')
            the_url = news_articles_response.get('url')
            content = news_articles_response.get('content')

            news_article_object = News_article(source, author,title, id,description,the_url,content)

    return news_article_object


