# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReaderBaseInfoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 504)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("font: 75 14pt \"Adobe Arabic\";\n"
"background-color:#efefef;\n"
"color:#000;\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dataTableWidget = QtWidgets.QTableWidget(self.frame)
        self.dataTableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dataTableWidget.setStyleSheet("font: 75 6pt \"Adobe Arabic\";\n"
"border-radius:0px;\n"
"color:#000;\n"
"border: 1px solid #000;\n"
"background-color:#FFF")
        self.dataTableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.dataTableWidget.setObjectName("dataTableWidget")
        self.dataTableWidget.setColumnCount(0)
        self.dataTableWidget.setRowCount(0)
        self.dataTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout_4.addWidget(self.dataTableWidget, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 3, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 3, 3, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 4)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_6.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 8, 1, 1)
        self.selectFileButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectFileButton.sizePolicy().hasHeightForWidth())
        self.selectFileButton.setSizePolicy(sizePolicy)
        self.selectFileButton.setMinimumSize(QtCore.QSize(150, 50))
        self.selectFileButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.selectFileButton.setSizeIncrement(QtCore.QSize(50, 100))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.selectFileButton.setFont(font)
        self.selectFileButton.setAcceptDrops(False)
        self.selectFileButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selectFileButton.setStyleSheet("font: 75 14pt \"Adobe Arabic\";\n"
"border-radius:5px;\n"
"color:#000;\n"
"border: 1px solid #000")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/18637/.designer/uisource/importData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setIconSize(QtCore.QSize(0, 0))
        self.selectFileButton.setAutoDefault(False)
        self.selectFileButton.setDefault(True)
        self.selectFileButton.setFlat(False)
        self.selectFileButton.setObjectName("selectFileButton")
        self.gridLayout_6.addWidget(self.selectFileButton, 0, 1, 1, 2)
        self.savePushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.savePushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.savePushButton.setSizeIncrement(QtCore.QSize(50, 100))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.savePushButton.setFont(font)
        self.savePushButton.setStyleSheet("font: 75 14pt \"Adobe Arabic\";\n"
"border-radius:5px;\n"
"color:#000;\n"
"border: 1px solid #000")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/18637/.designer/uisource/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savePushButton.setIcon(icon1)
        self.savePushButton.setIconSize(QtCore.QSize(0, 0))
        self.savePushButton.setCheckable(False)
        self.savePushButton.setAutoExclusive(False)
        self.savePushButton.setAutoDefault(False)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout_6.addWidget(self.savePushButton, 0, 5, 1, 1)
        self.mongoDBButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mongoDBButton.sizePolicy().hasHeightForWidth())
        self.mongoDBButton.setSizePolicy(sizePolicy)
        self.mongoDBButton.setMinimumSize(QtCore.QSize(150, 50))
        self.mongoDBButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.mongoDBButton.setStyleSheet("font: 75 14pt \"Adobe Arabic\";\n"
"border-radius:5px;\n"
"color:#000;\n"
"border: 1px solid #000")
        self.mongoDBButton.setObjectName("mongoDBButton")
        self.gridLayout_6.addWidget(self.mongoDBButton, 0, 7, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 0, 6, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 3, 2, 2, 1)
        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout_3.addWidget(self.timeLabel, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dataTableWidget, self.savePushButton)
        MainWindow.setTabOrder(self.savePushButton, self.selectFileButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DrillProjectInfoReader"))
        self.selectFileButton.setText(_translate("MainWindow", "导 入 数 据"))
        self.savePushButton.setText(_translate("MainWindow", "转 存 e x c e l"))
        self.mongoDBButton.setText(_translate("MainWindow", "写 入 数 据 库"))
        self.timeLabel.setText(_translate("MainWindow", "年月日"))
