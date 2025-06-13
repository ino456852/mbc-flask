import requests
from flask import Flask, render_template
from pymongo import MongoClient
from collections import Counter
import io
import base64
import matplotlib.pyplot as plt
import platform

if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'

plt.rcParams['axes.unicode_minus'] = False 

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['news_db']
questions = db['crawling_news']

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_text_list(html_text, selector):
    from bs4 import BeautifulSoup as bs
    # html을 잘 정리된 형태로 변환
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

def create_graph():
    # 1. 웹 크롤링
    html = web_get("https://news.naver.com/section/101")
    press_list = find_text_list(html, ".sa_text_press")  # 신문사 리스트

    # 2. 신문사별 기사 수 계산 후 정렬
    press_counter = Counter(press_list)
    sorted_press = sorted(press_counter.items(), key=lambda x: x[1], reverse=True)

    # 3. 데이터 분리
    labels = [item[0] for item in sorted_press]
    values = [item[1] for item in sorted_press]

    # 4. 그래프 생성
    plt.figure(figsize=(12, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title("신문사별 기사 수 (많은 순)")
    plt.xlabel("신문사")
    plt.ylabel("기사 수")
    plt.tight_layout()

    # 5. 이미지 버퍼에 저장 후 base64 인코딩
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    image_data = base64.b64encode(buf.read()).decode('utf-8')
    return image_data

@app.route('/')
def home():
    return '''
    <p><a href="/news/crawling">뉴스 크롤링페이지</a></p>
    <p><a href="/news/graph">뉴스 그래프</a></p>
    <p><a href="/news/wordcloud">뉴스 워드클라우드</a></p>
    '''


@app.route('/news/crawling')
def crawling_page():
    html = web_get("https://news.naver.com/section/101")
    titles = find_text_list(html, ".sa_text_strong")  
    press = find_text_list(html, ".sa_text_press")     
    leads = find_text_list(html, ".sa_text_lede")     

    questions.delete_many({})

    news_data = []
    for title, publisher, lead in zip(titles, press, leads):
        news_data.append({
            "title": title.strip(),
            "press": publisher.strip(),
            "lead": lead.strip()
        })
    if news_data:
        questions.insert_many(news_data)
    return render_template('news/crawling.html', titles=titles, press=press, leads=leads)

def get_count(item):
    return item[1]

@app.route('/news/graph')
def graph_page():
    image_data = create_graph()  # base64 인코딩된 그래프 이미지

    html = web_get("https://news.naver.com/section/101")
    press = find_text_list(html, ".sa_text_press")
    press_freq = Counter(press)
    press_table = sorted(press_freq.items(), key=get_count, reverse=True)

    return render_template('news/graph.html',
                            graph_data=image_data,
                            press_table=press_table)


@app.route('/news/wordcloud')
def wordcloud_page():
    return render_template('news/wordcloued.html', wc_url='/static/wordcloud.png')


if __name__ == "__main__":
    app.run(debug=True)

