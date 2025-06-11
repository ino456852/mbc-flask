from flask import Flask

# Flask 애플리케이션 인스턴스 생성
app = Flask(__name__)

# 라우팅(Routing): 특정 URL에 접속했을 때 실행될 함수를 지정
@app.route('/')
def hello_world():
    return '헬로 플라스크!'

@app.route('/info')
def my_name():
    return '내이름은 홍길동!'

@app.route('/now')
def now():
    from datetime import datetime
    return f'현재 시간은 {datetime.now().strftime("%Y-%m-%d %p:%M:%S")}'

@app.route('/today_lotto')
def today_lotto():
    import random
    lotto_numbers = random.sample(range(1, 46), 6)
    return f'오늘의 로또 번호는 {sorted(lotto_numbers)}입니다.'

# 이 파일이 직접 실행될 경우에만 웹 서버를 구동
if __name__ == '__main__':
    app.run(debug=True)
