import sys, time, random, traceback

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
    QWidget,
    QLabel
)


def do_something():
    print("我是牛马，我在干活")
    time.sleep(1)
    return "敲了一百行代码"


class WorkSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkSignals()

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.status = QLabel("还没有牛马干活")
        btn = QPushButton("一群马牛跑起来")

        btn.clicked.connect(self.execute)

        layout.addWidget(btn)
        layout.addWidget(self.status)
        container = QWidget()
        container.setLayout(layout)

        self.counter = 0
        self.setCentralWidget(container)
        self.show()
        self.setWindowTitle("牛马干活框架")
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.count)
        self.timer.start()

    def execute(self):
        worker = Worker(do_something)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.finished)
        self.threadpool.start(worker)

    def count(self):
        self.counter += 1
        self.status.setText("另外%d只牛马在干活" % self.counter)

    def finished(self):
        print("干完活了，接着干下一个。")

    def print_output(self, result):
        print("牛马在干活，结果：%s" % result)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
