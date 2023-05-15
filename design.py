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
        MainWindow.resize(465, 440)
        MainWindow.setMinimumSize(QSize(465, 440))
        MainWindow.setMaximumSize(QSize(465, 440))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 20, 363, 336))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.coef_edit = QLineEdit(self.widget)
        self.coef_edit.setObjectName(u"coef_edit")

        self.verticalLayout.addWidget(self.coef_edit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.eps_edit = QLineEdit(self.widget)
        self.eps_edit.setObjectName(u"eps_edit")

        self.verticalLayout.addWidget(self.eps_edit)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.left_edit = QLineEdit(self.widget)
        self.left_edit.setObjectName(u"left_edit")

        self.verticalLayout.addWidget(self.left_edit)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.right_edit = QLineEdit(self.widget)
        self.right_edit.setObjectName(u"right_edit")

        self.verticalLayout.addWidget(self.right_edit)

        self.pdButton = QPushButton(self.widget)
        self.pdButton.setObjectName(u"pdButton")

        self.verticalLayout.addWidget(self.pdButton)

        self.pd_Label = QLabel(self.widget)
        self.pd_Label.setObjectName(u"pd_Label")

        self.verticalLayout.addWidget(self.pd_Label)

        self.ntButton = QPushButton(self.widget)
        self.ntButton.setObjectName(u"ntButton")

        self.verticalLayout.addWidget(self.ntButton)

        self.nt_label = QLabel(self.widget)
        self.nt_label.setObjectName(u"nt_label")

        self.verticalLayout.addWidget(self.nt_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 465, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u043e\u043c \u0434\u0432\u0435\u043d\u0430\u0434\u0446\u0430\u0442\u043e\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u043d\u043d\u0443\u044e \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0446 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430:", None))
        self.pdButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u043d\u043e\u0433\u043e \u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pd_Label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442: ", None))
        self.ntButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u041d\u044c\u044e\u0442\u043e\u043d\u0430", None))
        self.nt_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442: ", None))
    # retranslateUi

