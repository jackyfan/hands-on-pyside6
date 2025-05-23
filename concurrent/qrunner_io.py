import sys

import requests
from PySide6.QtCore import QObject, QRunnable, QThreadPool, QTimer, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WorkSignals(QObject):
    data = Signal(tuple)


class Worker(QRunnable):
    def __init__(self, id, url):
        super().__init__()
        self.signals = WorkSignals()
        self.id = id
        self.url = url

    @Slot()
    def run(self):
        print("第%d牛马开始干活"%self.id)
        response = requests.get(self.url)
        for line in response.text.splitlines():
            self.signals.data.emit((self.id, line))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.urls = [
            "https://www.baidu.com/",
            "https://www.163.com/",
            "https://www.reddit.com/"]

        layout = QVBoxLayout()
        container = QWidget()

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        button = QPushButton("牛马开干了")
        button.pressed.connect(self.execute)
        layout.addWidget(self.text)
        layout.addWidget(button)

        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

    def execute(self):
        for n, url in enumerate(self.urls):
            worker = Worker(n, url)
            worker.signals.data.connect(self.display)
            self.threadpool.start(worker)

    def display(self, data):
        worker_id, s = data
        self.text.appendPlainText("Worker %d:%s" % (worker_id, s))


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
