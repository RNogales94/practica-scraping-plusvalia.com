import datetime
import os

from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()


class MongoDB:
    def __init__(self):
        mongo_user = os.getenv("MONGO_USER")
        mongo_pass = os.getenv("MONGO_PASSWORD")
        self.collection = os.getenv("COLLECTION_NAME")
        mongo_hostname = os.getenv("MONGO_HOSTNAME")

        uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_hostname}/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(uri)
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def insert_wikipedia_text(self, title: str, text: str):
        eig_db = self.client.get_database("eig")
        col = eig_db.get_collection(self.collection)
        col.insert_one({
            "title": title,
            "content": text,
            "date": datetime.datetime.now()
        })



if __name__ == "__main__":
    m = MongoDB()
    m.insert_wikipedia_text('prueba 2', 'hola, esto es otra prueba con otro esquema!')
