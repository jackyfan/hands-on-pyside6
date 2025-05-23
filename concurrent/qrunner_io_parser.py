import sys, re

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
    def __init__(self, id, url, parsers):
        super().__init__()
        self.signals = WorkSignals()
        self.id = id
        self.url = url
        self.parsers = parsers

    @Slot()
    def run(self):
        print("第%d牛马开始干活" % self.id)
        response = requests.get(self.url)
        data = {}
        for name, parser in self.parsers.items():
            m = parser.search(response.text)
            if m:
                data[name] = m.group(1).strip()
        self.signals.data.emit((self.id, data))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.urls = [
            "https://www.baidu.com/",
            "https://www.google.com/",
            "https://www.reddit.com/"]
        self.parsers = {
            "title": re.compile(r"<title.*?>(.*?)<\/title>", re.M | re.S),
            "h1": re.compile(r"<h1.*?>(.*?)<\/h1>", re.M | re.S),
            "h2": re.compile(r"<h2.*?>(.*?)<\/h2>", re.M | re.S),
        }

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
            worker = Worker(n, url, self.parsers)
            worker.signals.data.connect(self.display)
            self.threadpool.start(worker)

    def display(self, data):
        worker_id, s = data
        self.text.appendPlainText("Worker %d:%s" % (worker_id, s))


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
