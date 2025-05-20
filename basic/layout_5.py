import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from layout_colorwifget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        #设置布局周围的间距
        layout1.setContentsMargins(5,0,0,5)
        #设置元素之间的间距
        layout1.setSpacing(10)

        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))

        layout1.addLayout(layout2)

        layout1.addWidget(Color("green"))

        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("yellow"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)

        container = QWidget()
        container.setLayout(layout1)

        self.setMinimumSize(QSize(100, 100))
        self.setMaximumSize(QSize(500, 630))
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
