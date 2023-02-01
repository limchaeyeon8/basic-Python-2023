# 함수

# 값을 돌려주지 않는 것은 리턴 생략 가능

#1. 함수에 파라미터 있고 리턴 O
#2. 함수에 파라미터 있고 리턴 안 하는 
#3. 함수이 파라미터 없고 리턴 O
#4. 함수에 파라미터 없고 리턴 안 하는

# 함수 정의
def add(x, y):
    result = x + y
    print(result)

def sub(x, y):
    result = x - y
    print(result)

def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)


def hello():
    print('Hello~~~~')

def hello2():
    msg = 'Hello, hello'
    return msg

#함수 호출
hello()
print(hello2())

add(1024, 5)
sub(1024, 1000)
mul(512,2)
div(108,10)

