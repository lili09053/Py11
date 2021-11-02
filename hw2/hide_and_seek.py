import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow

class Hide_and_Seek(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox_1.stateChanged.connect(self.check1_clicked)

    def check1_clicked(self):
        if self.checkBox_1.isChecked():
            self.textBrowser_1.hide()
        else:
            self.textBrowser_1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Hide_and_Seek()
    wnd.show()
    sys.exit(app.exec())
