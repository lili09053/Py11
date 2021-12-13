import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_mainWindow

file = open("6.txt", "w", encoding="utf-8")


class McDonalds(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.check_clicked)
        self.checkBox_2.stateChanged.connect(self.check_clicked)
        self.checkBox_3.stateChanged.connect(self.check_clicked)
        self.checkBox_4.stateChanged.connect(self.check_clicked)
        self.pushButton.clicked.connect(self.make_order)

    def make_order(self):
        self.plainTextEdit.setPlainText(open("6.txt", "r", encoding="utf-8").read())
        file.close()

    def check_clicked(self):
        file = open("6.txt", "w", encoding="utf-8")
        temp = "Ваш заказ:\n\n"
        if self.checkBox.isChecked():
            temp += self.checkBox.text() + "\n"
        if self.checkBox_2.isChecked():
            temp += self.checkBox_2.text() + "\n"
        if self.checkBox_3.isChecked():
            temp += self.checkBox_3.text() + "\n"
        if self.checkBox_4.isChecked():
            temp += self.checkBox_4.text() + "\n"
        file.write(temp)
        file.close()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = McDonalds()
    wnd.show()
    sys.exit(app.exec())
