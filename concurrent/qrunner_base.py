import sys, time, random

from PySide6.QtCore import (
    QTimer,
    QRunnable,
    QThreadPool,
    QObject,
    Signal, Slot)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout
)


class WorkSignals(QObject):
    pass


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkSignals()

    @Slot()
    def run(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
