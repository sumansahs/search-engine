from mongoengine import Document, StringField, URLField

class SearchResult(Document):
    title = StringField(required=True)
    link = URLField(required=True)
    snippet = StringField()
