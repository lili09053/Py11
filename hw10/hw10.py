import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow
import random
import string

fi = open("input.txt", "w", encoding="utf-8")
sti = ""
for _ in range(10):
    sti += str(random.randint(-50, 50))
    sti += "\n"
fi.write(sti)
fi.close()

fo = open("output.txt", "w", encoding="utf-8")
sto = ""
for _ in range(10):
    sto += random.choice(string.ascii_letters)
    sto += str(random.randint(-50, 50))
    sto += "\n"
fo.write(sto)
fo.close()

name = ""


class Statistics(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculation)

    def open_file(self):
        global name
        name = self.name_file_textEdit.toPlainText()
        try:
            file = open(name, "r", encoding="utf-8")
            return True
        except FileNotFoundError:
            self.label_result.setText(f"Файл {name} отсутствует")
            self.min_textEdit.setText("0")
            self.max_textEdit.setText("0")
            self.average_textEdit.setText("0,00")
            return False

    def has_error(self):
        global name
        file = open(name, "r", encoding="utf-8")
        try:
            for i in file:
                row = int(i)
            return False
        except ValueError:
            self.label_result.setText(f"Файл {name} содержит некорректные данные")
            self.min_textEdit.setText("0")
            self.max_textEdit.setText("0")
            self.average_textEdit.setText("0,00")
            return True

    def calculation(self):
        if self.open_file() and not self.has_error():
            self.average()
            self.max_value()
            self.min_value()

    def average(self):
        global name
        file = open(name, "r", encoding="utf-8")
        sum = 0
        count = 0
        for i in file:
            if i == "\n":
                i = 0
            count += 1
            sum += int(i)
        self.average_textEdit.setText(str(float(sum / count)))

    def max_value(self):
        global name
        file = open(name, "r", encoding="utf-8")
        self.max_textEdit.setText(str(max(file)))

    def min_value(self):
        global name
        file = open(name, "r", encoding="utf-8")
        self.min_textEdit.setText(str(min(file)))


def exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Statistics()
    wnd.show()
    sys.exit(app.exec())