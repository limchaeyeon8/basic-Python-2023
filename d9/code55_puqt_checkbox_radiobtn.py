# 체크박스, 라디오 버튼

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        cbShortTitle = QCheckBox('Show Title', self)
        cbShortTitle.move(20, 20)     # 옮긴다 / 절대배치
        cbShortTitle.toggle()

        # signal 종류 stateChanged
        # connect() 매개 변수 안에 -> 슬롯 함수
        cbShortTitle.stateChanged.connect(self.changeTitle)

        cbKorea = QCheckBox('한국', self)
        cbKorea.move(20, 60)
        cbKorea.stateChanged.connect(self.checkKorea)

        rbFem = QRadioButton('여', self)
        rbFem.move(200, 20)
        rbFem.setChecked(True)

        rbMal = QRadioButton('남', self)
        rbMal.move(200, 60)
#        rbMal.setChecked(True)

        # 필수 설정
        self.setWindowTitle('버튼')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def changeTitle(self, state):
        if state == Qt.CheckState.Checked:          # Qt.Checked 도 사용 가능
            self.setWindowTitle('체크박스 체크')
        else:
            self.setWindowTitle('체크박스 체크 해제')

    def checkKorea(self,state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('나는 누구')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())