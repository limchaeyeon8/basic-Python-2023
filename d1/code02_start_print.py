# 별표 찍기

#print ('   *   ')
#print ('  ***  ')
#print (' ***** ')
#print ('*******')


#직각삼각형
a = int(input("정수를 입력하세요"))

for i in range(a):
    for j in range(a,i,-1):
        print('', end='')


    for j in range((i+1)*2-1):
        print("*", end='')
    print()

#속이 빈 삼각형
