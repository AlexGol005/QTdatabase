import os

import PySide2

from design import Ui_MainWindow
from PySide2 import QtWidgets, QtGui, QtCore
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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