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

