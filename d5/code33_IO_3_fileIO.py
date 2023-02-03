# 글자 인코딩 
# ASCII (아스키) -> 한 단어를 표현하는 체계(영어)
# Unicode (유니코드; UTF-8) -> 모든 나라 언어를 다 표현 가능
# encoding='utf-8' : 유니코드화

# 파일경로

# 파일 만들기

f = open(".\d5\sample07.md", 'w', encoding='utf-8')  # 파일 쓰기로 만듦    #encoding='utf-8' : 유니코드화
#f = open(".\DEV\..\d5\\sample06.md", 'w', encoding='utf-8')  # 파일 쓰기로 만듦    #encoding='utf-8' : 유니코드화
#f = open("C:\\DEV\\temp\\bank\\sample01.md", 'w', encoding='utf-8')  # 파일 쓰기로 만듦    #encoding='utf-8' : 유니코드화
# f = open("C:/DEV/temp/bank/sample01.md", 'w', encoding='utf-8')  # 파일 쓰기로 만듦    #encoding='utf-8' : 유니코드화

#f.write('# 첫 번째 파일 생성\n')       # 한글작성하면 아스키코드로 나오면서 다 깨짐
f.write('# 7 번째 파일 생성\n')       # 한글작성하면 아스키코드로 나오면서 다 깨짐
f.write('   상대경로에 생성~')

f.close()
#print('smaple.md가 생성되었습니다')
print('smaple07.md가 생성되었습니다')

