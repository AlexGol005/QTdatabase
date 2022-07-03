import os
import PySide2
from PySide2.QtWidgets import QTableWidgetItem
from PySide2 import QtWidgets

import sqlite3
from design import Ui_MainWindow

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

#
# class SQLiteTools():
#     def __init__(self):
#         pass
#
#     def createConnection(self, sqlite3):
#         '' 'Создать соединение с базой данных' ''
#         # Создать базу данных, открыть, если она существует, в противном случае создать базу данных
#         self.con = sqlite3.connect(sqlite3)
#         # Создать объект курсора
#         self.cur = self.con.cursor()


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.createConnection()

        # self.cur.execute("SELECT * FROM kinematicviscosity_viscositymjl")
        # print(self.cur.fetchall())


        self.ui.pushButton_search_kinematicviscosity.clicked.connect(self.click_pushButton_search_kinematicviscosity)

    def createConnection(self):
        """соединение с базой данных"""
        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()

    def click_pushButton_search_kinematicviscosity(self):
        name = self.ui.lineEdit_search_kinematicviscosity_name.text()
        lot = self.ui.lineEdit_lineEdit_search_kinematicviscosity_lot.text()
        temperature = self.ui.lineEdit_search_kinematicviscosity_temperature.text()

        self.cur.execute(f"SELECT name, lot, temperature, certifiedValue FROM kinematicviscosity_viscositymjl "
                         f"WHERE name='{name}' and lot='{lot}' and temperature='{temperature}'")
        data = self.cur.fetchall()

        r_count = len(data)
        c_count = len(data[0])

        table = self.ui.tableWidget_kinematic_results
        table.setRowCount(r_count)
        table.setColumnCount(c_count)
        table.setHorizontalHeaderLabels(['Название стандартного образца', 'Партия', 'Температура,'
                                        ' °C', 'Кинематическая вязкость, сСт'])
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        for r in range(r_count):
            for c in range(c_count):
                cell = QTableWidgetItem(str(data[r][c]))
                table.setItem(r, c, cell)



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyWindow()
    win.show()

    app.exec_()
