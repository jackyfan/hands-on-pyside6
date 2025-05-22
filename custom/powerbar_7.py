import sys
from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui, QtWidgets


class _Bar(QtWidgets.QWidget):
    def __init__(self, steps):
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                           QtWidgets.QSizePolicy.MinimumExpanding)
        if isinstance(steps, int):
            self.n_steps = steps
            self.steps = ["red"] * steps
        elif isinstance(steps, list):
            self.n_steps = len(steps)
            self.steps = steps
        else:
            raise TypeError("steps参数类型不对，必须是整数或列表")

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor("black")
        self._padding = 4

    def sizeHint(self):
        return QtCore.QSize(40, 120)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * self.n_steps)

        for n in range(n_steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            ypos = (1 + n) * step_size
            rect = QtCore.QRect(
                self._padding,
                self._padding + d_height - int(ypos),
                d_width,
                int(bar_height),
            )
            painter.fillRect(rect, brush)
        painter.end()

    def _trigger_refresh(self):
        self.update()


class PowerBar(QtWidgets.QWidget):
    def __init__(self, parent=None, steps=5):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar(steps)
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)
volume = PowerBar(
    steps=[
        "#5e4fa2",
        "#3288bd",
        "#66c2a5",
        "#abdda4",
        "#e6f598",
        "#ffffbf",
        "#fee08b",
        "#fdae61",
        "#f46d43",
        "#d53e4f",
        "#9e0142",
    ]
)

volume.show()
app.exec()
