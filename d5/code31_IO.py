# 입출력

number = input('수를 입력하세요 > ')
numbers = int(input('수를 입력하세요 > '))



print(number * 5)       # 출력은 문자 => 100 5번 출력
print(numbers * 5)      # int로 입력 되어 연산됨

print('Life' 'is' 'short')
print('Life ' 'is ' 'short')

print('Life', 'is', 'short')

a = [1,2,3,4]
for i in a:
#    print(i)
    print(i, end= ' ')
