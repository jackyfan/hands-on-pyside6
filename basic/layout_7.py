import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets  import QApplication,QMainWindow,QStackedLayout,QWidget
from layout_colorwifget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("yellow"))
        layout.addWidget(Color("green"))

        container = QWidget()
        container.setLayout(layout)

        self.setMinimumSize(QSize(100,100))
        self.setMaximumSize(QSize(500,630))
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

