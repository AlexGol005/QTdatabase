# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(563, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 541, 381))
        self.range = QWidget()
        self.range.setObjectName(u"range")
        self.widget = QWidget(self.range)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 531, 331))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout.addWidget(self.textEdit_2)

        self.tabWidget.addTab(self.range, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 531, 321))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit_3 = QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_2.addWidget(self.textEdit_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.textEdit_4 = QTextEdit(self.layoutWidget)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.verticalLayout_2.addWidget(self.textEdit_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(5)

        self.verticalLayout_3.addWidget(self.label)

        self.name = QTextEdit(self.tab)
        self.name.setObjectName(u"name")
        self.name.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_3.addWidget(self.name)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setIndent(5)

        self.verticalLayout_4.addWidget(self.label_4)

        self.lot = QTextEdit(self.tab)
        self.lot.setObjectName(u"lot")
        self.lot.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_4.addWidget(self.lot)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setIndent(5)

        self.verticalLayout_5.addWidget(self.label_5)

        self.temp = QTextEdit(self.tab)
        self.temp.setObjectName(u"temp")
        self.temp.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_5.addWidget(self.temp)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton_5.setFont(font1)

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(5)

        self.verticalLayout_6.addWidget(self.label_2)

        self.lot_2 = QTextEdit(self.tab)
        self.lot_2.setObjectName(u"lot_2")
        self.lot_2.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_6.addWidget(self.lot_2)

        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0416-\u041f\u0410", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.range), QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0442\u0438\u044e", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0430\u0440\u0442\u0438\u044e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.name.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0430\u0440\u0442\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
    # retranslateUi

