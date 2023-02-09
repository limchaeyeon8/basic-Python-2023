# 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
      super().__init__()
      self.initUI()

    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./d9/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q')       # 단축키 지정
        actExit.setStatusTip('앱종료')
        actExit.triggered.connect(qApp.quit)


        actSave = QAction(QIcon('./d9/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actExit.setStatusTip('저장')

        actEdit = QAction(QIcon('./d9/edit.png'), 'Edit', self)
        actEdit.setShortcut('Ctrl+E')
        actExit.setStatusTip('수정')

        actPrint = QAction(QIcon('./d9/print.png'), 'Print', self)
        actPrint.setShortcut('Ctrl+P')
        actExit.setStatusTip('프린트')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar')        # 툴바타이틀은 없어도 됨
        toolbar.addAction(actSave)
        toolbar.addAction(actEdit)
        toolbar.addAction(actPrint)
        toolbar.addAction(actExit)

        # 상태바
        self.statusBar().showMessage('StatusBar message')

        self.setWindowIcon(QIcon('./d9/monitor.png'))

        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        self.setGeometry(900, 200, 400, 200)  # x, y, w, h
        # self.move
        self.show()         # 핵심


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())