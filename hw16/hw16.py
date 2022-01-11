import sys, csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore
from ui16 import Ui_MainWindow

schools = []  # Список участвующих школ
classes = []  # Список участвующих классов
is_empty = True  # Указывает, пуст ли выбор класса

class TableClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.school_number.addItem("Все")
        self.class_number.addItem("Все")
        self.get_combo_boxes()
        self.school_number.currentTextChanged.connect(self.is_school_selected)
        self.result_button.clicked.connect(self.get_result)

    def get_combo_boxes(self):  # Получение списков всех участвующих школ и классов
        global schools, classes
        with open("rez.csv", encoding='utf-8') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=",")  # Работаем с файлом как со словарём
            for row in file_reader:  # Считывание данных из CSV файла
                school = row["login"].split("-")[2]  # Из логина получаем номер школы
                clss = row["login"].split("-")[3]  # Из логина получаем номер класса
                if school not in schools:  # Если найденной школы ещё не оказалось в списке
                    schools.append(school)  # Добавляем в список
                if clss not in classes:  # Если найденного класса ещё не оказалось в списке
                    classes.append(clss)  # Добавляем в список
            classes.sort()  # Сортируем список классов
        for elem in schools:  # Добавляем в выбор школ все доступные школы
            self.school_number.addItem(elem)  # Добавляем школу

    def is_school_selected(self):  # Для получения доступа выбора класса определённой школы
        # Если выбрана определённая школа и пуст выбор школы
        global is_empty
        if self.school_number.currentText() != "Все" and is_empty:
            is_empty = False
            for elem in classes:  # Добавляем в выбор класса все доступные классы
                self.class_number.addItem(elem)  # Добавляем класс
        if self.school_number.currentText() == "Все":
            is_empty = True
            self.class_number.clear()  # Очищаем выбор определённого класса
            self.class_number.addItem("Все")  # Добавляем в выборы класса все

    def setup_columns(self):  # Создаём столбцы для таблицы
        self.table.setColumnCount(2)  # Задаём кол-во столбцов в таблице
        widget_item = QTableWidgetItem()  # Столбец таблицы 1
        widget_item.setText("Фамилия")  # Столбец таблицы. Заносим название столбца
        self.table.setHorizontalHeaderItem(0, widget_item)  # Помещаем столбец в таблицу
        widget_item = QTableWidgetItem()  # Столбец таблицы 2
        widget_item.setText("Результат")  # Столбец таблицы 2. Заносим название столбца
        self.table.setHorizontalHeaderItem(1, widget_item)  # Помещаем столбец в таблицу

    def setup_rows(self):  # Создаём строки для таблицы
        self.table.setRowCount(self.count_rows())  # Задаём кол-во строк в таблице
        for i in range(0, self.table.rowCount()):
            item = QTableWidgetItem()  # Строка таблицы i
            item.setText(str(i + 1))  # Подписываем каждую строку порядковым номером
            self.table.setVerticalHeaderItem(i, item)

    def get_result(self):  # Заносим элементы в таблицу
        self.table.clear()
        self.table.setRowCount(0)
        self.setup_columns()  # Заполняем столбцы
        # self.setup_rows()  # Заполняем строки
        self.get_table()  # Заполняем таблицу

    def get_table(self):  # Заполнение таблицы
        with open("rez.csv", encoding='utf-8') as r_file:
            row_count = 0  # Для заполнения таблицы
            file_reader = csv.DictReader(r_file, delimiter=",")  # Работаем с файлом как со словарём
            for row in file_reader:  # Считывание данных из CSV файла
                if self.is_counted(row):
                    self.table.setRowCount(row_count + 1)
                    self.set_elem(self.table.horizontalHeaderItem(0).text(), row, row_count)
                    self.set_elem(self.table.horizontalHeaderItem(1).text(), row, row_count)
                    row_count += 1  # Переход на следующую строку таблицы

    def set_elem(self, column, row, row_count):  # Заполнение элемента таблицы
        if column == self.table.horizontalHeaderItem(0).text():
            if self.school_number.currentText() != "Все":
                item = QTableWidgetItem()  # Элемент таблицы
                school = row["login"].split("-")[2]  # Из логина получаем номер школы
                if self.class_number.currentText() != "Все":
                    clss = row["login"].split("-")[3]  # Из логина получаем номер класса
                    if school == self.school_number.currentText() and clss == self.class_number.currentText():
                        item.setText(row["user_name"].split(" ")[3])  # Записываем в элемент фамилию
                else:
                    if school == self.school_number.currentText():
                        item.setText(row["user_name"].split(" ")[3])  # Записываем в элемент фамилию
                self.table.setItem(row_count, 0, item)  # Заносим элемент в таблицу
            else:
                item = QTableWidgetItem()  # Элемент таблицы
                item.setText(row["user_name"].split(" ")[3])  # Записываем в элемент фамилию
                self.table.setItem(row_count, 0, item)  # Заносим элемент в таблицу
        else:
            if self.school_number.currentText() != "Все":
                item = QTableWidgetItem()  # Элемент таблицы
                school = row["login"].split("-")[2]  # Из логина получаем номер школы
                if self.class_number.currentText() != "Все":
                    clss = row["login"].split("-")[3]  # Из логина получаем номер класса
                    if school == self.school_number.currentText() and clss == self.class_number.currentText():
                        item.setText(row["Score"])  # Записываем в элемент общий балл [1:len(row["Score"]) - 1]
                else:
                    if school == self.school_number.currentText():
                        item.setText(row["Score"])  # Записываем в элемент общий балл [1:len(row["Score"]) - 1]
                self.table.setItem(row_count, 1, item)  # Заносим элемент в таблицу
            else:
                item = QTableWidgetItem()  # Элемент таблицы
                item.setText(row["Score"])  # Записываем в элемент общий балл [1:len(row["Score"]) - 1]
                self.table.setItem(row_count, 1, item)  # Заносим элемент в таблицу

    def is_counted(self, row):  # Проверка необходимости подсчёта  строки
        if row != "":
            if self.school_number.currentText() != "Все":
                school = row["login"].split("-")[2]  # Из логина получаем номер школы
                if self.class_number.currentText() != "Все":
                    clss = row["login"].split("-")[3]  # Из логина получаем номер класса
                    if school == self.school_number.currentText() and clss == self.class_number.currentText():
                        return True
                else:
                    if school == self.school_number.currentText():
                        return True
            else:
                return True
        return False


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = TableClass()
    wnd.show()
    sys.exit(app.exec())