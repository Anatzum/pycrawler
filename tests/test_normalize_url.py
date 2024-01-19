import unittest
from pycrawler.crawler import normalize_url

class TestNormalizeUrl(unittest.TestCase):
    def test_https(self):
        input = 'https://blog.boot.dev'
        actual = normalize_url(input)
        expected = 'blog.boot.dev'
        self.assertEqual(actual, expected)

    def test_http(self):
        input = 'http://blog.boot.dev'
        actual = normalize_url(input)
        expected = 'blog.boot.dev'
        self.assertEqual(actual, expected)

    def test_capitalization(self):
        input = 'https://Blog.Boot.dev'
        actual = normalize_url(input)
        expected = 'blog.boot.dev'
        self.assertEqual(actual, expected)

    def test_www(self):
        input = 'https://www.blog.boot.dev'
        actual = normalize_url(input)
        expected = 'blog.boot.dev'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
