# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eKW_pobieracz.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 400)
        MainWindow.setMinimumSize(QtCore.QSize(320, 400))
        MainWindow.setMaximumSize(QtCore.QSize(320, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineList = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineList.setObjectName("lineList")
        self.horizontalLayout.addWidget(self.lineList)
        self.btnList = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnList.setObjectName("btnList")
        self.horizontalLayout.addWidget(self.btnList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineSave = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineSave.setObjectName("lineSave")
        self.horizontalLayout_2.addWidget(self.lineSave)
        self.btnSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_2.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setGeometry(QtCore.QRect(10, 330, 301, 23))
        self.btnRun.setObjectName("btnRun")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 230, 301, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 19, 281, 69))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.lineSign = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineSign.setObjectName("lineSign")
        self.verticalLayout_4.addWidget(self.lineSign)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.lineFloor = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineFloor.setText("")
        self.lineFloor.setObjectName("lineFloor")
        self.verticalLayout_5.addWidget(self.lineFloor)
        self.lineRoof = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineRoof.setText("")
        self.lineRoof.setObjectName("lineRoof")
        self.verticalLayout_5.addWidget(self.lineRoof)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btnGen = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnGen.setFont(font)
        self.btnGen.setObjectName("btnGen")
        self.verticalLayout_7.addWidget(self.btnGen)
        self.btnGenSave = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnGenSave.setFont(font)
        self.btnGenSave.setObjectName("btnGenSave")
        self.verticalLayout_7.addWidget(self.btnGenSave)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 301, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 20, 131, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ch1o = QtWidgets.QCheckBox(self.widget)
        self.ch1o.setChecked(True)
        self.ch1o.setObjectName("ch1o")
        self.verticalLayout_2.addWidget(self.ch1o)
        self.ch1s = QtWidgets.QCheckBox(self.widget)
        self.ch1s.setChecked(False)
        self.ch1s.setObjectName("ch1s")
        self.verticalLayout_2.addWidget(self.ch1s)
        self.ch2 = QtWidgets.QCheckBox(self.widget)
        self.ch2.setChecked(True)
        self.ch2.setObjectName("ch2")
        self.verticalLayout_2.addWidget(self.ch2)
        self.ch3 = QtWidgets.QCheckBox(self.widget)
        self.ch3.setChecked(True)
        self.ch3.setObjectName("ch3")
        self.verticalLayout_2.addWidget(self.ch3)
        self.ch4 = QtWidgets.QCheckBox(self.widget)
        self.ch4.setObjectName("ch4")
        self.verticalLayout_2.addWidget(self.ch4)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget1 = QtWidgets.QWidget(self.groupBox_3)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 131, 114))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chMerge = QtWidgets.QCheckBox(self.widget1)
        self.chMerge.setCheckable(False)
        self.chMerge.setObjectName("chMerge")
        self.verticalLayout_3.addWidget(self.chMerge)
        self.chError = QtWidgets.QCheckBox(self.widget1)
        self.chError.setChecked(True)
        self.chError.setObjectName("chError")
        self.verticalLayout_3.addWidget(self.chError)
        self.chTurbo = QtWidgets.QCheckBox(self.widget1)
        self.chTurbo.setCheckable(False)
        self.chTurbo.setObjectName("chTurbo")
        self.verticalLayout_3.addWidget(self.chTurbo)
        self.chBg = QtWidgets.QCheckBox(self.widget1)
        self.chBg.setObjectName("chBg")
        self.verticalLayout_3.addWidget(self.chBg)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Plik = QtWidgets.QMenu(self.menubar)
        self.menu_Plik.setObjectName("menu_Plik")
        self.menu_O_programie = QtWidgets.QMenu(self.menubar)
        self.menu_O_programie.setObjectName("menu_O_programie")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Wsparcie = QtWidgets.QAction(MainWindow)
        self.action_Wsparcie.setObjectName("action_Wsparcie")
        self.action_github = QtWidgets.QAction(MainWindow)
        self.action_github.setObjectName("action_github")
        self.menu_O_programie.addAction(self.action_Wsparcie)
        self.menu_O_programie.addAction(self.action_github)
        self.menubar.addAction(self.menu_Plik.menuAction())
        self.menubar.addAction(self.menu_O_programie.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eKW pobieracz 0.3"))
        self.btnList.setText(_translate("MainWindow", "Lista Kw"))
        self.btnSave.setText(_translate("MainWindow", "Folder zapisu"))
        self.btnRun.setText(_translate("MainWindow", "Rozpocznij pobieranie"))
        self.groupBox.setTitle(_translate("MainWindow", "Generowanie listy KW"))
        self.label_3.setText(_translate("MainWindow", "Znak"))
        self.lineSign.setPlaceholderText(_translate("MainWindow", "BB1B"))
        self.label_4.setText(_translate("MainWindow", "od .. do"))
        self.lineFloor.setPlaceholderText(_translate("MainWindow", "1"))
        self.lineRoof.setPlaceholderText(_translate("MainWindow", "99999999"))
        self.btnGen.setText(_translate("MainWindow", "Generuj"))
        self.btnGenSave.setText(_translate("MainWindow", "Pobierz \n"
"z zakresu"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Do pobrania"))
        self.ch1o.setText(_translate("MainWindow", "Dział I-O"))
        self.ch1s.setText(_translate("MainWindow", "Dział I-SP"))
        self.ch2.setText(_translate("MainWindow", "Dział II"))
        self.ch3.setText(_translate("MainWindow", "Dział III"))
        self.ch4.setText(_translate("MainWindow", "Dział IV"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Zmienne"))
        self.chMerge.setText(_translate("MainWindow", "Złącz działy w jeden\n"
"pdf"))
        self.chError.setText(_translate("MainWindow", "Gdy brak aktualnej \n"
"pobieraj zupełną"))
        self.chTurbo.setText(_translate("MainWindow", "Tryb TURBO (Uważaj!)"))
        self.chBg.setText(_translate("MainWindow", "Zachować tło strony"))
        self.menu_Plik.setTitle(_translate("MainWindow", "&Plik"))
        self.menu_O_programie.setTitle(_translate("MainWindow", "&O programie"))
        self.action_Wsparcie.setText(_translate("MainWindow", "&Postaw mi kawę"))
        self.action_github.setText(_translate("MainWindow", "&Github"))
