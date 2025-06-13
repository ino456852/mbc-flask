from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
from  pymongo import MongoClient


app = Flask(__name__)

# 그래프 생성 함수
def create_graph():
    # 데이터를 준비합니다.
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 5, 3]

    # 그래프를 그립니다.
    plt.plot(x, y)
    plt.title("Simple Graph")
    plt.xlabel("X")
    plt.ylabel("Y")

    # 그래프를 이미지로 저장합니다.
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # 이미지 데이터를 base64로 인코딩하여 반환합니다.
    image_data = base64.b64encode(buf.read()).decode('utf-8')
    return image_data

# Flask 뷰 함수
@app.route('/')
def index():
    image_data = create_graph()  # 그래프를 생성합니다.
    # return render_template('index.html', image_data=image_data)  # 템플릿에 이미지 데이터를 전달합니다.
    return f"""
    <img src="data:image/png;base64,{ image_data }" alt="Graph" />

    """


@app.route('/apt_graph')
def apt():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["apartment_db"]
    collection = db["sales_data"]
    raw_data = collection.find({}, {"_id": 0, "거래금액(만원)": 1, "전용면적(㎡)": 1})
    x = []
    y = []
    for doc in raw_data:
        try:
            price = int(str(doc.get("거래금액(만원)", "0")).replace(",", ""))
            area = float(doc.get("전용면적(㎡)", 0))
            x.append(area)
            y.append(price)
        except:
            continue

    # 산점도 그래프 생성
    import matplotlib
    import matplotlib.pyplot as plt

    matplotlib.rcParams['font.family'] = 'Malgun Gothic'
    matplotlib.rcParams['axes.unicode_minus'] = False
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.5)
    plt.xlabel('전용면적(㎡)')
    plt.ylabel('거래금액(만원)')
    plt.title('전용면적 vs 거래금액 산점도')

    # 이미지 메모리 저장
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
    plt.close()
    return f"""
        <img src="data:image/png;base64,{ img_base64 }" alt="Graph" />

        """


if __name__ == '__main__':
    app.run(debug=True)