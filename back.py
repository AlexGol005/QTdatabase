import os
import PySide2
from PySide2.QtSql import QSqlDatabase

import sqlite3

from PySide2.QtWidgets import QTableWidgetItem

from design import Ui_MainWindow
from PySide2 import QtWidgets, QtGui, QtCore
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

        self.cur.execute("SELECT * FROM kinematicviscosity_viscositymjl")
        print(self.cur.fetchall())

        self.ui.pushButton_search_kinematicviscosity.clicked.connect(self.click_pushButton_search_kinematicviscosity)

        # self.listView.setModel(self.model_listView)


    def createConnection(self):
        """соединение с базой данных"""
        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()

    def click_pushButton_search_kinematicviscosity(self):
        name = self.ui.lineEdit_search_kinematicviscosity_name.text()
        lot = self.lineEdit_lineEdit_search_kinematicviscosity_lot.text()
        temperature = self.lineEdit_search_kinematicviscosity_temperature.text()

        # print(self.cur.fetchall())
        # lst = [*self.cur.fetchall()]
        self.cur.execute(f"SELECT name, lot, temperature, certifiedValue FROM kinematicviscosity_viscositymjl WHERE name='{name}'")
        data = self.cur.fetchall()

        r_count = len(data)
        c_count = len(data[0])

        table = self.ui.tableWidget_kinematic_results
        table.setRowCount(r_count)
        table.setColumnCount(c_count)
        table.setHorizontalHeaderLabels(['Название стандартного образца', 'Партия', 'Температура, °C', 'Кинематическая вязкость, сСт'])
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        for r in range(r_count):
            for c in range(c_count):
                cell = QTableWidgetItem(str(data[r][c]))
                table.setItem(r, c, cell)





#         self.setMouseTracking(True)
#
#         self.ui.comboBox.addItems(["HEX", "DEC", "OCT", "BIN"])
#         self.ui.pushButtonGET.setShortcut(QtGui.QKeySequence("F1"))
#
# # signals
#         self.ui.pushButtonLT.clicked.connect(self.onPBLTclicked)
#         self.ui.pushButtonRT.clicked.connect(self.onPBRTclicked)
#         self.ui.pushButtonLD.clicked.connect(self.onPBLDclicked)
#         self.ui.pushButtonRD.clicked.connect(self.onPBRDclicked)
#         self.ui.pushButtonCenter.clicked.connect(self.onPBCenterclicked)
#         self.ui.pushButtonGET.clicked.connect(self.getScreenPosition)
#         self.ui.dial.valueChanged.connect(self.showLCD)
#         self.ui.horizontalSlider.valueChanged.connect(self.showLCD)
#         self.ui.dial.installEventFilter(self)
#
#
#     def onPBLTclicked(self):
#         self.move(0, 0)
#
#     def onPBRTclicked(self):
#         print(QtWidgets.QApplication.screenAt(self.pos()).size().width())
#         print(self.width())
#         self.move(QtWidgets.QApplication.screenAt(self.pos()).size().width() - self.width(), 0)
#
#     def onPBLDclicked(self):
#         print(QtWidgets.QApplication.screenAt(self.pos()).size().height())
#         print(self.height())
#         self.move(0, QtWidgets.QApplication.screenAt(self.pos()).size().height() - self.height() - 75)
#
#     def onPBRDclicked(self):
#         print(QtWidgets.QApplication.screenAt(self.pos()).size().height())
#         print(self.height())
#         self.move(QtWidgets.QApplication.screenAt(self.pos()).size().width() - self.width(), QtWidgets.QApplication.screenAt(self.pos()).size().height() - self.height() - 75)
#
#     def onPBCenterclicked(self):
#         self.move(QtWidgets.QApplication.screenAt(self.pos()).size().width()/2 - self.width()/2,
#                   QtWidgets.QApplication.screenAt(self.pos()).size().height()/2 - self.height()/2)
#
#     def getScreenPosition(self):
#         print(self.pos())
#         print(QtWidgets.QApplication.screens())
#         print(QtWidgets.QApplication.primaryScreen())
#         self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screens()))
#
#     def showLCD(self):
#         if self.sender().objectName() == "dial":
#             value = self.ui.dial.value()
#             self.ui.horizontalSlider.setValue(value)
#
#         elif self.sender().objectName() == "horizontalSlider":
#             value = self.ui.horizontalSlider.value()
#             self.ui.dial.setValue(value)
#
# # events
#     def changeEvent(self, event: QtCore.QEvent) -> None:
#         if event.type() == QtCore.QEvent.Type.WindowStateChange:
#             if self.isMinimized():
#                 print('окно свернуто')
#
#     def moveEvent(self, event: QtGui.QMoveEvent) -> None:
#         print(self.pos())
#
#     def event(self, event: QtCore.QEvent):
#         if event.type() == QtCore.QEvent.Resize:
#             print(self.size())
#
#         return QtWidgets.QWidget.event(self, event)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyWindow()
    win.show()

    app.exec_()