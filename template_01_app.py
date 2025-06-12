# render_template 함수를 추가로 불러옵니다.
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index(): # 함수 이름도 역할에 맞게 변경해주는 것이 좋습니다.
    # 'Hello, World!'를 반환하는 대신, index.html 파일을 렌더링(rendering)합니다.
    my_name='백인호'
    return render_template('index.html',username=my_name)


@app.route('/hobby')
def hobby():
    my_name = "이순신"
    # 사용자의 취미 목록(리스트)을 전달해 봅시다.
    my_hobbies = ['독서', '코딩', '영화 감상']
    return render_template('index.html', username=my_name, hobbies=my_hobbies)

@app.route('/gugudan')
def gugudan():
    dan = 3
    result = [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]
    return render_template('gugudan.html', dan=dan, result=result)

@app.route('/gugudan2')
def gugudan2():
    dan = 5
    result = [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]
    return render_template('gugudan2.html', dan=dan, result=result)

@app.route('/gugudan3')
def gugudan3():
    dan = 5
    result = [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]
    return render_template('gugudan/gugudan3.html', dan=dan, result=result)

@app.route('/gugu', methods=['POST'])
def gugu():
    dan = request.form.get('dan', type=int)
    results = []
    for i in range(2, 10):
        results.append(f"{dan} × {i} = {dan * i}")
    return render_template('gugudan/gugu.html', dan=dan, results=results)

@app.route('/profile')
def profile():
    age = 30
    name = '백인호'
    hobby= '코딩'
    return render_template('profile.html' ,age=age, name=name, hobby=hobby)

if __name__ == '__main__':
    app.run(debug=True)
