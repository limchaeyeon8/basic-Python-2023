# 공공데이터 포털 csv 파일 읽기
# 부산광역시 시내버스, 마을버스 현황

import csv

fileName = 'BusBus.csv'
dirName = 'C:/Source/studyPython2023/'
fullPath = dirName + fileName         # 경로 합치기


file = open(fullPath, 'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')        #delimiter=',' : 구분자
next(reader)

for line in reader:
    print(line)

file.close()        # 반드시 닫아주세요!!!!

# 출력 자료구조 : 리스트
# 제목줄은 생략하여 셀 내용 읽어옴