# if문

names = ['채연', '자연', '메롱']
# name = names[1]
state = ['아픔', '안 아픔']

if names != names[2]:      # name과 '메롱'이 같지 않은 것이 참인 경우ㅡ
    print(f'{names[1]}씨, 진료실에서 담당의사를 만납니다.')
    if state == state[0]:
        print('선생님 배가 아파요...')
        print('어떻게 아프십니까?')
    else:
        print('어디가 아파서 오셨어요?')
        print('막 열도 나고 배도 아프구 학교 가기 싫구...')
        print('꾀병입니다.')

elif names == names[0]:
    print(f'{names[0]}씨, 주사실로 갑니다.')
    print('따끔~')
    print('채연씨, 진료실로 가주세요.')

else:
    print('대기해주세요.')