# 예외처리

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b    # ZeroDivisionError == 예외
                       # 0으로 나누면 무한하게 나누어지므로 금지

try:
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('계속되나요. . ?')        # exit() 있어도 이 finally 실행 뒤 종료됨

print('계산 테스트')

try:
    print(div(x, y))
#except ZeroDivisionError as e:     # 사용자가 요구하지 않는 한, 굳이 안 해도 됨
#    print('0으로 나누면 안돼!')
except Exception as e:      # 엑셉션 클래스 예외처리는 맨 아래에 있어야 한다
    print(e)
finally:
    print('계산은 계속됩니다. . .')     # finally : 예외가 생기든/안 생기든 출력되는 메시지

print(add(x, y))
print(mul(x, y))
