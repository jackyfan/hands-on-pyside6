import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QStackedLayout, QVBoxLayout,
                               QHBoxLayout, QWidget,
                               QPushButton)
from layout_colorwifget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        btn_layout = QHBoxLayout()
        page_layout = QVBoxLayout()
        self.stackLayout = QStackedLayout()
        page_layout.addLayout(btn_layout)
        page_layout.addLayout(self.stackLayout)

        btn1 = QPushButton("red")
        btn1.pressed.connect(self.activate_tab_1)
        btn_layout.addWidget(btn1)
        self.stackLayout.addWidget(Color("red"))

        btn2 = QPushButton("green")
        btn2.pressed.connect(self.activate_tab_2)
        btn_layout.addWidget(btn2)
        self.stackLayout.addWidget(Color("green"))

        btn3 = QPushButton("blue")
        btn3.pressed.connect(self.activate_tab_3)
        btn_layout.addWidget(btn3)
        self.stackLayout.addWidget(Color("blue"))

        container = QWidget()
        container.setLayout(page_layout)

        self.setMinimumSize(QSize(100, 100))
        self.setMaximumSize(QSize(500, 630))
        self.setCentralWidget(container)

    def activate_tab_1(self):
        self.stackLayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stackLayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stackLayout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
