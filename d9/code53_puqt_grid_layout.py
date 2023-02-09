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
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'), 0, 0)       # raw, column = 0, 0
        grid.addWidget(QLabel('Author'), 1, 0)
        grid.addWidget(QLabel('Review'), 2, 0)

        grid.addWidget(QLineEdit(''), 0, 1)      # 0행 1렬
        grid.addWidget(QLineEdit(''), 1, 1)      # 1행 1렬
        grid.addWidget(QTextEdit(''), 2, 1)      # 2행 1렬

        btnOk = QPushButton('OK')           # 헝가리안 표기법
        btnCancel = QPushButton('Cancel')

        grid.addWidget(btnOk, 3, 2)
        grid.addWidget(btnCancel, 3, 3)

        # 필수 설정
        self.setWindowTitle('박스배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

