from flask import Blueprint, request, jsonify
from models import SearchResult

api = Blueprint('api', __name__)

@api.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = SearchResult.objects.filter(title__icontains=query)
    return jsonify(results)
