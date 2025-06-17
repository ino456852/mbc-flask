from flask import Flask, render_template, redirect

app = Flask(__name__)

books = [
    {"id": 1, "title": "플라스크 웹 프로그래밍", "publisher": "한빛미디어", "genre": "프로그래밍", "status": "대여가능"},
    {"id": 2, "title": "데이터 분석 입문", "publisher": "이지스퍼블리싱", "genre": "데이터분석", "status": "대여중"},
    {"id": 3, "title": "파이썬으로 배우는 알고리즘", "publisher": "길벗", "genre": "알고리즘", "status": "대여가능"},
    {"id": 4, "title": "AI 시대의 통계학", "publisher": "프리렉", "genre": "통계", "status": "대여가능"},
]

@app.route("/")
def index():
    total_books = len(books)
    toggle_books = sum(1 for book in books if book['status'] == '대여가능')
    return render_template("book/index.html", books=books, total=total_books, toggle=toggle_books)

@app.route("/toggle/<int:book_id>", methods=["POST"])
def toggle(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "대여가능":
                book["status"] = "대여중"
            else:
                book["status"] = "대여가능"
            break
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
