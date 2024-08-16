import os
import json

class Indexer:
    def __init__(self, storage_path='index_storage'):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def index(self, url, links):
        index_data = {
            'url': url,
            'links': links
        }
        file_path = os.path.join(self.storage_path, self._sanitize_url(url) + '.json')
        with open(file_path, 'w') as f:
            json.dump(index_data, f)
        print(f"Indexed {url} with {len(links)} links.")

    def _sanitize_url(self, url):
        return url.replace('http://', '').replace('https://', '').replace('/', '_')

if __name__ == "__main__":
    indexer = Indexer()
    indexer.index('http://example.com', ['http://example.com/link1', 'http://example.com/link2'])
