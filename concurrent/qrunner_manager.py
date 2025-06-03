from PySide6.QtCore import (QAbstractListModel, Signal, QThreadPool, QTimer)


class WorkerManager(QAbstractListModel):
    _workers = {}
    _state = {}
    status = Signal(str)

    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.max_threads = self.threadpool.maxThreadCount()
        print("Multithreading with maximum %d threads" % self.max_threads)

        self.status_timer = QTimer()
        self.status_timer.setInterval(100)
        self.status_timer.timeout.connect(self.notify_status)
        self.status_timer.start()

    def notify_status(self):
        n_workers = len(self._workers)
        running = min(n_workers, self.max_threads)
        waiting = max(0, n_workers - self.max_threads)
        self.status.emit("{} running,{} waiting,{} threads".format(running, waiting, self.max_threads))
