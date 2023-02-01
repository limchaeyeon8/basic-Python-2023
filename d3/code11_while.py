# while문

hit = 0                 # 변수 초기화

while hit < 11:         # while True: -> 무한 반복
    hit += 1            # hit 1씩 증가

    print(f'나무를 {hit}번 찍음')
    if hit == 10:
        print('나무가 쓰러졌다 !')
        break
    else:
        print('효과는 미미했다 . . .')

print('야생의 \'나무\' 를 얻었다 !')


