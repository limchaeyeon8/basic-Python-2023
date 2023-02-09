# 창 닫기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
      super().__init__()
      self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        # 버튼 툴팁
        btn.setToolTip('이거 누르면 그냥 꺼져요. <b>조심</b>하세요!!!')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowIcon(QIcon('./d9/monitor.png'))      # <a href="https://www.flaticon.com/free-icons/dashboard" title="dashboard icons">Dashboard icons created by Freepik - Flaticon</a>
        self.setWindowTitle('Quit Button')
        self.setGeometry(900, 200, 400, 200)  # x, y, w, h
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())