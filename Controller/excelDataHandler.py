import sys
import time

import pandas as pd
import numpy as np
import xlrd
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from PyQt5.QtWidgets import QFileDialog, QApplication, QTableWidgetItem, QHeaderView

from View.ReaderBaseInfoUI import Ui_MainWindow

globalFilesPathList:list = []
globalCompanyList:list = []
globalDrillInfoList:list = []
globalDeepList:list = []
globalPerDayDeepList:list = []
globalWorkingStateList:list = []
globalTipsList:list = []


class window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectFileButton.clicked.connect(self.getFileOnClicked)
        self.selectFileButton.clicked.connect(self.loadBaseData)

    def getFileOnClicked(self):
        global globalFilesPathList
        global globalCompanyList
        global globalDrillInfoList
        global globalDeepList
        global globalPerDayDeepList
        global globalWorkingStateList
        global globalTipsList

        globalFilesPathList.clear()
        globalCompanyList.clear()
        globalDrillInfoList.clear()
        globalDeepList.clear()
        globalPerDayDeepList.clear()
        globalWorkingStateList.clear()
        globalTipsList.clear()

        self.selectFileButton.setEnabled(False)
        self.thread_2 = Thread_2()
        self.thread_2._signal.connect(self.setSelectFileButtonEnable)
        self.thread_2.start()
        fileNames, fileType = QFileDialog.getOpenFileNames(self,
                                                         "打开表格",
                                                         "",
                                                         "*.xlsx;*.xls;;All Files(*)")


        ###获取路径====================================================================
        if len(fileNames) == 0:
            print('未导入文件！！')
            globalFilesPathList.clear()
            pass
        else:
           for i in fileNames: globalFilesPathList.append(i)
           print(globalFilesPathList)

    def setSelectFileButtonEnable(self):
        self.selectFileButton.setEnabled(True)

    def loadBaseData(self):
        global globalFilesPathList
        global globalCompanyList
        global globalDrillInfoList
        global globalDeepList
        global globalPerDayDeepList
        global globalWorkingStateList
        global globalTipsList

        if len(globalFilesPathList) > 0:
            for i in globalFilesPathList:
                print(i)
                loadDataFromExcel(i)
            self.dataTableWidget.setColumnCount(6)
            self.dataTableWidget.setRowCount(20)
            n = 0
            self.dataTableWidget.setHorizontalHeaderLabels(['公司名称','项目基本情况介绍','钻孔深度','日进尺','工况','备注'])
            while n < len(globalDrillInfoList):
                #globalCompanyItem = QTableWidgetItem(str(globalCompanyList[n]))
                globalDrillItem = QTableWidgetItem(str(globalDrillInfoList[n]))
                globalDeepItem = QTableWidgetItem(str(globalDeepList[n]))
                globalPerDayDeepItem = QTableWidgetItem(str(globalPerDayDeepList[n]))
                globalWorkingStateItem = QTableWidgetItem(str(globalWorkingStateList[n]))
                globalTipsItem = QTableWidgetItem(str(globalTipsList[n]))
                # self.dataTableWidget.setItem(n,0,globalCompanyItem)
                self.dataTableWidget.setItem(n, 0, globalDrillItem)
                self.dataTableWidget.setItem(n, 1,globalDeepItem)
                self.dataTableWidget.setItem(n, 2, globalPerDayDeepItem)
                self.dataTableWidget.setItem(n, 3, globalWorkingStateItem)
                self.dataTableWidget.setItem(n, 4, globalTipsItem)
                n += 1
            self.dataTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.dataTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
            QApplication.processEvents()
        else:
            print('未导入文件！！！！')
def loadDataFromExcel(fileNames: str):
    global globalCompanyList
    global globalDrillInfoList
    global globalDeepList
    global globalPerDayDeepList
    global globalWorkingStateList
    global globalTipsList

    path_openfile_name = fileNames

    if path_openfile_name != '':
        input_table = pd.read_excel(path_openfile_name)

        # input_table_rows = input_table.shape[0]
        # input_table_colunms = input_table.shape[1]
        # dataDictKey = input_table.columns.values.tolist()
        # print(np.List(input_table.iloc[:,1]))
        dataList = np.array(input_table.iloc[0:, 1])
        # companyList = []
        drillInfoList = []
        deepList = []
        perDayDeepList = []
        workingStateList = []
        tipsList = []
        n = 0
        for i in dataList:
            # 索引出每个不为空的第一行即为新的项目数据行
            if str(i) != 'nan':
                #companyList.append(str(input_table.iloc[n,0]))

                # print(str(i).split())
                drillInfoStrList = str(i).split()
                #项目名称+施工地点+钻机编号+孔号+设计孔深+井型+孔径+开孔日期
                drillInfoList.append(''.join(drillInfoStrList[2]+'\n'+drillInfoStrList[1]+'\n'+drillInfoStrList[0]))
                print(drillInfoList)
                # print('钻孔深度：' + str(input_table.iloc[n, 2]) + '(m)')
                deepList.append(str(input_table.iloc[n, 2]) + '(m)')

               # print('日进尺：' + str(input_table.iloc[n, 3]) + '(m)')
                perDayDeepList.append(str(input_table.iloc[n, 3]) + '(m)')

                #print('工况：' + str(input_table.iloc[n, 5]))
                workingStateList.append(''.join(str(input_table.iloc[n, 5]).split()))

                #print('备注：' + str(input_table.iloc[n, 16]))
                tipsList.append(str(input_table.iloc[n, 16]))
            n += 1
        #companyList.pop(0)
        drillInfoList.pop(0)
        deepList.pop(0)
        perDayDeepList.pop(0)
        workingStateList.pop(0)
        tipsList.pop(0)
        print(drillInfoList)
        print(deepList)
        print(perDayDeepList)
        print(workingStateList)
        print(tipsList)
        globalDrillInfoList = globalDrillInfoList + drillInfoList
        globalDeepList = globalDeepList + deepList
        globalPerDayDeepList = globalPerDayDeepList + perDayDeepList
        globalWorkingStateList = globalWorkingStateList + workingStateList
        globalTipsList = globalTipsList + tipsList


qmut_1 = QMutex() # 创建线程锁
qmut_2 = QMutex()
# 继承QThread
class Thread_1(QThread):  # 线程1
    def __init__(self):
        super().__init__()

    def run(self):
        qmut_1.lock() # 加锁
        values = [1, 2, 3, 4, 5]
        for i in values:
            print(i)
            time.sleep(0.5)  # 休眠
        qmut_1.unlock() # 解锁


class Thread_2(QThread):  # 线程2
    _signal =pyqtSignal()
    def __init__(self):
        super().__init__()

    def run(self):
        # qmut_2.lock()  # 加锁
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            time.sleep(0.5)
        # qmut_2.unlock()  # 解锁
        self._signal.emit()



if __name__ == '__main__':
    #loadDataFromExcel('1')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = window()  # 创建窗体对象
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
    # a = []
    # a.append('1')
    # b = ['a']
    # b.insert(0,'1')
    # print(a)
    # print(b)
