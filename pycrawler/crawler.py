from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

def normalize_url(url_string: str) -> str:
    url = urlparse(url_string)
    hostname = str(url.hostname).replace('www.', '')
    path = url.path

    return f"{hostname}{path}"

def get_urls_from_html(html_string, base_url):
    urls = []
    soup = BeautifulSoup(html_string, 'html.parser')
    links = soup.findAll('a')
    for link in links:
        if 'href' in link.attrs:
            url = urlparse(link.get('href'))

            # skip relative urls that do not start with a /
            if not url.hostname: 
                if not url.path.startswith('/'):
                    continue
                else:
                    # append base_url to relative
                    url = urlparse(f"{base_url}{url.path}")

            url = f"{url.scheme}://{url.hostname}{url.path}"
            urls.append(url)

    return urls

def crawl_page(base_url, current_url, pages):
    parsed_base_url = urlparse(base_url)
    parsed_current_url = urlparse(current_url)

    #skip jpeg/jpg/png files
    extensions = ['.jpeg', '.jpg', '.png']
    if any(extension in current_url for extension in extensions):
        return pages

    if parsed_base_url.hostname != parsed_current_url.hostname:
        return pages

    normalized_url = normalize_url(current_url)
    if pages.get(normalized_url):
        pages[normalized_url] += 1
        return pages
    pages[normalized_url] = 1

    try:
        # print(f"Crawling {current_url}")
        response = requests.get(current_url)

        if response.status_code != 200:
            # print(f"Skipping page with status code: {response.status_code}")
            return pages

        # do not crawl not html pages 
        if not 'text/html' in response.headers['Content-Type']:
            # print(f"Skipping page with Content-Type: {response.headers['Content-Type']}")
            return pages

        raw_html = response.text
        next_urls = get_urls_from_html(raw_html, base_url)

        for url in next_urls:
            pages = crawl_page(base_url, url, pages)

    except requests.RequestException as e:
        print(f"Error during request: {e}")

    return pages
