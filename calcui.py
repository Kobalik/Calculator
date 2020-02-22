# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(334, 318)
        Form.setStyleSheet(u"Form {\n"
"	background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: silver;\n"
"	color: #fff;\n"
"	border: 2px solid;\n"
"	font-weight: bold;\n"
"	font-size: 16px;\n"
"	height: 30px;\n"
"	width: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 60, 320, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dividButton = QPushButton(self.gridLayoutWidget)
        self.dividButton.setObjectName(u"dividButton")

        self.gridLayout.addWidget(self.dividButton, 3, 3, 1, 1)

        self.pushButton_0 = QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.gridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)

        self.dotButton = QPushButton(self.gridLayoutWidget)
        self.dotButton.setObjectName(u"dotButton")

        self.gridLayout.addWidget(self.dotButton, 4, 2, 1, 1)

        self.equalsButton = QPushButton(self.gridLayoutWidget)
        self.equalsButton.setObjectName(u"equalsButton")

        self.gridLayout.addWidget(self.equalsButton, 4, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.minusButton = QPushButton(self.gridLayoutWidget)
        self.minusButton.setObjectName(u"minusButton")

        self.gridLayout.addWidget(self.minusButton, 2, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.miltiplyButton = QPushButton(self.gridLayoutWidget)
        self.miltiplyButton.setObjectName(u"miltiplyButton")

        self.gridLayout.addWidget(self.miltiplyButton, 4, 0, 1, 1)

        self.plusButton = QPushButton(self.gridLayoutWidget)
        self.plusButton.setObjectName(u"plusButton")

        self.gridLayout.addWidget(self.plusButton, 1, 3, 1, 1)

        self.clearButton = QPushButton(self.gridLayoutWidget)
        self.clearButton.setObjectName(u"clearButton")

        self.gridLayout.addWidget(self.clearButton, 0, 0, 1, 1)

        self.deleteButton = QPushButton(self.gridLayoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.gridLayout.addWidget(self.deleteButton, 0, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.endBracketButton = QPushButton(self.gridLayoutWidget)
        self.endBracketButton.setObjectName(u"endBracketButton")

        self.gridLayout.addWidget(self.endBracketButton, 0, 2, 1, 1)

        self.startBracketButton = QPushButton(self.gridLayoutWidget)
        self.startBracketButton.setObjectName(u"startBracketButton")

        self.gridLayout.addWidget(self.startBracketButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 321, 41))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(16)
        self.lineEdit.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calculator", None))
        self.dividButton.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.dotButton.setText(QCoreApplication.translate("Form", u".", None))
        self.equalsButton.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.minusButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.miltiplyButton.setText(QCoreApplication.translate("Form", u"*", None))
        self.plusButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.clearButton.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.endBracketButton.setText(QCoreApplication.translate("Form", u")", None))
        self.startBracketButton.setText(QCoreApplication.translate("Form", u"(", None))
    # retranslateUi

