# 모듈 사용

import math as m            # class로 안 된 모듈

import code22_person as p   # 우리가 만든 class
from code23_vehicle import Car

print(m.pi)
print(m.sin(0))
print(m.cos(0))
print(m.tan(0))
print(m.ceil(3.8))      # 올림
print(m.floor(3.8))     # 내림
print(2**10)
print(m.pow(2,10))


# 우리가 만든 모듈을 사용

me = p.Person('자연', 171, '여')
print(me)

# 
mycar = Car()
print(mycar)