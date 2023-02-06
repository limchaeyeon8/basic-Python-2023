# 차 부모클래스

class Car:
    # Mother CLass
    __name__ = '자동차'
    __color = 'white'
    __plate_num = ''
    __product_year = 1900



    def __str__(self) -> str:
        return f'부모 클래스'
    
    def get_name(self):
        return self.__name__
    
    def run(self):
        return f'차가 달립니다'
    
    def stop(self):
        return f'차가 멈춥니다'     # f 없어도 됨
    

