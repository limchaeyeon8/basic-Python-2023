# 클래스 생성

class Person:
#    pass            # 아직 뭘 적을지 모를 때 사용 // 오류는 사라짐
    name = 'unknown'
    height = ''
    gender = ''
    blood_type = 'A'

# 1. 초기화 추가
    #def __init__(self):
    #    self.name = '자연'
    #    self.height = '172'
    #    self.gender = 'Fem'
    #    self.gender = 'O'

    def __init__(self, name = '자연', height = '171', gender = 'Fem') -> None:   # 매개변수(로컬/지역) != 속성(멤버)변수(글로벌/전역)
        self.name = name            
        self.height = height
        self.gender = gender
    
    def walk(self):
        print(f'{self.name}이(가) 걷습니다')

    
    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빠르게 뜁니다')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다')

    
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다')


# 2. 생성자 외 매직 메서드 __str__
def __str__(self) -> str:
    return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'


yeon = Person('채연', 171, 'Fem')     # 이렇게 만들어지는 "객체" : 인스턴스 # 객체를 인스턴스
# yeon.name       = '임채연'      # 주석처리하면 초기값만 뜸
#yeon.height     = '171'
#yeon.gender     = '여자'
#yeon.blood_type = 'RH+ O'

print(f'{yeon.name}의 혈액형은 {yeon.blood_type}형입니다.')
print(f'{yeon.name}의 키는 {yeon.height}cm입니다.')
print(f'{yeon.name}의 성별은 {yeon.gender}입니다.')

yeon.run('Fast')
yeon.stop()
print(yeon)

# 1. 초기화 후 객체생성
#xa = Person('자연', 171, 'Fem')
xa = Person()
xa.run('Slow')            # 옵션(파라미터)가 필요함
print(xa)

print('================================')

# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'Fem')       #파라미터 입력 안 하면 자연이 나옴//
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)


