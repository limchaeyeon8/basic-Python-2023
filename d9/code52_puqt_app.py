# 레이아웃 절대적 배치; 창의 크기를 조절해도 위젯의 크기와 위치가 변하지 않는다
#           - 다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있다
#           - 앱 폰트 바꾸면 레이아웃이 망가질 수 있다
#           - 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 하며, 이것은 매우 번거로움

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOk = QPushButton('OK')           # 헝가리안 표기법
        btnCancel = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnOk)
        hbox.addWidget(btnCancel)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # 필수 설정
        self.setWindowTitle('절대배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

