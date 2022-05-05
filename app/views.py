from flask import render_template
from app import app
from .request import get_news, get_articles

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
    return render_template('index.html', title = title,message=message, news= news)

    

@app.route('/news/<source>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    articles = get_articles(id)

    return render_template('movie.html', articles = articles)

