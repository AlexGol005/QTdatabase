# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autorisation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Autorisation(object):
    def setupUi(self, Autorisation):
        if not Autorisation.objectName():
            Autorisation.setObjectName(u"Autorisation")
        Autorisation.resize(599, 566)
        Autorisation.setStyleSheet(u"background-color: rgb(0, 97, 97);\n"
"background-color: rgb(1, 96, 131);")
        self.centralwidget = QWidget(Autorisation)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_autorisation = QLabel(self.centralwidget)
        self.label_autorisation.setObjectName(u"label_autorisation")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_autorisation.sizePolicy().hasHeightForWidth())
        self.label_autorisation.setSizePolicy(sizePolicy)
        self.label_autorisation.setMaximumSize(QSize(16777215, 40))
        self.label_autorisation.setStyleSheet(u"font: 75 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_autorisation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_autorisation)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_login = QLabel(self.centralwidget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_login)

        self.lineEdit_login = QLineEdit(self.centralwidget)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.lineEdit_login)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.lineEdit_password)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_no_acc = QLabel(self.centralwidget)
        self.label_no_acc.setObjectName(u"label_no_acc")
        self.label_no_acc.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_no_acc)

        self.pushButton_signup = QPushButton(self.centralwidget)
        self.pushButton_signup.setObjectName(u"pushButton_signup")
        self.pushButton_signup.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"font: 9pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255)")

        self.horizontalLayout_6.addWidget(self.pushButton_signup)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.pushButton_enter = QPushButton(self.centralwidget)
        self.pushButton_enter.setObjectName(u"pushButton_enter")
        self.pushButton_enter.setMinimumSize(QSize(75, 0))
        self.pushButton_enter.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"font: 14pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255)\n"
"")

        self.verticalLayout_5.addWidget(self.pushButton_enter)

        Autorisation.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Autorisation)
        self.statusbar.setObjectName(u"statusbar")
        Autorisation.setStatusBar(self.statusbar)

        self.retranslateUi(Autorisation)

        QMetaObject.connectSlotsByName(Autorisation)
    # setupUi

    def retranslateUi(self, Autorisation):
        Autorisation.setWindowTitle(QCoreApplication.translate("Autorisation", u"\u0412\u0416-\u041f\u0410", None))
        self.label_autorisation.setText(QCoreApplication.translate("Autorisation", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_login.setText(QCoreApplication.translate("Autorisation", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_password.setText(QCoreApplication.translate("Autorisation", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_no_acc.setText(QCoreApplication.translate("Autorisation", u"   \u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430?", None))
        self.pushButton_signup.setText(QCoreApplication.translate("Autorisation", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.pushButton_enter.setText(QCoreApplication.translate("Autorisation", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

