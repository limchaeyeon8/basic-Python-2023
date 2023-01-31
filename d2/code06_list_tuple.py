# 복합형 # 리스트

arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)

sum = 0
for i in arr:
    sum += i

print(sum, end='\n\n')

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 13, 'World!', True]

print(arr1)
print(arr2)
print(arr3, end='\n\n')

print(type(arr3), end='\n\n')

arr4 = []       # 빈 리스트
arr5 = list()
print(arr5, end='\n\n')

arr6 = [1,2,3,4,[6,7,8,[9,10]]]     #액자식 리스트 가능 #3차원 배열
print(arr6, end='\n\n')

arr7 = [[1,2,3,4],[5, 6,7,8,9,10]]      #2차원 배열
print(arr7, end='\n\n')


# 튜플

tuple1 = (1,2,3,4)
print(tuple1)

arr5.append('4')
print(arr5)             #['4']

#tuple1.append(4)       #error  # 한 번 생성된 튜플은 불변
#print(tuple1)
#print(type(tuple1))    #빨간 밑줄이 없다면 터미널에 오류메시지
