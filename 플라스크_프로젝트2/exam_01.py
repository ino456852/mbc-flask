import requests     
from bs4 import BeautifulSoup as bs

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_text(html_text, selector):
    soup = bs(html_text, 'html.parser')
    return soup.select_one(selector).get_text()

def find_text_list(html_text, selector):
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

if __name__ == "__main__":
    html = web_get("https://search.naver.com/search.naver?query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
    title = find_text(html,"title")
    print(title)
------------------------------------------------------------------
import requests     
from bs4 import BeautifulSoup as bs

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_text(html_text, selector):
    soup = bs(html_text, 'html.parser')
    return soup.select_one(selector).get_text()

def find_text_list(html_text, selector):
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

if __name__ == "__main__":
    html = web_get("https://search.naver.com/search.naver?query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
    title_list = find_text_list(html,".card_area .this_text ")
    for t in title_list:
        print(t)

------------------------------------------------------------------



import requests     
from bs4 import BeautifulSoup as bs

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_text(html_text, selector):
    soup = bs(html_text, 'html.parser')
    return soup.select_one(selector).get_text()

def find_text_list(html_text, selector):
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

if __name__ == "__main__":
    html = web_get("https://search.naver.com/search.naver?query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
    title_list = find_text_list(html,".card_area .this_text ")
    review = find_text_list(html,".card_item .num")
    for t, r in zip(title_list, review):
        print(f"제목: {t}, 별점: {r}")

------------------------------------------------------------------

import requests     
from bs4 import BeautifulSoup as bs

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_text(html_text, selector):
    soup = bs(html_text, 'html.parser')
    return soup.select_one(selector).get_text()

def find_text_list(html_text, selector):
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

if __name__ == "__main__":
    html = web_get("https://search.naver.com/search.naver?query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
    title_list = find_text_list(html,".card_area .this_text ")
    review = find_text_list(html,".card_item .num")
    for t, r in zip(title_list, review):
            review = float(r)
            if review >= 8.0:
                print(f"제목: {t}, 별점: {review}")



------------------------------------------------------------------
import requests     
from bs4 import BeautifulSoup as bs

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_text(html_text, selector):
    soup = bs(html_text, 'html.parser')
    return soup.select_one(selector).get_text()

def find_text_list(html_text, selector):
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

if __name__ == "__main__":
    html = web_get("https://search.naver.com/search.naver?query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
    title_list = find_text_list(html,".card_area .this_text ")
    review = find_text_list(html,".card_item .num")
    review_mean = []
    for r in review:
        review_mean.append(float(r))
    avg_review = sum(review_mean) / len(review_mean)
    print(f"전체 영화의 평균 평점: {round(avg_review,2)}")


