import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow
import random


class Poem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.conclusion)

    def conclusion(self):
        lst = []
        with open('input.txt', encoding="utf-8") as file:
            for st in file:
                lst.append(st)
                random.choice(lst)
        self.textBrowser.setText(random.choice(lst))


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Poem()
    wnd.show()
    sys.exit(app.exec())
