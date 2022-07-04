import os
import PySide2
from PySide2.QtWidgets import QTableWidgetItem
from PySide2 import QtWidgets

import sqlite3
from autorisation import Ui_Autorisation

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class AutWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Autorisation()
        self.ui.setupUi(self)


        self.ui.pushButton_enter.clicked.connect(self.loginfunction)
        self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)


    def loginfunction(self):
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()
        print('успешная авторизация!')


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = AutWindow()
    widget = QtWidgets.QStackedWidget
    # widget.addWidget(win)
    # widget.setFixedWidth(480)
    # widget.setFixedHeight(620)

    win.show()

    app.exec_()