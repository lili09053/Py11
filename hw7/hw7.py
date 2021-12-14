import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow



class McDonalds(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit_1.setDisabled(True)
        self.textEdit_2.setDisabled(True)
        self.textEdit_3.setDisabled(True)
        self.textEdit_4.setDisabled(True)
        self.checkBox_1.stateChanged.connect(self.check1_clicked)
        self.checkBox_2.stateChanged.connect(self.check2_clicked)
        self.checkBox_3.stateChanged.connect(self.check3_clicked)
        self.checkBox_4.stateChanged.connect(self.check4_clicked)
        self.pushButton.clicked.connect(self.make_order)

    def make_order(self):
        temp = "Ваш заказ:\n\n"

        if self.checkBox_1.isChecked():
            temp += self.checkBox_1.text() + "....." + self.textEdit_1.toPlainText() + ".....10\n"
        if self.checkBox_2.isChecked():
            temp += self.checkBox_2.text() + "....." + self.textEdit_2.toPlainText() + ".....240\n"
        if self.checkBox_3.isChecked():
            temp += self.checkBox_3.text() + "....." + self.textEdit_3.toPlainText() + ".....300\n"
        if self.checkBox_4.isChecked():
            temp += self.checkBox_4.text() + "....." + self.textEdit_4.toPlainText() + ".....420\n"
        temp += "\nИтого: " + str(int(self.textEdit_1.toPlainText()) * 10 + int(self.textEdit_2.toPlainText()) * 240 + int(self.textEdit_3.toPlainText()) * 300 + int(self.textEdit_4.toPlainText()) * 420)
        self.plainTextEdit.setPlainText(temp) # open("7.txt", "r", encoding="utf-8").read()
        file.close()

    def check1_clicked(self):
        if self.checkBox_1.isChecked():
            self.textEdit_1.setText("1")
            self.textEdit_1.setDisabled(False)
        else:
            self.textEdit_1.setText("0")
            self.textEdit_1.setDisabled(True)

    def check2_clicked(self):
        if self.checkBox_2.isChecked():
            self.textEdit_2.setText("1")
            self.textEdit_2.setDisabled(False)
        else:
            self.textEdit_2.setText("0")
            self.textEdit_2.setDisabled(True)

    def check3_clicked(self):
        if self.checkBox_3.isChecked():
            self.textEdit_3.setText("1")
            self.textEdit_3.setDisabled(False)
        else:
            self.textEdit_3.setText("0")
            self.textEdit_3.setDisabled(True)

    def check4_clicked(self):
        if self.checkBox_4.isChecked():
            self.textEdit_4.setText("1")
            self.textEdit_4.setDisabled(False)
        else:
            self.textEdit_4.setText("0")
            self.textEdit_4.setDisabled(True)


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
