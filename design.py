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


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(878, 265)
        mainWindow.setMinimumSize(QSize(878, 262))
        mainWindow.setMaximumSize(QSize(880, 265))
        font = QFont()
        font.setPointSize(15)
        mainWindow.setFont(font)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.a_line = QLineEdit(self.centralwidget)
        self.a_line.setObjectName(u"a_line")
        self.a_line.setGeometry(QRect(10, 50, 201, 30))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 11, 24))
        self.b_line = QLineEdit(self.centralwidget)
        self.b_line.setObjectName(u"b_line")
        self.b_line.setGeometry(QRect(130, 50, 201, 30))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 20, 11, 24))
        self.c_line = QLineEdit(self.centralwidget)
        self.c_line.setObjectName(u"c_line")
        self.c_line.setGeometry(QRect(260, 50, 201, 30))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 20, 9, 24))
        self.g_line = QLineEdit(self.centralwidget)
        self.g_line.setObjectName(u"g_line")
        self.g_line.setGeometry(QRect(400, 50, 201, 30))
        self.h_line = QLineEdit(self.centralwidget)
        self.h_line.setObjectName(u"h_line")
        self.h_line.setGeometry(QRect(530, 50, 201, 30))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 20, 11, 24))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(530, 20, 11, 24))
        self.n_line = QLineEdit(self.centralwidget)
        self.n_line.setObjectName(u"n_line")
        self.n_line.setGeometry(QRect(660, 50, 201, 30))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(660, 20, 11, 24))
        self.simpson_button = QPushButton(self.centralwidget)
        self.simpson_button.setObjectName(u"simpson_button")
        self.simpson_button.setGeometry(QRect(20, 100, 181, 32))
        self.sp_button = QPushButton(self.centralwidget)
        self.sp_button.setObjectName(u"sp_button")
        self.sp_button.setGeometry(QRect(260, 100, 321, 32))
        self.simpson_label = QLabel(self.centralwidget)
        self.simpson_label.setObjectName(u"simpson_label")
        self.simpson_label.setGeometry(QRect(20, 140, 231, 24))
        self.sp_label = QLabel(self.centralwidget)
        self.sp_label.setObjectName(u"sp_label")
        self.sp_label.setGeometry(QRect(260, 140, 271, 24))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 878, 34))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"calculator", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"a", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"b", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"c", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"g", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"h", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"n", None))
        self.simpson_button.setText(QCoreApplication.translate("mainWindow", u"\u043c\u0435\u0442\u043e\u0434 \u0421\u0438\u043c\u043f\u0441\u043e\u043d\u0430", None))
        self.sp_button.setText(QCoreApplication.translate("mainWindow", u"\u043c\u0435\u0442\u043e\u0434 \u0441\u0440\u0435\u0434\u043d\u0438\u0445 \u043f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u0432", None))
        self.simpson_label.setText("")
        self.sp_label.setText("")
    # retranslateUi

