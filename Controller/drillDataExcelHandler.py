import sys
import time
import pandas as pd
import numpy as np
import re
import xlwt
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QApplication, QTableWidgetItem, QHeaderView, QMessageBox
from View.ReaderBaseInfoUI import Ui_MainWindow
import pymongo
import copy

globalAllInfoList:list = []
globalFilesPathList:list = []
globalCollectionName:list = []
class window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectFileButton.clicked.connect(self.getFileOnClicked)
        self.selectFileButton.clicked.connect(self.loadBaseData)
        self.selectFileButton.clicked.connect(self.setTableViewWithData)
        self.savePushButton.clicked.connect(self.saveBtnClicked)
        self.mongoDBButton.clicked.connect(self.savedInMongoDB)


    def getFileOnClicked(self):
        global globalFilesPathList
        global globalCollectionName
        global globalAllInfoList
        globalFilesPathList.clear()
        globalCollectionName.clear()
        globalAllInfoList.clear()
        self.dataTableWidget.clearContents()
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
        global globalCollectionName
        if len(globalFilesPathList) > 0:
            for i in globalFilesPathList:
                #print(i)
                patternName = re.compile(r'[0-9]+月+[0-9]+日')
                if patternName.search(i):
                    globalCollectionName.append(patternName.search(i).group())
                else:
                    QMessageBox.information(MainWindow,
                                            '警告！！！',
                                            '请确认文件名中是否存在日期信息')
                    break
            if len(set(globalCollectionName)) == 1:
                print(set(globalCollectionName))
                for i in globalFilesPathList : loadDataFromExcel(i)
                self.timeLabel.setText('2023年'+list(set(globalCollectionName))[0])
            else:
                QMessageBox.information(MainWindow,
                                        '警告！！！',
                                        '请确认所选生产日报是否为同一天！！！')



        else:
            print('未导入文件！！！！')


    def setTableViewWithData(self):
        global globalAllInfoList
        self.dataTableWidget.setColumnCount(6)
        self.dataTableWidget.setRowCount(len(globalAllInfoList))
        n = 0
        while n < len(globalAllInfoList):
            companyItem = QTableWidgetItem(str(globalAllInfoList[n][0][0]))
            drillProjectName = QTableWidgetItem(str(globalAllInfoList[n][1][0]))
            drillNumber = QTableWidgetItem(str(globalAllInfoList[n][2][0]))
            deepItem = QTableWidgetItem(str(globalAllInfoList[n][3][0]))
            perDayDeepItem = QTableWidgetItem(str(globalAllInfoList[n][4][0]))
            workingStateItem = QTableWidgetItem(str(globalAllInfoList[n][5][5]))
            #tipsItem = QTableWidgetItem(str(globalAllInfoList[n][6][0]))

            companyItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            drillProjectName.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            drillNumber.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            deepItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            perDayDeepItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            workingStateItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            #tipsItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            companyItem.setFont(QFont('Times', 8, QFont.Black))
            drillProjectName.setFont(QFont('Times', 8, QFont.Black))
            drillNumber.setFont(QFont('Times', 8, QFont.Black))
            deepItem.setFont(QFont('Times', 8, QFont.Black))
            perDayDeepItem.setFont(QFont('Times', 8, QFont.Black))
            workingStateItem.setFont(QFont('Times', 8, QFont.Black))
            #tipsItem.setFont(QFont('Times', 8, QFont.Black))

            self.dataTableWidget.setItem(n, 0, companyItem)
            self.dataTableWidget.setItem(n, 1,drillProjectName)
            self.dataTableWidget.setItem(n, 2, drillNumber)
            self.dataTableWidget.setItem(n, 3, deepItem)
            self.dataTableWidget.setItem(n, 4, perDayDeepItem)
            self.dataTableWidget.setItem(n, 5, workingStateItem)
            #self.dataTableWidget.setItem(n, 6, tipsItem)
            n += 1
        self.dataTableWidget.setHorizontalHeaderLabels(
            ['公司', '项目名称', '钻机编号', '当前深度', '昨日下深', '工况'])
        #self.dataTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.dataTableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")
        self.dataTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.dataTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.dataTableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        QApplication.processEvents()

    def saveBtnClicked(self):
        # 创建一个Workbook对象 编码encoding
        # Excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
        # 添加一个sheet工作表、sheet名命名为Sheet1、cell_overwrite_ok=True允许覆盖写
        # table = Excel.add_sheet('Sheet1', cell_overwrite_ok=True)

        rowCount = self.dataTableWidget.rowCount()
        columnCount = self.dataTableWidget.columnCount()
        # i = 0
        # while i < columnCount:
        #     j = 0
        #     while j < rowCount:
        #         table.write(j, i, self.dataTableWidget.item(j, i).text())
        #         j = j + 1
        #     i = i + 1
        row_num = 0  # 记录写入行数
        col_list = []  # 记录每行宽度
        # 个人信息：姓名，性别，年龄，手机号，固定电话，邮箱

        # 创建一个Workbook对象
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)
        # 创建一个sheet对象
        sheet = book.add_sheet('drillProject', cell_overwrite_ok=True)
        col_num = [0 for x in range(0, rowCount)]
        # 写入数据
        for i in range(0, rowCount-1):
            for j in range(0, columnCount-1):
                sheet.write(i, j, self.dataTableWidget.item(i, j).text())
                col_num[j] = len(self.dataTableWidget.item(i, j).text().encode('gb18030'))  # 计算每列值的大小
            col_list.append(copy.copy(col_num))  # 记录一行每列写入的长度
            row_num += 1
        # 获取每列最大宽度
        col_max_num = get_max_col(col_list)
        # 设置自适应列宽
        for i in range(0, len(col_max_num)):
            # 256*字符数得到excel列宽,为了不显得特别紧凑添加两个字符宽度
            sheet.col(i).width = 256 * (col_max_num[i] + 2)
        # 保存excel文件
        book.save(r'C:\Users\18637\Desktop\院属钻机生产日报.xlsx')

    def savedInMongoDB(self):
        global globalAllInfoList
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.drillProject
        collection = db.drillProjectItems
        rowCount = self.dataTableWidget.rowCount()
        # columnCount = self.dataTableWidget.columnCount()
        i = 0
        while i < rowCount:
            # j = 0
            # while j < columnCount:
            #     # drillProjectItem = ['company':]
            #     j = j + 1
            keysList = ['company','projectName','drillId','currentDeep','lastDayDeep','workState']
            print(globalAllInfoList[i])
            projectItem = []
            for infoList in globalAllInfoList[i]:
                infoListStr = ''.join(infoList)
                projectItem.append(infoListStr)
                print(projectItem)
            drillProjectItem =  dict(zip(keysList,projectItem))
            print(drillProjectItem)
            result = collection.insert_one(drillProjectItem)
            print(result)
            i = i + 1
        QMessageBox.information(MainWindow,'提示：','成功写入数据库！！！')
