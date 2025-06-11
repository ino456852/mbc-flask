from flask import Flask
from flask import request

# Flask 애플리케이션 인스턴스 생성
app = Flask(__name__)

# 라우팅(Routing): 특정 URL에 접속했을 때 실행될 함수를 지정
@app.route('/')
def hello_world():
    return '''
        <h1>환율계산기</h1>
        <a href="/current_form">환율계산기</a>
        '''
import naver_currency as nc
currency = nc.get_currency()
        
@app.route('/current_form')
def current_form():
    return '''
        <h2>💱 환율 계산기</h2>

        <form action="/current_calc" method="get"> 
            <label>
            금액 (원 또는 달러):
            <input type="number" id="amount" name="amount" required>
            </label>
            <br><br>

            <label>
            환율(원달러: %s):
            <input type="number" id="rate" name="rate" required>
            </label>
            <br><br>

            <label>
            방향:
            <select id="direction" name="direction">
                <option value="krw_to_usd">원 → 달러</option>
                <option value="usd_to_krw">달러 → 원</option>
            </select>
            </label>
            <br><br>

            <button type="submit">계산</button>
        </form>''' % currency["USD"]

@app.route('/current_calc', methods=['GET'])
def current_calc():
    amount = request.args.get('amount', type=float)
    rate = request.args.get('rate', type=float)
    direction = request.args.get('direction')

    if direction == 'krw_to_usd':
        result = amount / rate
        return f'{amount} 원은 약 {result:.2f} 달러입니다.'
    elif direction == 'usd_to_krw':
        result = amount * rate
        return f'{amount} 달러는 약 {result:.2f} 원입니다.'
    else:
        return '잘못된 방향입니다.'

if __name__ == '__main__':
    app.run(debug=True)
