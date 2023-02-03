# 모듈 사용

# 랜덤 숫자 출력
import random

#print(random.choice(range(1,7)))

numbers = [i for i in range(1,46)]  #1~45 리스트
lottery = []

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)
