import sys
import math
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from ui15 import Ui_Form


class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    @property
    def x(self):
        return self.X

    @x.setter
    def x(self, x):
        self.X = x

    @property
    def y(self):
        return self.Y

    @y.setter
    def y(self, y):
        self.Y = y


color = Qt.black


class DrawClass(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        global color
        color = QColorDialog().getColor()
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        count = 0
        coefficient = 0
        side_count = 1

        if self.repeat_count_text.toPlainText() != "":
            count = int(self.repeat_count_text.toPlainText())

        if self.coeff_text.toPlainText() != "":
            coefficient = 1 - float(self.coeff_text.toPlainText())

        if self.side_count_text.toPlainText() != "":
            side_count = int(self.side_count_text.toPlainText())

        length = 150

        pen = QPen(color, 2, Qt.SolidLine)
        qp.setPen(pen)

        point = []

        wight = 580 // 2
        height = 650 // 2
        alpha = 360 / side_count

        angle = 0
        while angle <= 360 + 1:
            x = int(wight + length * math.cos(math.radians(angle)))
            y = int(height + length * math.sin(math.radians(angle)))
            point.append(Point(x, y))
            angle += alpha

        for i in range(0, count):
            # Рисуем стороны N-угольника

            for j in range(0, len(point) - 1):
                qp.drawLine(point[j].x, point[j].y, point[j + 1].x, point[j + 1].y)

            for j in range(0, len(point) - 1):
                index = j + 1
                if point[j].x <= point[index].x:
                    point[j].x = int(point[j].x + abs(point[j].x - point[index].x) * coefficient)
                else:
                    point[j].x = int(point[j].x - abs(point[j].x - point[index].x) * coefficient)

                if point[j].y <= point[index].y:
                    point[j].y = int(point[j].y + abs(point[j].y - point[index].y) * coefficient)
                else:
                    point[j].y = int(point[j].y - abs(point[j].y - point[index].y) * coefficient)

            point[len(point) - 1].x = point[0].x
            point[len(point) - 1].y = point[0].y


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = DrawClass()
    wnd.show()
    sys.exit(app.exec())
