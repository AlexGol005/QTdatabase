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

    def loginfunction(self):


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = AutWindow()
    win.show()

    app.exec_()