import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets  import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        bt = QPushButton("按我一下")
        self.setFixedSize(QSize(300, 400))
        self.setCentralWidget(bt)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

