import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John")
        self.assertEqual(author.name, "John")

    def test_article_creation(self):
        article = Article(1, "Style Evolution", "How fashion guru influence trend", 1, 1)
        self.assertEqual(article.title, "Style Evolution")
        self.assertEqual(article.content,"How fashion guru influence trend")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Taifa Leo", "Fashion")
        self.assertEqual(magazine.title, "Taifa Leo")
        self.assertEqual(magazine.publisher, "Fashion")
       

if __name__ == "__main__":
    unittest.main()
