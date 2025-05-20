import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets  import (QApplication,QMainWindow,
                                QPushButton,QLabel,QToolBar)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        self.setFixedSize(QSize(300, 400))

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("工具栏")
        self.addToolBar(toolbar)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

