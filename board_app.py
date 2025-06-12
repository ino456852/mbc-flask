from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import datetime # 작성 시간을 기록하기 위해 임포트

app = Flask(__name__)

# --- MongoDB 연결 ---

client = MongoClient('mongodb://localhost:27017/')

db = client.posts# 'posts' 라는 이름의 데이터베이스에 접속 (없으면 자동 생성)
# --------------------

@app.route('/')
def home():
    # posts 컬렉션의 모든 document를 조회합니다.
    # created_at 필드를 기준으로 내림차순(-1) 정렬합니다.
    all_posts = list(db.posts.find({}).sort('created_at', -1))

    return render_template('board/index.html', posts=all_posts)

# --- 게시글 작성을 위한 라우트 ---
@app.route('/write')
def write():
    return render_template('board/write.html')

@app.route('/save', methods=['POST'])
def save():
    # 1. 클라이언트가 보낸 데이터 받기
    title = request.form['title_give']
    content = request.form['content_give']

    # 2. 데이터베이스에 저장할 document 만들기
    doc = {
        'title': title,
        'content': content,
        'created_at': datetime.datetime.now(datetime.timezone.utc) # UTC 시간으로 저장
    }

    # 3. posts 컬렉션에 document 삽입
    db.posts.insert_one(doc)

    return redirect(url_for('home')) # home()함수와 연결된 URL로 리다이렉트

if __name__ == '__main__':
    app.run(debug=True)
