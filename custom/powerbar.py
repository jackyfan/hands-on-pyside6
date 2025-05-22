import sys
from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui, QtWidgets


class _Bar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                           QtWidgets.QSizePolicy.MinimumExpanding)

    def sizeHint(self):
        return QtCore.QSize(40, 120)

    def paintEvent(self, ev):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QtGui.QColor("red"))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily("Times")
        font.setPointSize(10)
        painter.setFont(font)

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)
        painter.drawText(25, 25, "{}".format(n_steps_to_draw))
        painter.end()

    def _trigger_refresh(self):
        self.update()


class PowerBar(QtWidgets.QWidget):
    def __init__(self, parent=None, step=5):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)
volume = PowerBar()
volume.show()
app.exec()
