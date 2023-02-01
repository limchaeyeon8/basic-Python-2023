# 함수와 변수의 라이프 스코프(수명 주기)

a = 1

#def vartest(a):
#    a = a + 1
#    return a


def vartest(x):
    global a    # 전역 a를 지역에 가져다 씀
    a = a + x + 1
    return a

a = vartest(a)
print(a)