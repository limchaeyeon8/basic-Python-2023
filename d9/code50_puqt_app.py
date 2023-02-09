# 스타일

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정

        lbl_red = QLabel('Fairy Winkle')
        lbl_red.setStyleSheet('color: #8aa4c3;'
                              'border-style: solid;'
                              'border-width: 5px;'
                              'border-color: #c2d1e3;'             ##c2d1e3
                              'border-radius: 10px;'
                              )
        
        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet('color: #6bac97;'
                              'border-style: dashed;'
                              'border-width: 5px;'
                              'border-color: #85ceb7;'             ###85ceb7
                              #'border-radius: 10px;'
                              )

        vBox = QVBoxLayout()     # 레이아웃을 세로 구분짓는 레이아웃 // QHBoxLayout() : 가로로 배치
        vBox.addWidget(lbl_red) # 위젯 추가
        vBox.addWidget(lbl_green) # 위젯 추가

        self.setLayout(vBox)    # 전체 레이아웃에 vBox 추가

        # 기본 설정 - 사이즈, show() 필수!!
        self.setWindowTitle('▷스타일 지정')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

