# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(762, 621)
        SignUp.setStyleSheet(u"background-color: rgb(0, 97, 97);\n"
"background-color: rgb(1, 96, 131);")
        self.centralwidget = QWidget(SignUp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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


        self.verticalLayout.addLayout(self.verticalLayout_7)

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


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_password2 = QLabel(self.centralwidget)
        self.label_password2.setObjectName(u"label_password2")
        self.label_password2.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_password2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_password2)

        self.lineEdit_password2 = QLineEdit(self.centralwidget)
        self.lineEdit_password2.setObjectName(u"lineEdit_password2")
        self.lineEdit_password2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.lineEdit_password2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.pushButton_enter = QPushButton(self.centralwidget)
        self.pushButton_enter.setObjectName(u"pushButton_enter")
        self.pushButton_enter.setMinimumSize(QSize(75, 0))
        self.pushButton_enter.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"font: 14pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255)\n"
"")

        self.verticalLayout.addWidget(self.pushButton_enter)

        SignUp.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SignUp)
        self.statusbar.setObjectName(u"statusbar")
        SignUp.setStatusBar(self.statusbar)

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"\u0412\u0416-\u041f\u0410", None))
        self.label_autorisation.setText(QCoreApplication.translate("SignUp", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_login.setText(QCoreApplication.translate("SignUp", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_password.setText(QCoreApplication.translate("SignUp", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_password2.setText(QCoreApplication.translate("SignUp", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_enter.setText(QCoreApplication.translate("SignUp", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