def loadDataFromExcel(fileNames: str):
    global globalAllInfoList
    path_openfile_name = fileNames

    if path_openfile_name != '':
        input_table = pd.read_excel(path_openfile_name)

        # input_table_rows = input_table.shape[0]
        # input_table_colunms = input_table.shape[1]
        # dataDictKey = input_table.columns.values.tolist()
        # print(np.List(input_table.iloc[:,1]))
        dataList = np.array(input_table.iloc[3:, 0:])
        companyList = []
        # print(dataList)
        drillInfoList = []
        drillProjectNameList = []
        drillNumList = []
        deepList = []
        perDayDeepList = []
        workingStateList = []
        tipsList = []
        m = 0
        if 0 < len(dataList):
            for i in dataList:
                # 索引出每个不为空的第一行即为新的项目数据行
                if str(i[0]) != 'nan':
                    drillInfoList.clear()
                    companyList.clear()
                    drillProjectNameList.clear()
                    drillNumList.clear()
                    deepList.clear()
                    perDayDeepList.clear()
                    workingStateList.clear()
                    tipsList.clear()

                    companyList.append(str(i[0]))
                    drillInfoStrList = str(i[1]).split()
                    drillInfoStr = str(drillInfoStrList)
                    drillNameStr = str(i[1]).split()[0]
                    # 正则表达找出是项目名称
                    # patternName = re.compile(r'^[\u4e00-\u9fa5]+')
                    # if patternName.search(drillInfoStr):
                    #     drillNameStr = patternName.search(drillInfoStr).group()
                    # else:
                    #     drillNameStr = 'xxxx'
                    #     print('未找到项目名称！！！')
                    drillProjectNameList.append(drillNameStr)
                    print(drillNameStr)
                    # 正则表达找出是否为队属钻机
                    patternNum = re.compile(r'[-[0-9]+[\u4E00-\u9FA5A-Za-z0-9]+（.*\属）')
                    patternNum1 = re.compile(r'[-[0-9]+[\u4E00-\u9FA5A-Za-z0-9]+（.*\协）')
                    patternNum2 = re.compile(r'[-[0-9]+[\u4E00-\u9FA5A-Za-z0-9]+（.*\管）')

                    if patternNum.search(drillInfoStr):
                        drillNumStr = patternNum.search(drillInfoStr).group()
                    else:
                        if patternNum1.search(drillInfoStr):
                            drillNumStr = patternNum1.search(drillInfoStr).group()
                        else:
                            if patternNum2.search(drillInfoStr):
                                drillNumStr = patternNum2.search(drillInfoStr).group()
                            else:
                                drillNumStr = 'xxxx'
                                print('未匹配！！！！')
                    print(drillNumStr)
                    if '队管' in drillNumStr:
                        drillNumStr = drillNumStr.replace('管', '属')
                    drillNumList.append(drillNumStr)
                    # 项目名称+施工地点+钻机编号+孔号+设计孔深+井型+孔径+开孔日期
                    if len(drillInfoStrList)>3:
                        drillInfoList.append(
                            ''.join(drillInfoStrList[2] + '\n' + drillInfoStrList[1] + '\n' + drillInfoStrList[0]))
                    else:
                        QMessageBox.information(MainWindow,
                                                '警告！！',
                                                '数据源不合法！！请选择生产日报！！')
                        break
                    # print('钻孔深度：' + str(input_table.iloc[n, 2]) + '(m)')
                    deepList.append(str(input_table.iloc[m + 3, 2]) + '(m)')

                    # print('日进尺：' + str(input_table.iloc[m, 3]) + '(m)')
                    perDayDeepList.append(str(input_table.iloc[m + 3, 3]) + '(m)')

                    # print('工况：' + str(input_table.iloc[m, 5]))
                    workingStateList.append('6:00-10:00' + ''.join(str(input_table.iloc[m + 3, 5]).split()))

                    # print('备注：' + str(input_table.iloc[m, 16]))
                    tipsList.append(str(input_table.iloc[m, 16]))
                else:
                    if m % 6 == 1:
                        workingStateList.append('10:00-14:00' + ''.join(str(input_table.iloc[m, 5]).split()))
                    elif m % 6 == 2:
                        workingStateList.append('14:00-18:00' + ''.join(str(input_table.iloc[m, 5]).split()))
                    elif m % 6 == 3:
                        workingStateList.append('18:00-22:00' + ''.join(str(input_table.iloc[m, 5]).split()))
                    elif m % 6 == 4:
                        workingStateList.append('22:00-2:00' + ''.join(str(input_table.iloc[m, 5]).split()))
                    elif m % 6 == 5:
                        workingStateList.append('2:00-6:00' + ''.join(str(input_table.iloc[m, 5]).split()))
                        ndList1 = [companyList.copy(), drillProjectNameList.copy(), drillNumList.copy(), deepList.copy(), perDayDeepList.copy(),
                                workingStateList.copy(), tipsList.copy()]
                        ndArray = np.array(ndList1, dtype='object')

                        if '外协' not in drillNumStr and '队属' in drillNumStr:
                            globalAllInfoList.append(ndArray)
                        else:
                            print('数据不合法哦！！！')

                m += 1
            print(globalAllInfoList)
        else:
            QMessageBox.information(MainWindow,
                                    '警告！！',
                                    '数据源不合法！！请选择生产日报！！')

    else:
        QMessageBox.information(MainWindow,
                                '警告！！',
                                '你未选择任何文件！！')

