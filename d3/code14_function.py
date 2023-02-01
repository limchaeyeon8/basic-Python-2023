# 함수


# 함수 정의
def add(x, y):
    result = x + y
    return result

def sub(x, y):
    result = x - y
    return result

def mul(x, y):
    result = x * y
    return result

def div(x, y):
    result = x // y
    return result


#함수 호출
val = add(1024, 5)
print(val)              # return 없으면 리턴이 안 돼서 None 상태

val= sub(1024, 1000)
print(val) 

val= mul(512,2)
print(val) 

val= div(108,10)
print(val) 

