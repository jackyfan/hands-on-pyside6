import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QPushButton, QLabel, QToolBar, QStatusBar)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        self.setFixedSize(QSize(300, 400))

        label = QLabel("你好!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("工具栏")
        self.addToolBar(toolbar)

        print_btn = QAction("打印", self)
        print_btn.setToolTip("打印一下")
        print_btn.triggered.connect(self.print_checked)
        toolbar.addAction(print_btn)
        self.setStatusBar(QStatusBar(self))

    def print_checked(self, s):
        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
