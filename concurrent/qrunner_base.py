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
)


class WorkSignals(QObject):
    pass


class Worker(QRunnable):
    def __init__(self, *args,**kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkSignals()
    @Slot()
    def run(self):
        pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
