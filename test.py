from flask import Flask, render_template, request, redirect, url_for, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.todos # DB

@app.route('/greet/<name>')
def greet(name):
    name = 'Alice'
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)