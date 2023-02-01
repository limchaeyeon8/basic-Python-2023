# 매개변수 개수가 일정치 않은 경우

def add(*args):         # arguments
    result = 0
    for i in args:
        result += i
    
    return result

print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))
print(add(1,2,3,4,5,6,7,8,9,10,11,12,114,15,15,6,3,636,37))

