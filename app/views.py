from turtle import tiltangle, title
from flask import render_template,request,redirect,url_for
from datetime import datetime
from app import app
from .request import get_news, get_articles, get_headlines, search_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    # Getting popular movie
    news = get_news()
    print(news)
    title = 'Home - Welcome to The best Movie Review Website Online'
    message = 'Hello World'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title,message=message, news= news)


    

    

@app.route('/articles/<source>')
def articles(source):

    '''
    View movie page function that returns the movie details page and its data
    '''
    articles = get_articles(source)

    return render_template('articles.html', articles = articles)

#@app.route('/article/<title>')
#def article(title):

    
    #View movie page function that returns the movie details page and its data
    
    #article = get_article(title)
    #title = f'{article.title}'

    #return render_template('article.html',article = article)
@app.route('/headlines')
def headlines():
    headlines = get_headlines()
    title = 'headlines'

    return render_template('headlines.html', headlines = headlines, title = title)

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',newws = searched_news, title = title)
