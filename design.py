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
        MainWindow.resize(850, 428)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.range = QWidget()
        self.range.setObjectName(u"range")
        self.verticalLayout = QVBoxLayout(self.range)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.range)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.range)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.range)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit_2 = QTextEdit(self.range)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout.addWidget(self.textEdit_2)

        self.tabWidget.addTab(self.range, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit_3 = QTextEdit(self.tab_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_2.addWidget(self.textEdit_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.textEdit_4 = QTextEdit(self.tab_2)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.verticalLayout_2.addWidget(self.textEdit_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_search_kinematicviscosity_name = QLabel(self.tab)
        self.label_search_kinematicviscosity_name.setObjectName(u"label_search_kinematicviscosity_name")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_search_kinematicviscosity_name.setFont(font)
        self.label_search_kinematicviscosity_name.setAlignment(Qt.AlignCenter)
        self.label_search_kinematicviscosity_name.setIndent(5)

        self.verticalLayout_3.addWidget(self.label_search_kinematicviscosity_name)

        self.lineEdit_search_kinematicviscosity_name = QLineEdit(self.tab)
        self.lineEdit_search_kinematicviscosity_name.setObjectName(u"lineEdit_search_kinematicviscosity_name")

        self.verticalLayout_3.addWidget(self.lineEdit_search_kinematicviscosity_name)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_search_kinematicviscosity_lot = QLabel(self.tab)
        self.label_search_kinematicviscosity_lot.setObjectName(u"label_search_kinematicviscosity_lot")
        self.label_search_kinematicviscosity_lot.setFont(font)
        self.label_search_kinematicviscosity_lot.setAlignment(Qt.AlignCenter)
        self.label_search_kinematicviscosity_lot.setIndent(5)

        self.verticalLayout_9.addWidget(self.label_search_kinematicviscosity_lot)

        self.lineEdit_lineEdit_search_kinematicviscosity_lot = QLineEdit(self.tab)
        self.lineEdit_lineEdit_search_kinematicviscosity_lot.setObjectName(u"lineEdit_lineEdit_search_kinematicviscosity_lot")

        self.verticalLayout_9.addWidget(self.lineEdit_lineEdit_search_kinematicviscosity_lot)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_search_kinematicviscosity_temperature = QLabel(self.tab)
        self.label_search_kinematicviscosity_temperature.setObjectName(u"label_search_kinematicviscosity_temperature")
        self.label_search_kinematicviscosity_temperature.setFont(font)
        self.label_search_kinematicviscosity_temperature.setAlignment(Qt.AlignCenter)
        self.label_search_kinematicviscosity_temperature.setIndent(5)

        self.verticalLayout_10.addWidget(self.label_search_kinematicviscosity_temperature)

        self.lineEdit_search_kinematicviscosity_temperature = QLineEdit(self.tab)
        self.lineEdit_search_kinematicviscosity_temperature.setObjectName(u"lineEdit_search_kinematicviscosity_temperature")

        self.verticalLayout_10.addWidget(self.lineEdit_search_kinematicviscosity_temperature)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.pushButton_search_kinematicviscosity = QPushButton(self.tab)
        self.pushButton_search_kinematicviscosity.setObjectName(u"pushButton_search_kinematicviscosity")
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton_search_kinematicviscosity.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_search_kinematicviscosity)

        self.label_searchresult_kinematicviscosity = QLabel(self.tab)
        self.label_searchresult_kinematicviscosity.setObjectName(u"label_searchresult_kinematicviscosity")
        self.label_searchresult_kinematicviscosity.setFont(font)
        self.label_searchresult_kinematicviscosity.setAlignment(Qt.AlignCenter)
        self.label_searchresult_kinematicviscosity.setIndent(5)

        self.verticalLayout_4.addWidget(self.label_searchresult_kinematicviscosity)

        self.tableWidget_kinematic_results = QTableWidget(self.tab)
        self.tableWidget_kinematic_results.setObjectName(u"tableWidget_kinematic_results")

        self.verticalLayout_4.addWidget(self.tableWidget_kinematic_results)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

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
        self.label_search_kinematicviscosity_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_search_kinematicviscosity_lot.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f", None))
        self.label_search_kinematicviscosity_temperature.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.pushButton_search_kinematicviscosity.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label_searchresult_kinematicviscosity.setText(QCoreApplication.translate("MainWindow", u" \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
    # retranslateUi

