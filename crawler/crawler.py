# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import requests
# from bs4 import BeautifulSoup
# from indexer.indexer import Indexer

# class Crawler:
#     def __init__(self, base_url):
#         self.base_url = base_url
#         self.indexer = Indexer()

#     def fetch(self, url):
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             return response.text
#         except requests.RequestException as e:
#             print(f"Error fetching {url}: {e}")
#             return None

#     def parse(self, html):
#         soup = BeautifulSoup(html, 'html.parser')
#         return [a['href'] for a in soup.find_all('a', href=True)]

#     def crawl(self):
#         html = self.fetch(self.base_url)
#         if html:
#             links = self.parse(html)
#             self.indexer.index(self.base_url, links)
#             for link in links:
#                 print(link)

# if __name__ == "__main__":
#     base_url = ':http//www.google.com'
#     crawler = Crawler(base_url)
#     crawler.crawl()
