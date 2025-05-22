import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QHBoxLayout
from powerbar import PowerBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        powerbar = PowerBar(steps=6)
        layout.addWidget(powerbar)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
