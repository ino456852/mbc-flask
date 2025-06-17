from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['qna_db']
questions = db['questions']

@app.route('/qna')
def qna_list():
    all_qna = questions.find()
    return render_template('/qna/qna_list.html', qna_list=all_qna)

@app.route('/qna/write', methods=['GET', 'POST'])
def qna_write():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        questions.insert_one({'title': title, 'content': content, 'answers': []})
        return redirect(url_for('qna_list'))
    return render_template('qna/qna_write.html')

@app.route('/qna/<id>')
def qna_detail(id):
    qna = questions.find_one({'_id': ObjectId(id)})
    return render_template('qna/qna_detail.html', qna=qna)

@app.route('/qna/answer', methods=['POST'])
def qna_answer():
    qna_id = request.form['qna_id']
    answer = request.form['answer']
    questions.update_one(
        {'_id': ObjectId(qna_id)},
        {'$push': {'answers': answer}}
    )
    return redirect(url_for('qna_detail', id=qna_id))

if __name__ == '__main__':
    app.run(debug=True)
