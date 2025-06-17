from flask import Flask, render_template, request, redirect, url_for, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.todos # DB

@app.route('/')
def todo_main():
    tasks = list(db.tasks.find().sort('_id'))
    return render_template('todo/todo_main.html', tasks=tasks)


@app.route('/todo_add', methods=['POST'])
def todo_add():
    task_text = request.form.get('task')  
    if task_text:
        db.tasks.insert_one({'text':task_text})
    return redirect('/')


@app.route('/todo_del', methods=['POST'])
def todo_del():
    task_id = request.form.get('task_id')
    if task_id:
        db.tasks.delete_one({'_id':ObjectId(task_id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
