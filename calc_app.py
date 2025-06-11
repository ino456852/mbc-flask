from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/calc')
def calc():
    return '''
    <form action="/calc_result">
    <input type="number" name="n1" value="3">
    
    <select name="op">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select>
    
    <input type="number" name="n2" value="5">
    
    <button type="submit">계산</button>
    </form>
'''

@app.route('/calc_result')
def calc_result():
    n1 = request.args.get('n1', default=0, type=int)
    n2 = request.args.get('n2', default=0, type=int)
    op = request.args.get('op', default='+', type=str)

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2 if n2 != 0 else 'Error'

    return f'''
    <h1>계산 결과</h1>
    <p>{n1} {op} {n2} = {result}</p>
    <a href="/calc">다시 계산하기</a>
    '''
    

if __name__ == '__main__':
    app.run(debug=True)