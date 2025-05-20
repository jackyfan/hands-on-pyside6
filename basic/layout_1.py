import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets  import QApplication,QMainWindow,QPushButton
from layout_colorwifget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        color = Color("red")

        self.setMinimumSize(QSize(100,100))
        self.setMaximumSize(QSize(500,720))
        self.setCentralWidget(color)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

