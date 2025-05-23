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
        self.is_paused = False

    @Slot()
    def run(self):
        try:
            for n in range(100):
                self.signals.progress.emit(n+1)
                time.sleep(0.1)

                #进入循环，不会退出
                while self.is_paused:
                    time.sleep(0)

                if self.is_killed:
                    raise WorkKilledException

        except WorkKilledException:
            pass
    def kill(self):
        self.is_killed = True
    def pause(self):
        self.is_paused = True
    def resume(self):
        self.is_paused = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        container = QWidget()
        layout =QHBoxLayout()
        btn_stop = QPushButton("停止")
        btn_pause = QPushButton("暂停")
        btn_resume = QPushButton("恢复")

        layout.addWidget(btn_stop)
        layout.addWidget(btn_pause)
        layout.addWidget(btn_resume)
        container.setLayout(layout)

        self.setCentralWidget(container)
        #创建进度条
        self.status = self.statusBar()
        self.progress = QProgressBar()
        self.status.addPermanentWidget(self.progress)
        self.worker = Worker()
        self.worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(self.worker)

        btn_stop.pressed.connect(self.worker.kill)
        btn_pause.pressed.connect(self.worker.pause)
        btn_resume.pressed.connect(self.worker.resume)

        self.show()
    def update_progress(self,n):
        self.progress.setValue(n)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
