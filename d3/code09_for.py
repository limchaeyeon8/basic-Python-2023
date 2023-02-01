# for문

arr = [1,2,3,4,5]
sum = 0

for item in arr:            # 1.00\n1\n2.00\n2\n ~~~ \n5
    print(f'{item:2.2f}')   # 1.00 ~ 5.00
    print(item)             # 1 ~ 5
    sum += item             #==) sum = sum + item

print('합계 : ', sum)       # 합계 : 15



# 
vals = [i for i in range(1,11)]     # 리스트를 편하게 만드는 방법
print(vals)

num = 0
for item in vals:
    num += 1
    if num % 2 == 0:
        continue            # 이후의 것을 수행하지 않고 다시 for문으로 감
        break               # break 만나면 for문 완전 탈출
    else:
        print(num, '번째 수는', item, '입니다.')

print(range(10))    == print(range(0,10))
