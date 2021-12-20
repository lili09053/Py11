import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow

name = ""


class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_pushButton.clicked.connect(self.open_file)
        self.save_pushButton.clicked.connect(self.save_file)
        self.create_pushButton.clicked.connect(self.create_file)

    def open_file(self):
        global name
        name = self.name_textEdit.toPlainText()
        file = open(name, "r", encoding="utf-8")
        self.show_textEdit.setText(file.read())
        file.close()

    def save_file(self):
        global name
        name = self.name_textEdit.toPlainText()
        f = open(name, "w", encoding="utf-8")
        st = self.show_textEdit.toPlainText()
        f.write(st)
        f.close()

    def create_file(self):
        self.show_textEdit.clear()


def exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Editor()
    wnd.show()
    sys.exit(app.exec())
