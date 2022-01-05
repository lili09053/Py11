import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from untitled import Ui_MainWindow


class DrawClass(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.update()  # перерисовка окна

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        count = 0
        length = 0
        coefficient = 0.0
        if self.repeat_count_text.toPlainText() != "":
            count = int(self.repeat_count_text.toPlainText())
        if self.side_text.toPlainText() != "":
            length = int(self.side_text.toPlainText())
        if self.coefficient_text.toPlainText() != "":
            coefficient = float(self.coefficient_text.toPlainText())

        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        size = 2

        for i in range(0, count):
            self.draw_square(qp, length)
            length = int(length * coefficient)


    def draw_square(self, qp, length):
        x = (580 - length) // 2
        y = (650 - length) // 2

        qp.drawLine(x, y, x + length, y)
        qp.drawLine(x, y, x, y + length)
        qp.drawLine(x + length, y + length, x, y + length)
        qp.drawLine(x + length, y + length, x + length, y)


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
