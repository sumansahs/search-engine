import os

class Config:
    MONGODB_SETTINGS = {
        'db': 'search_engine_db',
        'host': os.getenv('MONGO_URI', 'mongodb://localhost:27017/search_engine_db')
    }

