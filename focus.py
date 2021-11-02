import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow


class Focus(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_arrow.clicked.connect(self.button_clicked)

    def button_clicked(self):
        if self.pushButton_arrow.text() == "->":
            self.pushButton_arrow.setText("<-")
        else:
            self.pushButton_arrow.setText("->")
        
        temp = self.textEdit_left.toPlainText()
        self.textEdit_left.setText(self.textEdit_right.toPlainText())
        self.textEdit_right.setText(temp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Focus()
    wnd.show()
    sys.exit(app.exec())





