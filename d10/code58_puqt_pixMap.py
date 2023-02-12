# 이미지처리 위젯

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        pixmap = QPixmap('./d10/cat.png')

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)

        self.setLayout(vbox)

        # 필수 설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(300, 300, 300, 300)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())        