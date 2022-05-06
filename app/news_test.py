import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('a','b','c','d','e','f')

    def test_instance(self):
        '''test to check if the object is of type News'''
        self.assertTrue(isinstance(self.new_news,News))

    def test_init(self):
        '''
        test_init test case to test if the news_article object is initialized properly
        '''
        self.assertEqual(self.new_news.id, 'a')
        self.assertEqual(self.new_news.name, 'b')
        self.assertEqual(self.new_news.description, 'c')
        self.assertEqual(self.new_news.url, 'd')
        self.assertEqual(self.new_news.category, 'e')
        self.assertEqual(self.new_news.country, 'f')
        


if __name__ == '__main__':
    unittest.main()
