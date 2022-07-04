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
        Autorisation.resize(549, 475)
        Autorisation.setStyleSheet(u"background-color: rgb(0, 97, 97);\n"
"background-color: rgb(1, 96, 131);")
        self.widget = QWidget(Autorisation)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 451, 431))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_autorisation = QLabel(self.widget)
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

        self.verticalLayout_2.addWidget(self.label_autorisation)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_login = QLabel(self.widget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_login)

        self.lineEdit_login = QLineEdit(self.widget)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lineEdit_login)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_password = QLabel(self.widget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lineEdit_password)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pushButton_enter = QPushButton(self.widget)
        self.pushButton_enter.setObjectName(u"pushButton_enter")
        self.pushButton_enter.setMinimumSize(QSize(75, 0))
        self.pushButton_enter.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"font: 14pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255)\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_enter)


        self.retranslateUi(Autorisation)

        QMetaObject.connectSlotsByName(Autorisation)
    # setupUi

    def retranslateUi(self, Autorisation):
        Autorisation.setWindowTitle(QCoreApplication.translate("Autorisation", u"\u0424\u043e\u0440\u043c\u0430 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_autorisation.setText(QCoreApplication.translate("Autorisation", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_login.setText(QCoreApplication.translate("Autorisation", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_password.setText(QCoreApplication.translate("Autorisation", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_enter.setText(QCoreApplication.translate("Autorisation", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

