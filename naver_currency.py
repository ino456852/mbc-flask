import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8%EA%B3%84%EC%82%B0%EA%B8%B0&ackey=ct030s8y"
def get_currency(debug=False):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.title.text)
    emarr = [el.text.strip() for el in soup.select(".csp dt em, .csd dt em")]
    if debug: print(emarr)
    conarr = [float(el.text.replace(",","")) for el in soup.select(".csp .spt_con strong,.csd .spt_con strong")]
    if debug: print(conarr)
    return dict(zip(emarr,conarr))
if __name__ == "__main__":
    print(get_currency())