from pycrawler.crawler import *
import sys

def main():
    if len(sys.argv) != 2:
        print('Did not provide a url')
        sys.exit(1)

    url = sys.argv[1]
    pages = crawl_page(url, url, {})
    sorted_pages = dict(sorted(pages.items(), key=lambda item: item[1], reverse=True))
    for page, count in sorted_pages.items():
        print(f"{page}: [{count}]")

if __name__ == '__main__':
    main()
