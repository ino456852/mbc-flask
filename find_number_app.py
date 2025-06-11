from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <h1>숫자맞추기게임</h1>
        <a href="/find_number">게임 시작</a>
        '''

@app.route('/find_number')
def find_number():
    return '''
        <h1>숫자 맞추기 게임</h1>
        <form action="/check_number">
            <label for="user_number">1부터 100 사이의 숫자를 입력하세요</label>
            <br>
            <input type="number" name="no" min="1" max="100" required>
            <button type="submit">정답확인</button>
        </form>
    '''
import random
COM_NUM = random.randint(1,100)

@app.route('/check_number')
def check_number():
    no = request.args.get('no', default=0, type=int)
    result = '''
        <h1>숫자 맞추기 게임</h1>
        <form action="/check_number">
            <label for="user_number">1부터 100 사이의 숫자를 입력하세요</label>
            <br>
            <input type="number" name="no" min="1" max="100" required>
            <button type="submit">정답확인</button>
        </form>
        <div>%s</div>
    '''
    if no == 0:
        return result %  '숫자를 입력해주세요'
    if COM_NUM == no:
        return result %  str(no)+ '정답입니다'
    if COM_NUM < no:
        return result %  str(no)+ '낮춰주세요'
    return result %  str(no)+ '높여주세요'

if __name__ == '__main__':
    app.run(debug=True)