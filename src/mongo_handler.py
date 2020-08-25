from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection
from typing import Dict, List


class MongoHandler:
    def __init__(self, mongo_uri: str) -> None:
        client = MongoClient(mongo_uri)
        db = client.get_default_database()
        self.collection = db['advertisements']

    def get_adverts(self, _: str) -> List[Dict]:
        return list(self.collection.find())
