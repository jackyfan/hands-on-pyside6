import sys, time, random

from PySide6.QtCore import (
    QTimer,
    QRunnable,
    QThreadPool,
    QObject,
    Signal, Slot)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WorkSignals(QObject):
    finished = Signal()
    error = Signal(str)
    result = Signal(dict)


class Worker(QRunnable):
    def __init__(self, iterations=5):
        super().__init__()
        self.signals = WorkSignals()
        self.iterations = iterations
    @Slot()
    def run(self):
        try:
            for n in range(self.iterations):
                time.sleep(0.01)
                v = 5 / (40 - n)
        except Exception as e:
            self.signals.error.emit(str(e))
        else:
            self.signals.finished.emit()
            self.signals.result.emit({"n": n, "v": v})


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        layout = QVBoxLayout()
        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.do_bad)

        layout.addWidget(self.l)
        layout.addWidget(b)
        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def do_bad(self):
        worker = Worker(iterations=random.randint(10, 50))
        #注册插槽
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

    def worker_output(self, s):
        print("RESULT", s)

    def worker_complete(self):
        print("THREAD COMPLETE!")

    def worker_error(self, t):
        print("ERROR: %s" % t)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
