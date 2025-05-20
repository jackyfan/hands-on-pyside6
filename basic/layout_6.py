import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets  import QApplication,QMainWindow,QGridLayout,QWidget
from layout_colorwifget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        layout = QGridLayout()

        layout.addWidget(Color("red"),0,0)
        layout.addWidget(Color("yellow"),1,0)
        layout.addWidget(Color("green"),1,1)
        layout.addWidget(Color("blue"),2,1)
        layout.addWidget(Color("red"), 2, 2)
        layout.addWidget(Color("yellow"), 3, 2)

        container = QWidget()
        container.setLayout(layout)

        self.setMinimumSize(QSize(100,100))
        self.setMaximumSize(QSize(500,630))
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

