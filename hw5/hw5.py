import sys
from PyQt5 import QtCore, QtWidgets

count = 0
field = []
player = ""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 350)
        MainWindow.setMinimumSize(QtCore.QSize(300, 350))
        MainWindow.setMaximumSize(QtCore.QSize(300, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow = MainWindow

        global field
        global count
        count = 9
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                self.fields = QtWidgets.QPushButton(self.centralwidget)
                self.fields.setGeometry(QtCore.QRect(50 + j * 70, 60 + i * 70, 60, 60))
                self.fields.setText("")
                self.fields.clicked.connect(self.make_attempt)
                row.append(self.fields)
            field.append(row)

        self.new_game = QtWidgets.QPushButton(self.centralwidget)
        self.new_game.setGeometry(QtCore.QRect(100, 310, 101, 31))
        self.new_game.setObjectName("new_game")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 10, 101, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.x_button = QtWidgets.QRadioButton(self.layoutWidget)
        self.x_button.setObjectName("x_button")
        self.horizontalLayout.addWidget(self.x_button)
        self.o_button = QtWidgets.QRadioButton(self.layoutWidget)
        self.o_button.setObjectName("o_button")
        self.horizontalLayout.addWidget(self.o_button)
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(50, 270, 201, 31))
        self.info_label.setText("")
        self.info_label.setObjectName("info_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.new_game.clicked.connect(self.clear_field)
        self.x_button.clicked.connect(self.change_priority)
        self.o_button.clicked.connect(self.change_priority)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Крестики-нолики"))
        self.new_game.setText(_translate("MainWindow", "Новая игра"))
        self.x_button.setText(_translate("MainWindow", "X"))
        self.o_button.setText(_translate("MainWindow", "O"))

    def off_field(self):
        for i in range(0, 3):
            for j in range(0, 3):
                field[i][j].setEnabled(False)

    def clear_field(self):
        global count
        count = 9
        global player
        if self.x_button.isChecked():
            self.o_button.setChecked(False)
            player = self.x_button.text()
        if self.o_button.isChecked():
            self.x_button.setChecked(False)
            player = self.o_button.text()
        for i in range(0, 3):
            for j in range(0, 3):
                field[i][j].setEnabled(True)
                field[i][j].setText("")
        self.info_label.setText("")

    def make_attempt(self):
        global count
        global player
        if player != "" and self.MainWindow.sender().text() == "":
            count -= 1
            self.MainWindow.sender().setText(player)
            if player == "X":
                player = "O"
            else:
                player = "X"
        if count == 0:
            self.off_field()
            self.info_label.setText("Ничья!")
        if self.is_player_win() or self.is_diagonal():
            self.off_field()

    def is_player_win(self):
        for temp in range(0, 3):
            if (field[temp][0].text() == field[temp][1].text() == field[temp][2].text() == "X") or (
                    field[0][temp].text() == field[1][temp].text() == field[2][temp].text() == "X"):
                self.info_label.setText("Победитель - X!")
                return True
            if (field[temp][0].text() == field[temp][1].text() == field[temp][2].text() == "O") or (
                    field[0][temp].text() == field[1][temp].text() == field[2][temp].text() == "O"):
                self.info_label.setText("Победитель - O!")
                return True
        return False

    def is_diagonal(self):
        if (field[0][0].text() == field[1][1].text() == field[2][2].text() == "X") or (
                field[2][0].text() == field[1][1].text() == field[0][2].text() == "X"):
            self.info_label.setText("Победитель - X!")
            return True
        if (field[0][0].text() == field[1][1].text() == field[2][2].text() == "O") or (
                field[2][0].text() == field[1][1].text() == field[0][2].text() == "O"):
            self.info_label.setText("Победитель - O!")
            return True
        return False

    def change_priority(self):
        global player
        if self.x_button.isChecked():
            self.o_button.setChecked(False)
            player = self.x_button.text()
        if self.o_button.isChecked():
            self.x_button.setChecked(False)
            player = self.o_button.text()
        self.clear_field()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
