import sys
from PySide6.QtCore import Qt
from PySide6 import QtCore,QtGui, QtWidgets


class _Bar(QtWidgets.QWidget):
    def paintEvent(self, ev):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0,0,painter.device().width(), painter.device().height())
        painter.fillRect(rect,brush)


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
