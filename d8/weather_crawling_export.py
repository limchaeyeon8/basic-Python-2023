# %% [markdown]
# ## 웹 크롤링
# 
# ### 인터넷 접속 라이브러리 추가

# %%
# 1. urllib 호출
from urllib.request import urlopen, Request     #d5 urallib 불러오기 <<< 참고

# 2. 도시별 날씨 검색함수
def get_weather(city):
    # 기상청 홈페이지 - 도시별 날씨 페이지
    url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
    page = urlopen(url=url)

    text = page.read().decode('utf-8')
    text = text[text.find(f'>{city}</a>'):]

# 기온 가져오기
    for i in range(7):          # 총 13 raw
        text = text[text.find(f'<td>')+1:]

    start = 3                   # # 3 번째 이후 인덱스 ~ ((( 'td>' 제외하고 읽기)))
    end = text.find('</td>')
    current_temp = text[start:end]

    print(f'{city}의 현재 기온은 {current_temp}˚C 입니다')


# 습도 가져오기
    for i in range(3):          # 7 + '3' => '10' 위치
        text = text[text.find(f'<td>')+1:]

    start = 3                   
    end = text.find('</td>')     
    current_hum = text[start:end]

    print(f'{city}의 현재 기온은 {current_hum}% 입니다')


# 3.
get_weather('부산')


