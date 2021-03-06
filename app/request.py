from curses.panel import top_panel
from typing import NewType
#from app import app
import urllib.request,json
from .models import News,News_article
from datetime import datetime
from datetime import timezone
#from app.models.news_article import News_article
#from .models import news

#News = news.News

# Getting api key
#api_key = app.config['NEWS_API_KEY']
api_key = '367d2b9d52254328a2263a46260220e4'


# Getting the news  urls
#base_url = app.config['NEWS_API_BASE_URL']
#top_url = app.config['TOP_URL']
#headline_url = app.config['HEADLINES_URL']
#search_base_url = app.config['SEARCH_NEWS_URL']
base_url = None
top_url = None
headline_url = None
search_base_url = None

def configure_request(app):
    global api_key,base_url,top_url,headline_url,search_base_url
    #api_key = app.config['NEWS_API_KEY']
    api_key= '367d2b9d52254328a2263a46260220e4'
    base_url = app.config['NEWS_API_BASE_URL']
    top_url = app.config['TOP_URL']
    headline_url = app.config['HEADLINES_URL']
    search_base_url = app.config['SEARCH_NEWS_URL']



def get_news():
    """
    Function to get news to display on homepage
    """
    news_url = base_url.format(api_key)
    #news_url = base_url

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
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        
        
        
        if description:
            new_news = News(id, name,description, url, category, country)
            news_results.append(new_news)

    return news_results
#TOP_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=367d2b9d52254328a2263a46260220e4'
#HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=367d2b9d52254328a2263a46260220e4'

def get_articles(source_id):
    """
    Function to get news to display on homepage
    """
    #news_url = base_url.format(api_key)
    arts_url = top_url.format(source_id,api_key)

    with urllib.request.urlopen(arts_url) as url:
        get_arts_data = url.read()
        get_news_response = json.loads(get_arts_data)
        arts_results = None
        
        arts_results_list = get_news_response['articles']
        arts_results = process_arts(arts_results_list)

    return arts_results


'''def get_articles(source_id):
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

    return news_article_object'''

def process_arts(arts_list):
    """
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        arts_list: A list of dictionaries that contain articles details

    Returns :
        arts_results: A list of article objects

    """
    arts_results = []
    for article in arts_list:
        source = article.get('source')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        the_url = article.get('url')
        content = article.get('content')
        urlToImage = article.get('urlToImage')
        publishedA = article.get('publishedAt')
        d = datetime.fromisoformat(publishedA[:-1]).astimezone(timezone.utc)
        
        #pub = publishedA.strptime()
        publishedAt = d.strftime("%B %d, %Y")
        time = d.strftime("%H:%M:%S")



        #publishedAt = pub.strftime("%B %d, %Y")
        
        if urlToImage:
            new_article = News_article(source, author, title, description, the_url, content,urlToImage,publishedAt,time )
            arts_results.append(new_article)

    return arts_results


def get_headlines():
    """
    Function to get news to display on homepage
    """
    #news_url = base_url.format(api_key)
    headlines_url = headline_url.format(api_key)

    with urllib.request.urlopen(headlines_url) as url:
        get_headlines_data = url.read()
        get_news_response = json.loads(get_headlines_data)
        headlines_results = None
        
        headlines_results_list = get_news_response['articles']
        headlines_results = process_arts(headlines_results_list)

    return headlines_results

def search_news(country):
    search_news_url = search_base_url.format(country,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_arts(search_news_list)


    return search_news_results
