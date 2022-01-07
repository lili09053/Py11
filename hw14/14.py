import sys, random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from ui14 import Ui_Form


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


class DrawClass(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        count = 0
        coefficient = 0
        if self.repeat_count_text.toPlainText() != "":
            count = int(self.repeat_count_text.toPlainText())
        length = 300
        if self.coeff_text.toPlainText() != "":
            coefficient = 1 - float(self.coeff_text.toPlainText())

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)

        x = (580 - length) // 2
        y = (650 - length) // 2

        point = []

        point.append(Point(x, y))
        point.append(Point(x + length, y))
        point.append(Point(x + length, y + length))
        point.append(Point(x, y + length))
        point.append(Point(x, y))

        for i in range(0, count):
            # Рисуем стороны квадрата

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
