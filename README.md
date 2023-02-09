# studyPython2023
부경대 IoT 파이썬 학습 리포지토리

## 1일차 - 1주차
1. 기본구성
    - Git/GitHub 설치 및 연동
    - Visual Studio Code 설치 및 연동
    - Python 설치

2. 파이썬 기본
    - 콘솔 출력(1)
    - 주석


```python
# desc : 콘솔 출력 - 주석
print('Hello, Python!') # 콘솔출력 함수
```

## 2일차
1. 파이썬 기본
    -콘솔출력(2)
    - 변수
    - 자료형
    - 연산자
```python
#자료형
val = 1             #변수
print(type(val))    # <class 'int'>

#문자열 포맷팅
pi = 3.1415928979
print(f'파이는 {pi}입니다.')        #파이는 3.1415928979입니다.
print(f'파이는 {pi:0.2f}입니다.')       #파이는 3.14입니다. # 소수점 2번째 자리까지 출력
print(f'파이는 {pi:10.3f}입니다.', end = '\n\n')       #파이는      3.142입니다.
                                               # 앞에 공백 + 소수점 3번째 자리까지 출력
```

    - 흐름제어


## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수


## 4일차
1. 파이썬 기본
    - 가상환경
    - 객체지향 프로그래밍 OOP
    - 패키지, 모듈


## 5일차
1. 파이썬 기본
    - 패키지 계속
    - 입출력 다시
    - 예외처리


## 6일차 - 2주차
1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중상속

2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/limchaeyeon8/studyPython2023/blob/main/project1/add_app.py)

![실행화면](https://raw.githubusercontent.com/limchaeyeon8/studyPython2023/main/Images/addr_app.png)

실행화면


## 7일차
1. 파이썬 응용
    - 주피터 노트북
        - 노트북 생성 : 파일> 새파일 // cTL + aLT + Win+ N 
        - 
    - 리스트 연산 추가
    - 라이브러리 사용법
        - folium (지도 라이브러리)


## 8일차
1. 파이썬 응용
    -라이브러리 사용법
        - urllib.request
    - 웹 크롤링
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링
    - 자료구조 추가
    - 윈폼 개발(GUI)
    - 응용 학습


![실행화면](https://raw.githubusercontent.com/limchaeyeon8/studyPython2023/main/Images/jupyterFolium.png)

Folium OpenAPI 연동화면
    - 검색 단어 '운동장'

## 9일차
1. 파이썬 응용
    - GUI 개발 
        - Tkinter(구식 방법) 소개
        - PyQt 소개 및 설치
    - 자료구조 추가
