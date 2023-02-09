# 화면 중심 셋팅 (추가)
# QtCore - 날짜 (추가)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime


class MyApp(QMainWindow):

    def __init__(self):
      super().__init__()
      self.initUI()

    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./d9/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+W')       # 단축키 지정
        actExit.setStatusTip('앱종료')
        actExit.triggered.connect(qApp.quit)


        actSave = QAction(QIcon('./d9/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        actEdit = QAction(QIcon('./d9/edit.png'), 'Edit', self)
        actEdit.setShortcut('Ctrl+E')
        actEdit.setStatusTip('수정')

        actPrint = QAction(QIcon('./d9/print.png'), 'Print', self)
        actPrint.setShortcut('Ctrl+P')
        actPrint.setStatusTip('프린트')

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
        now = QDate.currentDate()       # 현재 일자 받아옴
        time = QTime.currentTime()      # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd-dddd') + ' ' + time.toString('hh:mm:ss'))

        self.setWindowIcon(QIcon('./d9/monitor.png'))

        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        #self.setGeometry(900, 200, 400, 200)  # x, y, w, h
        # self.move(1440 // 2 - 200, 900 // 2 - 100)     # 정중앙에 위치잡기
        self.move(50, 50)
        self.resize(400,200)
        self.setCenter()
        self.show()         # 핵심!!

    # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry()       # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()  # 모니터화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())