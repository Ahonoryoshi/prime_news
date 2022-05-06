class News:
    """
    Class for creating instances of news objects
    """
    
    def __init__(self, id, name,description, url, category, country):
        """
        This method allows us to instantiate an instance.
        """
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class News_article:
    '''
    Class to generate instances of news_articles
    '''
    def __init__(self,source,author, title, description, url,content, urlToImage, publishedAt, time):
        """
        Initializing the class object
        """
        self.source= source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.content = content
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.time = time