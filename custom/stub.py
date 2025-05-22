import sys
from PySide6.QtCore import Qt
from PySide6 import QtCore, QtWidgets


class _Bar(QtWidgets.QWidget):
    pass


class PowerBar(QtWidgets.QWidget):
    def __init__(self, parent=None, step=5):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        dial = QtWidgets.QDial()
        layout.addWidget(dial)

        self.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)
volume = PowerBar()
volume.show()
app.exec_()
