# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(590, 300)
        MainWindow.setMaximumSize(QtCore.QSize(590, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.result_btn = QtWidgets.QPushButton(self.centralwidget)
        self.result_btn.setGeometry(QtCore.QRect(170, 170, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.result_btn.setFont(font)
        self.result_btn.setObjectName("result_btn")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(170, 210, 271, 41))
        self.result_label.setSizeIncrement(QtCore.QSize(791, 0))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.result_label.setFont(font)
        self.result_label.setText("")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.subjects_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.subjects_dropdown.setGeometry(QtCore.QRect(170, 70, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.subjects_dropdown.setFont(font)
        self.subjects_dropdown.setObjectName("subjects_dropdown")
        self.subjects_dropdown.addItem("")
        self.weight_input = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_input.setGeometry(QtCore.QRect(172, 119, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.weight_input.setFont(font)
        self.weight_input.setObjectName("weight_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 591, 45))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.result_btn.setText(_translate("MainWindow", "Get Results"))
        self.subjects_dropdown.setItemText(0, _translate("MainWindow", "Select Subject"))
        self.label.setText(_translate("MainWindow", "   Grade Calculator"))
