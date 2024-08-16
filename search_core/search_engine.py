import os
import json
from ml_module.ranker import Ranker
from bias_module.bias_detection import BiasDetector

class SearchEngine:
    def __init__(self, index_path=os.path.join(os.path.dirname(__file__), '..', 'index_storage')):
        self.index_path = index_path
        self.ranker = Ranker()
        self.bias_detector = BiasDetector()

    def search(self, query):
        results = []
        for file_name in os.listdir(self.index_path):
            file_path = os.path.join(self.index_path, file_name)
            with open(file_path, 'r') as file:
                index_data = json.load(file)
                if query in index_data['url'] or any(query in link for link in index_data['links']):
                    results.append({
                        'url': index_data['url'],
                        'content': index_data['content']
                    })
        ranked_results = self.ranker.rank([result['url'] for result in results])
        unbiased_results = self.bias_detector.reduce_bias(results)
        return [result['url'] for result in unbiased_results]

if __name__ == "__main__":
    search_engine = SearchEngine()
    query = 'example'
    results = search_engine.search(query)
    print(f"Search results for '{query}': {results}")
