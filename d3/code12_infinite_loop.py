# 무한반복 예제

num = 0

while True:             # 무한반복
    print('메뉴를 선택하세요')
    print('1. 회원 입력')
    print('2. 회원 검색')
    print('3. 회원 수정')
    print('4. 회원 삭제')
    print('5. 프로그램 종료')

    num = int(num)      # 문자로 받은 '1'을 숫자 1로 변경//항변화
    num = input('메뉴 번호 입력 > ')

    if num == 1:
        print('회원정보를 입력하세요')

    elif num == 2:
        print('회원을 검색하세요')
    elif num == 3:
        print('회원정보를 수정합니다')

    elif num == 4:
        print('삭제할 회원을 고르세요')

    elif num == 5:
        print('프로그램 종료')
        break
    else:
        continue