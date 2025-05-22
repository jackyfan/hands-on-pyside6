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
    QProgressBar,
    QVBoxLayout,
    QPushButton,
    QWidget
)


class WorkSignals(QObject):
    progress = Signal(int)


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkSignals()

    @Slot()
    def run(self):
        total = 1000
        for n in range(total):
            progress_pc = int(100 * float(n + 1) / total)
            self.signals.progress.emit(progress_pc)
            time.sleep(0.1)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.progress = QProgressBar()
        btn = QPushButton("马牛跑起来")
        btn.clicked.connect(self.execute)

        layout.addWidget(self.progress)
        layout.addWidget(btn)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(worker)
    def update_progress(self,progress):
        self.progress.setValue(progress)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
