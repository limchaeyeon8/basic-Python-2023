# 예외처리

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b    # ZeroDivisionError == 예외
                       # 0으로 나누면 무한하게 나누어지므로 금지

x, y = input('두 수를 입력하세요 > ').split()
x = int(x)
y = int(y)

# 원사적인 예외처리
#if y == 0:
#    print('y에 0을 넣지마세요')     # 예외처리(1)   # ZeroDivisionError 고치지만 add, mul 수행이 안 됨
#    exit()

print('계산 테스트')
#try:
#    print(div(x, y))                 # 예외처리(2-1)   # add, mul만 수행
#except:
#    print('나누기 실패 : 0으로 나누려고 했습니다.')  # 예외처리(2-2)   # div 실패에 대한 메시지

try:
    print(div(x, y))
except Exception as e:                 # 예외처리(2-3)  # Exception 클래스로 직접 예외 메시지 안 적어도 자동 표시가능
    print(e)


print(add(x, y))
print(mul(x, y))
