import requests
from bs4 import BeautifulSoup

TO_CRAWL = ["http://example.com"]
CRAWLED = set()

url = TO_CRAWL.pop()
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, "html.parser")