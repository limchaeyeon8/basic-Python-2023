# 콘솔출력 보충
# 이스케이프 캐릭터 (탈출 문자)

print('1. Hello.\r\nWorld')
print('2. Hello.\nWorld')      # 사용 권장

print('3. Hello.\n\tWorld')
print('4. Hello.\tWorld')      

print('5. Hello.\t\bWorld')
print('6. Hello.\bWorld')      

print('7. Hello.\n\'World\'')   # 문자열 내 홑따옴표
print('8. Hello. "World"')
print('9. Hello.\"World\"')

print('10. Hello.\\ World')     # \를 문자열에 표현

print('11. Hello.\0')           # 문자열이 끝


# 문자열 포맷팅 - 구닥다리
# %로 포맷코드 시작

me = '저'
name = '채연'
age= 23
print('%s 는 %s 입니다. %d 입니다.' % (me, name, age))

print(f'{234.463636:.2f}')      # 최신식

print('%4.4f' %(234.46363))     # 구식  // 정수 전체자리수/ 소수점자리수
print('%9.4f' %(234.46363))     # 실제자릿수보다 크면 앞공백 생길 수도





