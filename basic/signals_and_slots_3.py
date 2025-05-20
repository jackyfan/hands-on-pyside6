import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_title = [
    "1", "1",
    "2", "2",
    "3", "3",
    "99"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("主界面")
        self.bt = QPushButton("按我一下")
        self.bt.setCheckable(True)
        # 发送事件
        self.bt.clicked.connect(self.bt_was_checked)
        self.windowTitleChanged.connect(self.window_title_was_changed)
        self.setFixedSize(QSize(300, 400))
        self.setCentralWidget(self.bt)

    def bt_was_checked(self):
        self.bt.setText("我被按下了")
        new_window_title = choice(window_title)
        print("设置新窗体标题：%s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def window_title_was_changed(self, title):
        print("改变窗体标题：%s" % title)
        if title == "99":
            self.bt.setEnabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
