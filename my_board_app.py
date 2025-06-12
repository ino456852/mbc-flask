from flask import Flask, render_template, request, redirect, url_for, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# Flask 앱 생성
app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

# 'my_board' 데이터베이스를 가리킵니다
# 1. client 생성 MongoDB오 통신
# 2. client.db이름 생성 -> DB이름
# 3. client.db이름.컬렉션이름 -> 컬렉션이름(데이터저장소)

db = client.posts # DB

# --- 라우트(Route) 정의 ---

# 1. 게시글 목록 보기 (메인 페이지)
@app.route('/')
def list_boards():
    """게시글 목록을 최신순으로 가져와서 list.html에 렌더링합니다."""
    # find()로 모든 게시물을 가져오되, created_at을 기준으로 내림차순(-1) 정렬
    all_boards = db.boards.find().sort('created_at', -1)
    return render_template('my_board/list.html', all_boards=all_boards)

# 2. 게시글 작성 (GET: 폼 보여주기, POST: 데이터 저장)
@app.route('/write', methods=['GET', 'POST'])
def write_post():
    
    return render_template('my_board/write.html')

# 3. POST : 데이터 저장
@app.route('/write_action', methods=['POST'])
def write_action():
        # 폼에서 데이터 받아오기
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        password = request.form['password']

        # 데이터베이스에 저장할 문서(document) 생성
        post_data = {
            'title': title,
            'content': content,
            'author': author,
            'password': password,  # 실제 운영 환경에서는 비밀번호를 암호화해야 합니다.
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
            'view_count': 0
        }

        # 'posts' 컬렉션에 문서 삽입
        db.boards.insert_one(post_data)

        # 글 목록 페이지로 리다이렉트
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)