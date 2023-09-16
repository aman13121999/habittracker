
from flask import Flask
from routes import pages
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://aman1:aman1@cluster0.cm2fuzf.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
    app.db = client.get_default_database()

    app.register_blueprint(pages)
    return app
