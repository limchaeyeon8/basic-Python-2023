# 연산자
# 할당 연산; assignment
# 2=1 (x)

val = 1
# 1 = val (x)


# equal 연산자

print(1==1)     #True

# 사칙연산

print(1+1)
print(1-1)
print(10*10)
print(2 ** 10)      #2의 10승
print(1024 / 2)     #나누기
print(1024 // 2)    #정수형 나누기
print(1024 % 2)     #나머지 0

print(1 // 3)       #0
print(1 % 3)        #1

print(1 // 2)        #0
print(1 % 2)        #1

print(3 // 3)       #1
print(3 % 3)        #0

print(4 // 3)       #1
print(4 % 3)        #1

print(6 // 3)       #2
print(6 % 3)        #0

print(8 // 3)       #2
print(9 % 3)        #0
print(12 % 3)       #####나머지를 이용하여 배수 계산 가능

### zero devision ###
# print(6 // 0)     #error
# print(6 % 0)      #0


# 문자열 연산   # +, *만 존재

first = 'Hello'
second = 'World'
print(first + ' ' + second)     # == print(first, second)

print(first * 4)        # 문자열 반복

# 문자열 길이
print(len(first))       #5
print(first[0])       
print(first[1])       
print(first[2])       
print(first[3])       
print(first[4])       
# print(first[5])       # 존재하지 않음


# 파이썬에서 인덱스 찾는 특이한 방법    #거꾸로 인덱스를 찾아감
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])        
# print(first[-6])        #error

# 리스트 슬라이싱
current = '2023-01-31 15:14:02' #현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print('\n' + (current[0:4]) + '년' + (current[5:7]) + '월' + (current[8:10]) + '일' + (current[11:13]) + '시' + (current[14:16]) + '분' + (current[17:]) + '초')

print(current[-19:-15])



# 리스트 연산

que = [1,2,3,4,5]
que[0] = 7
print(que)          #해당 인덱스 변경

tup = (1,2,3,4,5)
#tup[1] = 9         #튜플은 변경 안 됨
print(tup)

# que[5] = 10       #error #최고 인덱스는 4
print(que)

que.append(10)      # ((뒤에서))배열이 늘어나며 삽입 가능
print(que)

que.insert(3, 99)   #((원하는 위치에서))배열이 늘어나며 삽입 가능
print(que)

que.remove(99)      #해당값 삭제
print(que)


# 문자열 == 문자열 리스트(특수한 리스트)

title = 'python'
print(title)
print('\n')


# title[0] = 'P'    # 문자열에서는 값변경x
# print(title[0])
print('P' + title[1:])
print(title[0])
print('\n')

# 일반적인 문자형 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
text[0] = 'P'
print(text)
print('\n')


# 문자열 포맷팅
print("I'm so happy {0} you {1} ".format('to see','!!'))       # .format([문자,실수,정수,등등 가능])

# 최신식 문자열 포맷팅
preword = 3
sayHello = 'Hey'
print(f"{sayHello}, me {preword}. I'm so happy {'to see'} you{'!!'}")


pi = 3.1415928979
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.2f}입니다.')       # 소수점 2번째 자리까지 출력
print(f'파이는 {pi:10.3f}입니다.', end = '\n\n')       # 앞에 공백 + 소수점 3번째 자리까지 출력

#특정문자로 문자열 가르기
full_name = 'Chae Yeon. Lim'
print (full_name.split())               #스페이스
vals = full_name.split('.')             #.
print(vals)
age = 23
print(f"Hello! I'm {full_name}, and I'm {age:2.2f}.")
print(f"Hello! I'm {vals[0]}, and I'm {age:2.2f}.")
print(f"Hello! I'm {vals[1]}, and I'm {age:2.2f}.")

print(full_name.replace((vals[0]), 'Chloe'))    # replce로 교체


# 문자열 공백 없애기 ##############################

hi = '           Hello, bye          '
print(hi.lstrip() + '|')      #좌측 공백 제거
print(hi.rstrip() + '|')      #우측 공백 제거
print(hi.strip()  + '|')      #양측 공백 제거

# 문자열에서 값 찾기
print(full_name.index('e'))    #인덱스 위치 //없는 문자면 value error

print(full_name.find('z'))      #찾는 게 없으면 -1 리턴
print(full_name.find('o'))      

# 찾는 단어의 개수 알려줌
print(full_name.count('e')) 


# 모든 단어를 대문자/소문자로 변경
print(full_name.upper())
print(full_name.lower())


# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)