# 获取每列所占用的最大列宽
def get_max_col(max_list):
    line_list = []
    # i表示行，j代表列
    for j in range(len(max_list[0])):
        line_num = []
        for i in range(len(max_list)):
            line_num.append(max_list[i][j])  # 将每列的宽度存入line_num
        line_list.append(max(line_num))  # 将每列最大宽度存入line_list
    return line_list
# def write_excel():
#     row_num = 0  # 记录写入行数
#     col_list = []  # 记录每行宽度
#     # 个人信息：姓名，性别，年龄，手机号，固定电话，邮箱
#
#     # 创建一个Workbook对象
#     book = xlwt.Workbook(encoding="utf-8",style_compression=0)
#     # 创建一个sheet对象
#     sheet = book.add_sheet('person_msg', cell_overwrite_ok=True)
#     col_num = [0 for x in range(0, len(data))]
#     # 写入数据
#     for i in range(0, len(data)):
#         for j in range(0, len(data[i])):
#             sheet.write(row_num, j, data[i][j])
#             col_num[j] = len(data[i][j].encode('gb18030')) # 计算每列值的大小
#         col_list.append(copy.copy(col_num))  # 记录一行每列写入的长度
#         row_num += 1
#     # 获取每列最大宽度
#     col_max_num = get_max_col(col_list)
#     # 设置自适应列宽
#     for i in range(0, len(col_max_num)):
#         # 256*字符数得到excel列宽,为了不显得特别紧凑添加两个字符宽度
#         sheet.col(i).width = 256 * (col_max_num[i] + 2)
#     # 保存excel文件
#     book.save('person_msg.xls')


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

