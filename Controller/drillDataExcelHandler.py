import sys
import time

import pandas as pd
import numpy as np
import re
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from PyQt5.QtWidgets import QFileDialog, QApplication, QTableWidgetItem, QHeaderView

from View.ReaderBaseInfoUI import Ui_MainWindow
globalAllInfoList:list = []
globalFilesPathList:list = []
globalCompanyList:list = []
globalDrillInfoList:list = []
globalDrillNumList:list = []
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
        self.selectFileButton.clicked.connect(self.setTableViewWithData)
    def getFileOnClicked(self):
        global globalFilesPathList
        global globalCompanyList
        global globalDrillInfoList
        global globalDrillNumList
        global globalDeepList
        global globalPerDayDeepList
        global globalWorkingStateList
        global globalTipsList

        globalFilesPathList.clear()
        globalCompanyList.clear()
        globalDrillInfoList.clear()
        globalDrillNumList.clear()
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
        global globalAllInfoList
        global globalCompanyList
        global globalDrillInfoList
        global globalDrillNumList
        global globalDeepList
        global globalPerDayDeepList
        global globalWorkingStateList
        global globalTipsList

        if len(globalFilesPathList) > 0:
            for i in globalFilesPathList:
                #print(i)
                loadDataFromExcel(i)
        else:
            print('未导入文件！！！！')

    def setTableViewWithData(self):
        global globalAllInfoList
        print(globalAllInfoList)
def loadDataFromExcel(fileNames: str):
    global globalAllInfoList
    global globalCompanyList
    global globalDrillInfoList
    global globalDrillNumList
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
        dataList = np.array(input_table.iloc[3:, 0:])
        # companyList = []
        # print(dataList)
        drillInfoList = []
        drillNumList = []
        deepList = []
        perDayDeepList = []
        workingStateList = []
        tipsList = []
        n = 0
        for i in dataList:
            # drillInfoList.clear()
            # deepList.clear()
            # perDayDeepList.clear()
            # workingStateList.clear()
            # tipsList.clear()
            # 索引出每个不为空的第一行即为新的项目数据行
            if str(i[0]) != 'nan':
                drillInfoList.clear()
                drillNumList.clear()
                deepList.clear()
                perDayDeepList.clear()
                workingStateList.clear()
                tipsList.clear()
                #companyList.append(str(input_table.iloc[n,0]))

                # print(str(i).split())
                drillInfoStrList = str(i).split()

                #正则表达找出是否为队属钻机
                pattern1 = re.compile(r'[-[0-9]+[\u4E00-\u9FA5A-Za-z0-9]+（.*\属）')
                pattern2 = re.compile(r'[-[0-9]+[\u4E00-\u9FA5A-Za-z0-9]+（.*\协）')
                pattern3 = re.compile(r'[-[0-9]+[\u4E00-\u9FA5A-Za-z0-9]+（.*\管）')
                drillInfoStr = str(drillInfoStrList)
                if pattern1.search(drillInfoStr):
                    drillNumStr = pattern1.search(drillInfoStr).group()
                else:
                    if  pattern2.search(drillInfoStr):
                        drillNumStr = pattern2.search(drillInfoStr).group()
                    else:
                        if pattern3.search(drillInfoStr):
                            drillNumStr = pattern3.search(drillInfoStr).group()
                        else:
                            print('未匹配！！！！')
                print(drillNumStr)
                drillNumList.append(drillNumStr)
                #项目名称+施工地点+钻机编号+孔号+设计孔深+井型+孔径+开孔日期
                drillInfoList.append(''.join(drillInfoStrList[2]+'\n'+drillInfoStrList[1]+'\n'+drillInfoStrList[0]))

                # print('钻孔深度：' + str(input_table.iloc[n, 2]) + '(m)')
                deepList.append(str(input_table.iloc[n+3, 2]) + '(m)')

               # print('日进尺：' + str(input_table.iloc[n, 3]) + '(m)')
                perDayDeepList.append(str(input_table.iloc[n+3, 3]) + '(m)')

                #print('工况：' + str(input_table.iloc[n, 5]))
                workingStateList.append('6:00-10:00'+''.join(str(input_table.iloc[n+3, 5]).split()))

                #print('备注：' + str(input_table.iloc[n, 16]))
                tipsList.append(str(input_table.iloc[n, 16]))
            else:
                if n%6 == 1:
                    workingStateList.append('10:00-14:00'+''.join(str(input_table.iloc[n, 5]).split()))
                elif n%6 == 2:
                    workingStateList.append('14:00-18:00'+''.join(str(input_table.iloc[n, 5]).split()))
                elif n%6 == 3:
                    workingStateList.append('18:00-22:00'+''.join(str(input_table.iloc[n, 5]).split()))
                elif n%6 == 4:
                    workingStateList.append('22:00-2:00'+''.join(str(input_table.iloc[n, 5]).split()))
                elif n%6 == 5:
                    workingStateList.append('2:00-6:00'+''.join(str(input_table.iloc[n, 5]).split()))
                    list = [drillInfoList, drillNumList,deepList, perDayDeepList, workingStateList, tipsList]
                    ndArray = np.array(list, dtype='object')
                    globalAllInfoList.append(ndArray)
            n += 1

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
            #print(i)
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
           # print(i)
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
