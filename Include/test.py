import requests
from bs4 import BeautifulSoup
import pandas as pd

# 웹사이트 URL 설정
url = 'https://news.naver.com/section/101'

# requests를 사용하여 웹 페이지 내용 가져오기
response = requests.get(url) # 지정 웹사이트에 url에 get 요청을 보낸다.

# 웹 페이지의 HTML 내용을 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# a태그이면서 class 이름이 sa_text_title 를 가져옴
news_headline = soup.find_all('a', class_="sa_text_title")

# div태그이면서 class 이름이 sa_text_lede 를 가져옴
news_body = soup.find_all('div', class_="sa_text_lede")

# print(news_headline)
# print(news_body)

news_titles = []

# news_headline의 뉴스 타이틀만 출력
for title in news_headline:
    news_titles.append(title.text);

# # news_headline의 뉴스 타이틀만 출력
# for body in news_body:
#     print(body.text)
    
news_title_list = {"뉴스제목" : news_titles }

# 추출한 데이터를 엑셀에 저장
df = pd.DataFrame(news_title_list)
df.to_excel("C:/Users/Owner/Desktop/python/뉴스제목.xlsx", index=False)