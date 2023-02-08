# 외부 패키지 사용

import requests

res = requests.get('https://www.naver.com')
print(res.status_code)          # 200
print('================\n')
print(res.content)
