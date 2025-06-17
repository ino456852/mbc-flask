from flask import Flask, render_template

app = Flask(__name__)

# 경로에 name이라는 URL 변수 받기
@app.route('/greet/<name>')
def greet(name):
    return render_template("greeting.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
