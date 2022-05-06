import unittest
from models import news_article
News_article = news_article.News_article

class News_articleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_article = News_article('bbc','qw','sd','wdw','dq','ad', 'k', 'we')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article,News_article))


if __name__ == '__main__':
    unittest.main()
