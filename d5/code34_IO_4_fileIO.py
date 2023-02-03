# 파일 읽어오기

file = open('.\\d5\\sample07.md', 'r', encoding='utf-8' )

#text = file.readline()
#print(text)
#print('sample07.md를 읽어왔습니다')

while True:
    text = file.read()

    if not text: break

    print(text)
    print('sample07.md를 읽어왔습니다')


file.close()        # 파일을 오픈하면 반드시 클로즈 해주어야 함