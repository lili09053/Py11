import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt5 import QtCore

morse_alphabet_dict = {'A': '.-',
                       'B': '-...',
                       'C': '-.-.',
                       'D': '-..',
                       'E': '.',
                       'F': '..-.',
                       'G': '--.',
                       'H': '....',
                       'I': '..',
                       'J': '.---',
                       'K': '-.-',
                       'L': '.-..',
                       'M': '--',
                       'N': '-.',
                       'O': '---',
                       'P': '.--.',
                       'Q': '--.-',
                       'R': '.-.',
                       'S': '...',
                       'T': '-',
                       'U': '..-',
                       'V': '...-',
                       'W': '.--',
                       'X': '-..-',
                       'Y': '-.--',
                       'Z': '--..', }


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 530, 100)         # расположение и размер окна
        self.setWindowTitle('Азбука Морзе 2')        # имя окна
        self.setMinimumSize(QtCore.QSize(530, 100))  # максимальный размер окна
        self.setMaximumSize(QtCore.QSize(530, 100))  # минимальный размер окна

        self.output = QLineEdit(self)                # создание объекта класса QLineEdit
        self.output.move(10, 30)                     # настраиваем расположение поля вывода
        self.output.resize(510, 30)                  # настраиваем размер поля вывода
        self.output.setEnabled(False)                # делаем поле вывода неизменяемым объектом

        b = 5

        for k, v in morse_alphabet_dict.items():     # создаём кнопки с помощью цикла
            self.button = QPushButton(self)          # создание объекта класса QPushButton
            self.button.setText(k)                   # даём "имя" кнопки
            self.button.resize(20, 20)               # настраиваем размер кнопки
            self.button.move(b, 0)                   # настраиваем расположение кнопки
            b = b + 20                               # изменяем значение, для следующих кнопок
            self.button.clicked.connect(self.print_code)    # соединяем сигнал с методом

    def print_code(self):
        s = morse_alphabet_dict[self.sender().text()]       # обращаемся к элементу словаря по ключу и
                                                            # достаём его значение
        self.output.setText(f"{self.output.text()} {s}")    # закладываем измененный тескт


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Ui_MainWindow()
    wnd.show()
    sys.exit(app.exec())


