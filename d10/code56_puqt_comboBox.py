# 체크박스, 라디오 버튼

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lblOption = QLabel('선택값 : ', self)
        self.lblOption.move(20, 20)

        cbOption = QComboBox(self)
        cbOption.addItem('Option1')
        cbOption.addItem('Option2')
        cbOption.addItem('Option3')
        cbOption.addItem('Option4')
        cbOption.addItem('Option5')
        cbOption.move(20, 40)

        cbOption.activated[str].connect(self.onActivated)       # str = Option 아이템들

        # 필수 설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onActivated(self, text):
        self.lblOption.setText('선택값 : ' + text)
        self.lblOption.adjustSize()         # 글자수 만큼 라벨 넓이를 조정


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