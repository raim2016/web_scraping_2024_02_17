import requests
from bs4 import BeautifulSoup

# 웹사이트 URL 설정
url = 'https://news.naver.com/section/101'

# requests를 사용하여 웹 페이지 내용 가져오기
response = requests.get(url) # 지정 웹사이트에 url에 get 요청을 보낸다.

# 웹 페이지의 HTML 내용을 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 a 태그 찾기
news_headline = soup.find_all('a', class_="sa_text_title")

news_body = soup.find_all('div', class_="sa_text_lede")

print(news_headline)
print(news_body)

# news_headline의 뉴스 타이틀만 출력
# for news_title in news_headline:
#     print(news_title.text)
for body in news_body:
    print(body.text)