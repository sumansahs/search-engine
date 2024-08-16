import random
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class BiasDetector:
    def __init__(self):
        self.source_count = defaultdict(int)
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def detect_bias(self, results):
        source_counts = defaultdict(int)
        sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
        for result in results:
            source = self.get_source(result['url'])
            sentiment = self.get_sentiment(result['content'])
            source_counts[source] += 1
            sentiments[sentiment] += 1
        return source_counts, sentiments

    def reduce_bias(self, results):
        self.source_count = defaultdict(int)
        sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
        balanced_results = []
        for result in results:
            source = self.get_source(result['url'])
            sentiment = self.get_sentiment(result['content'])
            if self.source_count[source] < 2 and sentiments[sentiment] < 2:  # Example threshold
                balanced_results.append(result)
                self.source_count[source] += 1
                sentiments[sentiment] += 1
        return balanced_results

    def get_source(self, url):
        # Extract the domain as the source
        return url.split("//")[-1].split("/")[0]

    def get_sentiment(self, text):
        score = self.sentiment_analyzer.polarity_scores(text)
        if score['compound'] >= 0.05:
            return 'positive'
        elif score['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

if __name__ == "__main__":
    detector = BiasDetector()
    sample_results = [
        {'url': 'http://biasedsource1.com/article1', 'content': 'This article contains a biased positive opinion about example.'},
        {'url': 'http://biasedsource1.com/article2', 'content': 'This article contains a biased positive opinion about example.'},
        {'url': 'http://neutral.com/article', 'content': 'This article provides a neutral viewpoint on example.'},
        {'url': 'http://biasedsource2.com/article1', 'content': 'This article contains a biased negative opinion about example.'}
    ]
    unbiased_results = detector.reduce_bias(sample_results)
    print(f"Unbiased Results: {[result['url'] for result in unbiased_results]}")
