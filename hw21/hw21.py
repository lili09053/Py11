import sys, csv, sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore
from ui21 import Ui_MainWindow

conn = sqlite3.connect("music_db.sqlite")
cursor = conn.cursor()

class TableClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_result)

    def setup_columns(self):  # Создаём столбцы для таблицы
        self.tableWidget.setColumnCount(1)  # Задаём кол-во столбцов в таблице
        widget_item = QTableWidgetItem()  # Столбец таблицы
        widget_item.setText("Album Title")  # Столбец таблицы. Заносим название столбца
        self.tableWidget.setHorizontalHeaderItem(0, widget_item)  # Помещаем столбец в таблицу

    def get_result(self):  # Заносим элементы в таблицу
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.setup_columns()  # Заполняем столбцы
        self.get_table()  # Заполняем таблицу

    def get_table(self):  # Заполнение таблицы
        i = 0
        genre = "\'" + self.textEdit.toPlainText() + "\'"
        for row in cursor.execute(
                """SELECT DISTINCT Title FROM Album
                   WHERE AlbumId IN(
                        SELECT AlbumId FROM Track
                        WHERE GenreId =(
                            SELECT GenreId FROM Genre
                            WHERE Name =""" + genre + """))
                        ORDER BY ArtistId, Title"""):
            i += 1
            self.tableWidget.setRowCount(i)
            widget_item = QTableWidgetItem()  # Столбец таблицы
            widget_item.setText(row[0])  # Столбец таблицы. Заносим название столбца
            self.tableWidget.setVerticalHeaderItem(i - 1, widget_item)  # Помещаем столбец в таблицу


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