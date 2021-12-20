import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow

file = open("input.txt", "r", encoding="utf-8")


class Poem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.download)

    def download(self):
        a = 1
        st1 = ""
        st2 = ""
        for i in file:
            if a % 2 == 0:
                st2 += i + "\n"
            else:
                st1 += i + "\n"
            a += 1
        self.textEdit.setText(st1 + st2)


def exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Poem()
    wnd.show()
    sys.exit(app.exec())
