# IMDb에서 영화 정보 가져오기: https://www.imdb.com
# 1. 제목
# 2. 평점
# 3. 줄거리
# 4. 감독
# 5. 배우

from bs4 import BeautifulSoup
import requests

target = "https://www.imdb.com/title/tt5848272/?ref_=inth_ov_tt"
raw = requests.get(target)
# print(raw.text)
html = BeautifulSoup(raw.text, 'html.parser')

title = html.select("div.title_wrapper h1")
# print(title[0].text)

rating = html.select("div.ratingValue strong")
# print(rating[0].text)

summary = html.select("div.summary_text")
# print(summary[0].text)

directors = html.select("div.plot_summary_wrapper div.plot_summary div:nth-of-type(2) a")
for director in directors:
    print(director.text)

