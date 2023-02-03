# 다중입력

# x, y = input('두 영단어를 입력하세요 > ').split()       # 잘라줌

# print(x)
# print(y)


# 완전 다중입력(*입력갯수 상관 없음)

inputs = list(map(str, input('단어를 입력하세요(개수 상관 없음) > ').split()))  # map():들어오는 값들을 나열해주는 기능 

print(inputs)

inputs = list(map(int, input('정수를 입력하세요(개수 상관 없음) > ').split()))  # 정수 int

print(inputs)

