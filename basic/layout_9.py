import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets  import (QApplication,QMainWindow,
                                QStackedLayout,QTabWidget,
                                QWidget)
from layout_colorwifget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        tabs = QTabWidget()
        #选项位置
        tabs.setTabPosition(QTabWidget.West)
        #文档模式，macOS有效果
        #tabs.setDocumentMode(True)
        #选项可以移动
        tabs.setMovable(True)

        for _,color in enumerate(["red","green","blue"]) :
            tabs.addTab(Color(color),color)

        self.setMinimumSize(QSize(100,100))
        self.setMaximumSize(QSize(500,630))
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

