# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceOR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 770)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(560, 770))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.RunQt = QtWidgets.QPushButton(self.centralwidget)
        self.RunQt.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RunQt.setFont(font)
        self.RunQt.setObjectName("RunQt")
        self.gridLayout.addWidget(self.RunQt, 3, 12, 1, 2)
        self.NumRollQt = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.NumRollQt.setFont(font)
        self.NumRollQt.setMinimum(1)
        self.NumRollQt.setMaximum(50)
        self.NumRollQt.setObjectName("NumRollQt")
        self.gridLayout.addWidget(self.NumRollQt, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.DetTextQt = QtWidgets.QTextEdit(self.centralwidget)
        self.DetTextQt.setMinimumSize(QtCore.QSize(540, 650))
        self.DetTextQt.setMaximumSize(QtCore.QSize(1900, 1000))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DetTextQt.setFont(font)
        self.DetTextQt.setObjectName("DetTextQt")
        self.gridLayout.addWidget(self.DetTextQt, 5, 0, 1, 14)
        self.DicePullQt = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DicePullQt.setFont(font)
        self.DicePullQt.setMinimum(1)
        self.DicePullQt.setObjectName("DicePullQt")
        self.gridLayout.addWidget(self.DicePullQt, 3, 0, 1, 1)
        self.StrQt = QtWidgets.QCheckBox(self.centralwidget)
        self.StrQt.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StrQt.setFont(font)
        self.StrQt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.StrQt.setObjectName("StrQt")
        self.gridLayout.addWidget(self.StrQt, 0, 12, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.WPchQt = QtWidgets.QCheckBox(self.centralwidget)
        self.WPchQt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WPchQt.setAutoFillBackground(True)
        self.WPchQt.setText("")
        self.WPchQt.setObjectName("WPchQt")
        self.gridLayout.addWidget(self.WPchQt, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)
        self.RRchQt = QtWidgets.QCheckBox(self.centralwidget)
        self.RRchQt.setEnabled(False)
        self.RRchQt.setMinimumSize(QtCore.QSize(16, 16))
        self.RRchQt.setMaximumSize(QtCore.QSize(100, 100))
        self.RRchQt.setSizeIncrement(QtCore.QSize(0, 0))
        self.RRchQt.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RRchQt.setFont(font)
        self.RRchQt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RRchQt.setAutoFillBackground(False)
        self.RRchQt.setText("")
        self.RRchQt.setIconSize(QtCore.QSize(30, 30))
        self.RRchQt.setTristate(False)
        self.RRchQt.setObjectName("RRchQt")
        self.gridLayout.addWidget(self.RRchQt, 3, 3, 1, 1)
        self.RRstrQt = QtWidgets.QPushButton(self.centralwidget)
        self.RRstrQt.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.RRstrQt.setFont(font)
        self.RRstrQt.setObjectName("RRstrQt")
        self.gridLayout.addWidget(self.RRstrQt, 3, 11, 1, 1)
        self.WPstrQt = QtWidgets.QPushButton(self.centralwidget)
        self.WPstrQt.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.WPstrQt.setFont(font)
        self.WPstrQt.setObjectName("WPstrQt")
        self.gridLayout.addWidget(self.WPstrQt, 0, 11, 1, 1)
        self.QQt = QtWidgets.QComboBox(self.centralwidget)
        self.QQt.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QQt.setFont(font)
        self.QQt.setEditable(False)
        self.QQt.setObjectName("QQt")
        self.QQt.addItem("")
        self.QQt.addItem("")
        self.QQt.addItem("")
        self.QQt.addItem("")
        self.QQt.addItem("")
        self.gridLayout.addWidget(self.QQt, 3, 8, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 8, 1, 2)
        self.OMQt = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.OMQt.setFont(font)
        self.OMQt.setMinimum(-10)
        self.OMQt.setMaximum(10)
        self.OMQt.setObjectName("OMQt")
        self.gridLayout.addWidget(self.OMQt, 3, 6, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 4, 1, 2)
        self.LDQt = QtWidgets.QPushButton(self.centralwidget)
        self.LDQt.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LDQt.setFont(font)
        self.LDQt.setObjectName("LDQt")
        self.gridLayout.addWidget(self.LDQt, 0, 4, 1, 4)
        self.FAQQt = QtWidgets.QPushButton(self.centralwidget)
        self.FAQQt.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.FAQQt.setFont(font)
        self.FAQQt.setObjectName("FAQQt")
        self.gridLayout.addWidget(self.FAQQt, 0, 10, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_2.setBuddy(self.NumRollQt)
        self.label.setBuddy(self.DicePullQt)
        self.label_4.setBuddy(self.RRchQt)
        self.label_3.setBuddy(self.QQt)

        self.retranslateUi(MainWindow)
        self.QQt.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.DicePullQt, self.NumRollQt)
        MainWindow.setTabOrder(self.NumRollQt, self.QQt)
        MainWindow.setTabOrder(self.QQt, self.StrQt)
        MainWindow.setTabOrder(self.StrQt, self.RunQt)
        MainWindow.setTabOrder(self.RunQt, self.DetTextQt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RunQt.setToolTip(_translate("MainWindow", "Бросай!"))
        self.RunQt.setText(_translate("MainWindow", "GO"))
        self.NumRollQt.setToolTip(_translate("MainWindow", "Кол-во Бросков"))
        self.label_2.setToolTip(_translate("MainWindow", "Кол-во Бросков"))
        self.label_2.setText(_translate("MainWindow", "Roll"))
        self.label.setToolTip(_translate("MainWindow", "Запас кубов"))
        self.label.setText(_translate("MainWindow", "Dice"))
        self.DicePullQt.setToolTip(_translate("MainWindow", "Запас кубов"))
        self.StrQt.setToolTip(_translate("MainWindow", "Генерировать каждый бросок отдельно\n"
"на длительном действии"))
        self.StrQt.setText(_translate("MainWindow", "Stroka"))
        self.label_6.setToolTip(_translate("MainWindow", "Трата ПСВ"))
        self.label_6.setText(_translate("MainWindow", "WP"))
        self.WPchQt.setToolTip(_translate("MainWindow", "Трата ПСВ"))
        self.label_4.setToolTip(_translate("MainWindow", "Переброс неудачных кубов"))
        self.label_4.setText(_translate("MainWindow", "RR"))
        self.RRchQt.setToolTip(_translate("MainWindow", "Переброс неудачных кубов"))
        self.RRstrQt.setToolTip(_translate("MainWindow", "Трата ПСВ на переброс в единичном бросоке"))
        self.RRstrQt.setText(_translate("MainWindow", "RR"))
        self.WPstrQt.setToolTip(_translate("MainWindow", "Трата ПСВ на +3 куба в единичном бросоке"))
        self.WPstrQt.setText(_translate("MainWindow", "WP"))
        self.QQt.setToolTip(_translate("MainWindow", "Качество, Профа и т.д.\n"
"Определяет то, какие значения\n"
"добрасываются при выпадении успехов"))
        self.QQt.setItemText(0, _translate("MainWindow", "+2: (8, 9, 10)"))
        self.QQt.setItemText(1, _translate("MainWindow", "+1: (9, 10)"))
        self.QQt.setItemText(2, _translate("MainWindow", "0: (10)"))
        self.QQt.setItemText(3, _translate("MainWindow", "-1: (-)"))
        self.QQt.setItemText(4, _translate("MainWindow", "-2: (-1)"))
        self.label_3.setToolTip(_translate("MainWindow", "Доброс"))
        self.label_3.setText(_translate("MainWindow", "Q"))
        self.OMQt.setToolTip(_translate("MainWindow", "Количество\n"
"авто\n"
"успехов"))
        self.label_5.setToolTip(_translate("MainWindow", "Количество\n"
"авто\n"
"успехов"))
        self.label_5.setText(_translate("MainWindow", "OM"))
        self.LDQt.setText(_translate("MainWindow", "Куб удачи"))
        self.FAQQt.setToolTip(_translate("MainWindow", "Трата ПСВ на +3 куба в единичном бросоке"))
        self.FAQQt.setText(_translate("MainWindow", "FAQ"))

