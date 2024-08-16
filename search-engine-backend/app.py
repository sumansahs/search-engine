from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['search_engine']
search_collection = db['searches']

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    # Check if the query is in the database
    cached_result = search_collection.find_one({'query': query})
    if cached_result:
        return jsonify(cached_result['results'])

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    search_results = []
    for g in soup.find_all(class_='g'):
        title = g.find('h3').text if g.find('h3') else 'No title'
        link = g.find('a')['href'] if g.find('a') else 'No link'
        snippet = g.find(class_='IsZvec').text if g.find(class_='IsZvec') else 'No snippet'
        search_results.append({'title': title, 'link': link, 'snippet': snippet})

    image_response = requests.get(f"https://www.google.com/search?tbm=isch&q={query}", headers=headers)
    image_soup = BeautifulSoup(image_response.text, 'html.parser')

    image_results = []
    for img in image_soup.find_all('img'):
        image_src = img.get('data-src') or img.get('src')
        if image_src:
            image_results.append({'src': image_src})

    results = {'search_results': search_results, 'image_results': image_results}

    # Store results in MongoDB
    search_collection.insert_one({'query': query, 'results': results})

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
