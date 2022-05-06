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
        '''Test to check if object is of type News_article'''
        self.assertTrue(isinstance(self.new_news_article,News_article))

    def test_init(self):
        '''
        test_init test case to test if the news_article object is initialized properly
        '''
        self.assertEqual(self.new_news_article.source, 'bbc')
        self.assertEqual(self.new_news_article.author, 'qw')
        self.assertEqual(self.new_news_article.title, 'sd')
        self.assertEqual(self.new_news_article.description, 'wdw')
        self.assertEqual(self.new_news_article.url, 'dq')
        self.assertEqual(self.new_news_article.content, 'ad')
        self.assertEqual(self.new_news_article.urlToImage, 'k')
        self.assertEqual(self.new_news_article.publishedAt, 'we')




if __name__ == '__main__':
    unittest.main()
