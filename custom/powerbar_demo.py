import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QHBoxLayout
from powerbar import PowerBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        powerbar = PowerBar(steps=["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
        powerbar.setBarPadding(2)
        powerbar.setBarSolidPercent(0.9)
        powerbar.setBackgroundColor('gray')
        powerbar.setNotchesVisible(True)
        layout.addWidget(powerbar)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
