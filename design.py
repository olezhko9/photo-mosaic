# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__main__\Python\photo puzzle\design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(310, 10, 451, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pixmapLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.pixmapLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmapLabel.setObjectName("pixmapLabel")
        self.verticalLayout_2.addWidget(self.pixmapLabel)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(20, 230, 271, 31))
        self.runButton.setObjectName("runButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 10, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 271, 73))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.directoryLabel = QtWidgets.QLabel(self.widget)
        self.directoryLabel.setText("")
        self.directoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.directoryLabel.setObjectName("directoryLabel")
        self.gridLayout.addWidget(self.directoryLabel, 1, 1, 1, 1)
        self.directoryButton = QtWidgets.QPushButton(self.widget)
        self.directoryButton.setObjectName("directoryButton")
        self.gridLayout.addWidget(self.directoryButton, 1, 0, 1, 1)
        self.pictureButton = QtWidgets.QPushButton(self.widget)
        self.pictureButton.setObjectName("pictureButton")
        self.gridLayout.addWidget(self.pictureButton, 0, 0, 1, 1)
        self.pictureLabel = QtWidgets.QLabel(self.widget)
        self.pictureLabel.setText("")
        self.pictureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureLabel.setObjectName("pictureLabel")
        self.gridLayout.addWidget(self.pictureLabel, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 150, 271, 71))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.pixelsTileLEdit = QtWidgets.QLineEdit(self.widget1)
        self.pixelsTileLEdit.setObjectName("pixelsTileLEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pixelsTileLEdit)
        self.processLEdit = QtWidgets.QLineEdit(self.widget1)
        self.processLEdit.setObjectName("processLEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.processLEdit)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.progressLayout = QtWidgets.QWidget(self.centralwidget)
        self.progressLayout.setEnabled(True)
        self.progressLayout.setGeometry(QtCore.QRect(20, 300, 271, 42))
        self.progressLayout.setObjectName("progressLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.progressLayout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.progressLayout)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.progressLayout)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pixmapLabel.setText(_translate("MainWindow", "Выбранное изображение"))
        self.runButton.setText(_translate("MainWindow", "Запустить"))
        self.directoryButton.setText(_translate("MainWindow", "Папка с картинками"))
        self.pictureButton.setText(_translate("MainWindow", "Выбрать картинку"))
        self.label_4.setText(_translate("MainWindow", "Количество процессов"))
        self.label_3.setText(_translate("MainWindow", "Пикселей в ячейке"))
        self.label.setText(_translate("MainWindow", "Прогресс выполнения"))
