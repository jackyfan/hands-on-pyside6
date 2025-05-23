import sys, time

from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QWidget,
)


class WorkKilledException(Exception):
    pass


class WorkSignals(QObject):
    progress = Signal(int)


class Worker(QRunnable):
    signals = WorkSignals()

    def __init__(self):
        super().__init__()
        self.is_killed = False

    @Slot()
    def run(self):
        try:
            for n in range(100):
                self.signals.progress.emit(n+1)
                time.sleep(0.1)

                if self.is_killed:
                    raise WorkKilledException
        except WorkKilledException:
            pass
    def kill(self):
        self.is_killed = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        container = QWidget()
        layout =QHBoxLayout()
        btn = QPushButton("停止")
        layout.addWidget(btn)
        container.setLayout(layout)
        self.setCentralWidget(container)
        #创建进度条
        self.status = self.statusBar()
        self.progress = QProgressBar()
        self.status.addPermanentWidget(self.progress)
        self.worker = Worker()
        self.worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(self.worker)

        btn.pressed.connect(self.worker.kill)

        self.show()
    def update_progress(self,n):
        self.progress.setValue(n)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
