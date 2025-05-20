import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets  import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.bt_is_checked=True

        self.setWindowTitle("主界面")
        bt = QPushButton("按我一下")
        bt.setCheckable(True)
        #发送事件
        bt.clicked.connect(self.bt_was_toggled)
        bt.setChecked(self.bt_is_checked)
        self.setFixedSize(QSize(300, 400))
        self.setCentralWidget(bt)

    def bt_was_toggled(self,is_checked):
        self.bt_is_checked = is_checked
        print("我被按下?",is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

