import unittest
from pycrawler.crawler import get_urls_from_html

class TestGetUrlsFromHttp(unittest.TestCase):
    def test_base(self):
        base_url = 'https://google.com'
        input = """
            <html>
                <head>
                    <title>Sample Page</title>
                </head>
                <body>
                    <h1>Hello, World!</h1>
                    <p>This is a sample HTML page.</p>
                    <a href="https://google.com">Sample Link</a>
                </body>
            </html>
        """
        actual = get_urls_from_html(input, base_url)
        expected = ['https://google.com']
        self.assertEqual(actual, expected)

    def test_absolute_path(self):
        base_url = 'https://google.com'
        input = """
            <html>
                <head>
                    <title>Sample Page</title>
                </head>
                <body>
                    <h1>Hello, World!</h1>
                    <p>This is a sample HTML page.</p>
                    <a href="https://google.com/search">Sample Link</a>
                </body>
            </html>
        """
        actual = get_urls_from_html(input, base_url)
        expected = ['https://google.com/search']
        self.assertEqual(actual, expected)

    def test_absolute_relative(self):
        base_url = 'https://google.com'
        input = """
            <html>
                <head>
                    <title>Sample Page</title>
                </head>
                <body>
                    <h1>Hello, World!</h1>
                    <p>This is a sample HTML page.</p>
                    <a href="/search">Sample Link</a>
                </body>
            </html>
        """
        actual = get_urls_from_html(input, base_url)
        expected = ['https://google.com/search']
        self.assertEqual(actual, expected)

    def test_absolute_query(self):
        base_url = 'https://google.com'
        input = """
            <html>
                <head>
                    <title>Sample Page</title>
                </head>
                <body>
                    <h1>Hello, World!</h1>
                    <p>This is a sample HTML page.</p>
                    <a href="https://google.com/search?q='cats'">Sample Link</a>
                </body>
            </html>
        """
        actual = get_urls_from_html(input, base_url)
        expected = ['https://google.com/search']
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
