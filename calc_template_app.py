from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/calc')
def calc():
    return render_template('calc/calc.html')

@app.route('/calc_result')
def calc_result():
    n1 = request.args.get('n1', default=0, type=int)
    n2 = request.args.get('n2', default=0, type=int)
    op = request.args.get('op', default='+')

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2

    return render_template('calc/calc_result.html', n1=n1, n2=n2, op=op, result=result)
    

if __name__ == '__main__':
    app.run(debug=True)