#import os
import code

# 자동차 클래스

class Car:
    __number = '54라 9538'

    def get_num(self) -> str:
        return self.__number
    
    #클래스 외부에선 변경x, 멤버함수로는 내부 조작o
    def set_num(self, number) -> str:
        return self.__number

    def __init__(self, number = '54라 9538') -> None:
        self.__number = number
        print('__init__')

#    def __new__(cls):
#        print('__new__')
#        return super().__new__(cls)     #super = Car 클래스의 부모 클래스 - 상속

    def __str__(self) -> str:
        return f'차 번호는 {self.__number} 입니다.'
    
    def get_number(self):
        return self.__number

yourCar = Car('88호 7645')
print(yourCar)
yourCar.__number = '54라 9999'      # 외부에서는 멤버변수에 접근불가
print(yourCar)          # 못 바꿈
print('클래스 내부함수 사용')
yourCar.set_num('55오 5555')
print(yourCar)

myCar = Car()
print(myCar)
print(f'제 차는 아이오닉이고, 번호는 {myCar.get_num()} 입니다')


myCar.__number = '132거 8874'
print(myCar.__number)
print(myCar)

#print(os.environ)