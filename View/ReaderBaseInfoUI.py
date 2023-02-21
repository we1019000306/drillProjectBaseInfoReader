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
        MainWindow.resize(800, 500)
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
        self.gridLayout_4.addWidget(self.dataTableWidget, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 2, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_6.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.savePushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setMinimumSize(QtCore.QSize(25, 50))
        self.savePushButton.setMaximumSize(QtCore.QSize(350, 16777215))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/18637/.designer/uisource/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savePushButton.setIcon(icon)
        self.savePushButton.setIconSize(QtCore.QSize(0, 0))
        self.savePushButton.setCheckable(False)
        self.savePushButton.setAutoExclusive(False)
        self.savePushButton.setAutoDefault(False)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout_6.addWidget(self.savePushButton, 0, 5, 1, 1)
        self.selectFileButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectFileButton.sizePolicy().hasHeightForWidth())
        self.selectFileButton.setSizePolicy(sizePolicy)
        self.selectFileButton.setMinimumSize(QtCore.QSize(400, 50))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/18637/.designer/uisource/importData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectFileButton.setIcon(icon1)
        self.selectFileButton.setIconSize(QtCore.QSize(0, 0))
        self.selectFileButton.setAutoDefault(False)
        self.selectFileButton.setDefault(True)
        self.selectFileButton.setFlat(False)
        self.selectFileButton.setObjectName("selectFileButton")
        self.gridLayout_6.addWidget(self.selectFileButton, 0, 0, 1, 2)
        self.previewPushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewPushButton.sizePolicy().hasHeightForWidth())
        self.previewPushButton.setSizePolicy(sizePolicy)
        self.previewPushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.previewPushButton.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.previewPushButton.setFont(font)
        self.previewPushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.previewPushButton.setStyleSheet("font: 75 14pt \"Adobe Arabic\";\n"
"border-radius:5px;\n"
"color:#000;\n"
"border: 1px solid #000")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/18637/.designer/uisource/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previewPushButton.setIcon(icon2)
        self.previewPushButton.setIconSize(QtCore.QSize(0, 0))
        self.previewPushButton.setAutoDefault(False)
        self.previewPushButton.setDefault(False)
        self.previewPushButton.setFlat(True)
        self.previewPushButton.setObjectName("previewPushButton")
        self.gridLayout_6.addWidget(self.previewPushButton, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 2, 1, 2, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menulayerPaint = QtWidgets.QMenu(self.menubar)
        self.menulayerPaint.setObjectName("menulayerPaint")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menulayerPaint.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dataTableWidget, self.savePushButton)
        MainWindow.setTabOrder(self.savePushButton, self.selectFileButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "layerPaintUtil"))
        self.savePushButton.setText(_translate("MainWindow", "保 存"))
        self.selectFileButton.setText(_translate("MainWindow", "导 入 数 据"))
        self.previewPushButton.setText(_translate("MainWindow", "预 览"))
        self.menulayerPaint.setTitle(_translate("MainWindow", "便捷预览"))