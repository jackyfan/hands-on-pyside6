import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets  import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主界面")
        bt = QPushButton("按我一下")
        bt.setChecked(True)
        #发送事件
        bt.clicked.connect(self.bt_was_clicked)
        bt.clicked.connect(self.bt_was_toggled)
        self.setFixedSize(QSize(300, 400))
        self.setCentralWidget(bt)
    def bt_was_clicked(self):
        print("我被按下了!")

    def bt_was_toggled(self,checked):
        print("我被按下?",checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

