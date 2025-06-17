from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import datetime

# 로컬 MongoDB에 연결
# MongoClient() 안에 아무것도 넣지 않으면 기본적으로 'mongodb://localhost:27017/'로 연결됩니다.
client = MongoClient('mongodb://localhost:27017/')
db = client.localQnAboard

def get_next_post_num():
    """
    'counters' 컬렉션에서 'post_num'의 seq 값을 1 증가시키고 그 값을 반환합니다.
    """
    # find_one_and_update는 문서를 찾고 업데이트하는 것을 한 번에(원자적으로) 처리합니다.
    # {'$inc': {'seq': 1}} : seq 필드 값을 1 증가시킵니다.
    # return_document=ReturnDocument.AFTER : 업데이트 이후의 문서를 반환하도록 설정합니다.
    # from pymongo.collection import ReturnDocument (상단에 추가 필요)
    from pymongo.collection import ReturnDocument

    doc = db.counters.find_one_and_update(
        {'_id': 'QnA_num'},
        {'$inc': {'seq': 1}},
        return_document=ReturnDocument.AFTER # 업데이트 후의 문서를 반환하라는 뜻
    )
    return doc['seq']

app = Flask(__name__)

@app.route('/ping')
def ping():
    # 연결이 잘 되었는지 터미널에서 확인하기 위한 간단한 테스트
    try:
        client.admin.command('ping')
        return "MongoDB is connected 백인호!"
    except Exception as e:
        return f"Error connecting to MongoDB: {e}"

@app.route('/')
def home():
    return '''
    <p><a href="/QnA/web/list">웹게시판</a></p>
    <p><a href="/QnA/list">QnA 게시판</a></p>
    '''

@app.route('/QnA/list')
def list_page():
    # 'posts' 컬렉션의 모든 문서를 가져오되, 'post_num'을 기준으로 내림차순(-1) 정렬
    all_posts = list(db.posts.find({}).sort("QnA_num", -1))
    return render_template('QnA/list.html', posts=all_posts)

@app.route('/QnA/write')
def write_page():
    
    return render_template('QnA/detail.html')

@app.route('/QnA/post/<int:num>')
def detail_page(num):
    # URL에서 받은 게시물 번호(num)를 이용해 DB에서 해당 게시물을 찾습니다.
    # find_one은 조건에 맞는 문서 하나를 딕셔너리 형태로 반환합니다.
    post = db.posts.find_one({'post_num': num})

    # 만약 해당 번호의 게시물이 없다면? (예외 처리)
    if post is None:
        return "게시물이 존재하지 않습니다.", 404

    # 찾은 게시물 데이터를 detail.html로 넘겨줍니다.
    return render_template('/QnA/detail.html', post=post)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
