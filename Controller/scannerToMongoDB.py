import sys
import os
import time
import datetime
import pandas as pd
import numpy as np
import re
import pymongo


globalAllInfoList:list = []
globalFilesPathList:list = []
globalCollectionName:list = []

def saveDataToMongoDB():
    global globalFilesPathList
    global globalCollectionName
    globalAllInfoList.clear()
    globalCollectionName.clear()
    if len(globalFilesPathList) > 0:
        for i in globalFilesPathList:
            #print(i)
            patternName = re.compile(r'[0-9]+月+[0-9]+日')
            if patternName.search(i):
                print("2023/"+patternName.search(i).group().replace('日','').replace('月','/'))
                date = datetime.datetime.strptime("2023/"+patternName.search(i).group().replace('日','').replace('月','/'), "%Y/%m/%d")
                dateStr = date.strftime("%Y/%m/%d")
                globalCollectionName.append(dateStr)
                loadDataFromExcel(i)
                savedInMongoDB(dateStr)
            else:
                print('文件命名无日期相关信息！！！！！！！')
                break
    print('全部数据导入成功！！！！')



def savedInMongoDB(dateStr):
    global globalAllInfoList
    global globalCollectionName
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    if len(globalCollectionName) > 0:
        collectionName = globalCollectionName[0]
        collection = db[dateStr]
        rowCount = len(globalAllInfoList)
        # columnCount = self.dataTableWidget.columnCount()
        i = 0
        while i < rowCount:
            # j = 0
            # while j < columnCount:
            #     # drillProjectItem = ['company':]
            #     j = j + 1
            keysList = ['company', 'projectName', 'drillId', 'currentDeep', 'lastDayDeep', 'workState']
            print(globalAllInfoList[i])
            projectItem = []
            for infoList in globalAllInfoList[i]:
                infoListStr = ''.join(infoList)
                projectItem.append(infoListStr)
                print(projectItem)
            drillProjectItem = dict(zip(keysList, projectItem))
            print(drillProjectItem)
            result = collection.update_one({"drillId":drillProjectItem["drillId"]},{"$set":drillProjectItem},upsert=True)
            print(result)
            i = i + 1
        print('成功写入数据库！！！')
    else:
        print('数据源选择有误，无法写入数据库！！！')

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
                    drillNumStr.replace('（','(')
                    drillNumStr.replace('）',')')
                    if '队管' in drillNumStr:
                        drillNumStr = drillNumStr.replace('管', '属')
                    drillNumList.append(drillNumStr)
                    # 项目名称+施工地点+钻机编号+孔号+设计孔深+井型+孔径+开孔日期
                    if len(drillInfoStrList)>3:
                        drillInfoList.append(
                            ''.join(drillInfoStrList[2] + '\n' + drillInfoStrList[1] + '\n' + drillInfoStrList[0]))
                    else:
                        print('数据源不合法！！请选择生产日报！！')
                        break
                    # print('钻孔深度：' + str(input_table.iloc[n, 2]) + '(m)')
                    deepList.append(str(input_table.iloc[m + 3, 2]) + '(m)')

                    # print('日进尺：' + str(input_table.iloc[m, 3]) + '(m)')
                    perDayDeepList.append(str(input_table.iloc[m + 3, 3]) + '(m)')

                    # print('工况：' + str(input_table.iloc[m, 5]))
                    workingStateList.append('6:00-10:00' + ''.join(str(input_table.iloc[m + 3, 5]).split()))

                    # print('备注：' + str(input_table.iloc[m, 16]))
                    tipsList.append(str(input_table.iloc[m + 3, 16]))
                else:
                    if m % 6 == 1:
                        workingStateList.append('10:00-14:00' + ''.join(str(input_table.iloc[m+3, 5]).split()))
                    elif m % 6 == 2:
                        workingStateList.append('14:00-18:00' + ''.join(str(input_table.iloc[m+3, 5]).split()))
                    elif m % 6 == 3:
                        workingStateList.append('18:00-22:00' + ''.join(str(input_table.iloc[m+3, 5]).split()))
                    elif m % 6 == 4:
                        workingStateList.append('22:00-2:00' + ''.join(str(input_table.iloc[m+3, 5]).split()))
                    elif m % 6 == 5:
                        workingStateList.append('2:00-6:00' + ''.join(str(input_table.iloc[m+3, 5]).split()))
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
            print('Error!')

    else:
        print('Error!')

def scannerAllFolder(pathName):
    global globalFilesPathList
    if os.path.exists(pathName):
        filelist = os.listdir(pathName)
        for f in filelist:
            f = os.path.join(pathName, f)
            if os.path.isdir(f):
                scannerAllFolder(f)
            else:
                dirname = os.path.dirname(f)
                baseName = os.path.basename(f)
                if dirname.endswith(os.sep):
                    globalFilesPathList.append(dirname + baseName)
                else:
                    globalFilesPathList.append(dirname + os.sep + baseName)

if __name__ == '__main__':
    #loadDataFromExcel('1')
    pathName = 'C:\\Users\\18637\\Desktop\\生产日报\\2023'
    scannerAllFolder(pathName)
    if len(globalFilesPathList)>0:
        for f in globalFilesPathList:
            print(f)
    else:
        print('无文件！！！')

    saveDataToMongoDB()
