import os
class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL =  "https://newsapi.org/v2/sources?apiKey={}"
    TOP_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SEARCH_NEWS_URL =  'https://newsapi.org/v2/everything?q={}&apiKey={}'
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


