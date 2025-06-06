import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets  import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        bt = QPushButton("按我一下")
        bt.setCheckable(True)
        #发送事件
        bt.clicked.connect(self.bt_was_clicked)
        self.setFixedSize(QSize(300, 400))
        self.setCentralWidget(bt)

    #函数、方法都可以作为插槽
    def bt_was_clicked(self):
        print("我被按下了")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

