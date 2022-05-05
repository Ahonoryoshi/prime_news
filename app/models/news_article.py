class News_article:
    '''
    Class to generate instances of news_articles
    '''
    def __init__(self,source,author, title, description, url,content, urlToImage, publishedAt):
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