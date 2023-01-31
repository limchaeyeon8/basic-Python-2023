# 자료형

# None
None                    # 컴퓨터왈 : 난몰랑
print(None)             # result == None
print(0 == None)        # result == false
print('' == None)       # result == false


# 숫자형

val = 3
print(type(val))        # class == 'int'

val = 3.14
print(type(val))        # class == 'float'

val = 'Hello'
print(type(val))        # class == 'str'(문자열)


val = 0b1010
print(type(val))        # class == 'int' // 2진수 // 10진수 10

val = 0o52
print(type(val))        # class == 'int' // 8진수 // 10진수 


val = 14.352242524574745646463755758768755569252
print(type(val))        # class == 'float'

val = 4,520,000
print(type(val))        # class == 'tuple'(튜플)

val = 4_520_000
print(type(val))        # class == 'int'

val = 3_099.99
print(type(val))        # class == 'float'



# 문자열형

val = '\nLife is short,\nYou need Python.\n'
print(val)
print(type(val))        # class == 'str'(문자열)

val = '\nHell World!\n'
print(val)
print(type(val))        # class == 'str'(문자열)

val = '\nHell\t\t\tWorld!\n'
print(val)

val = '\nHell\t\t\bWorld!\n'
print(val)

val = '''\nLife is short,
You need Python.\n'''
print(val)


val = "Hi, I'm 'ChaeYeon'"
val = 'Hi, I\'m \'ChaeYeon\''


# 불린형(Boolean) or 불형

참 = True
거짓 = False
print(type(거짓))

print(1 + 1 == 1)       #False
print(1 + 1 == 2)       #True

#거짓이라는 False 값 변수가 참이냐
print(거짓 == True)     #False
print(거짓 == False)    #True
print(거짓 is False)    #True

print(bool(1))          #1 == True
print(bool(0))          #0 == False
print(bool(2))          #2 == True   #파이썬에서 0 외엔 모두 True로 용인 // 하지만, 1 이외의 값은 참이라 하지 말기