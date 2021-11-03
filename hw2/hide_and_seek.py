import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow

class Hide_and_Seek(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox_1.stateChanged.connect(self.check1_clicked)
        self.checkBox_2.stateChanged.connect(self.check2_clicked)
        self.checkBox_3.stateChanged.connect(self.check3_clicked)
        self.checkBox_4.stateChanged.connect(self.check4_clicked)

    def check1_clicked(self):
        if self.checkBox_1.isChecked():
            self.textBrowser_1.hide()
        else:
            self.textBrowser_1.show()
    
    def check2_clicked(self):
        if self.checkBox_2.isChecked():
            self.textBrowser_2.hide()
        else:
            self.textBrowser_2.show()

    def check3_clicked(self):
        if self.checkBox_3.isChecked():
            self.textBrowser_3.hide()
        else:
            self.textBrowser_3.show()

    def check4_clicked(self):
        if self.checkBox_4.isChecked():
            self.textBrowser_4.hide()
        else:
            self.textBrowser_4.show()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Hide_and_Seek()
    wnd.show()
    sys.exit(app.exec())
