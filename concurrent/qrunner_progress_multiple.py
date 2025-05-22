import sys, time, random, uuid

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


class WorkSignals(QObject):
    progress = Signal(str, int)
    finished = Signal(str)


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.job_id = uuid.uuid4().hex
        self.signals = WorkSignals()

    @Slot()
    def run(self):
        total = 1000
        delay = random.random() / 100
        for n in range(total):
            progress_pc = int(100 * float(n + 1) / total)
            self.signals.progress.emit(self.job_id, progress_pc)
            time.sleep(delay)
        self.signals.finished.emit(self.job_id)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.progress = QProgressBar()
        btn = QPushButton("一群马牛跑起来")
        self.status = QLabel("0只牛马")
        btn.clicked.connect(self.execute)

        layout.addWidget(self.progress)
        layout.addWidget(btn)
        layout.addWidget(self.status)
        container = QWidget()
        container.setLayout(layout)
        # 保存任务进度
        self.worker_progress = {}

        self.setCentralWidget(container)
        self.show()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.refresh_progress)
        self.timer.start()

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        worker.signals.finished.connect(self.cleanup)
        self.threadpool.start(worker)

    def update_progress(self, job_id, progress):
        self.worker_progress[job_id] = progress

    def cleanup(self, job_id):
        if job_id in self.worker_progress:
            del self.worker_progress[job_id]
            self.refresh_progress()

    def calculate_progress(self):
        if not self.worker_progress:
            return 0
        return sum(v for v in self.worker_progress.values()) / len(self.worker_progress)

    def refresh_progress(self):
        # Calculate total progress.
        progress = self.calculate_progress()
        print(self.worker_progress)
        self.progress.setValue(progress)
        self.status.setText("%d只牛马" % len(self.worker_progress))


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
