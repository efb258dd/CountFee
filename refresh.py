# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refresh.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,QtTest
import time
import numpy as np
import pandas as pd
import sys
import random
import logging
import requests
from bs4 import BeautifulSoup
import hashlib
from CalcularFee import Ui_MainForm

class Ui_MainForm1(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(400, 265)
        self.status_label = QtWidgets.QLabel(MainForm)
        self.status_label.setGeometry(QtCore.QRect(135, 140, 241, 161))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        
        self.Refresh_label = QtWidgets.QLabel(MainForm)
        self.Refresh_label.setGeometry(QtCore.QRect(50, 51, 241, 161))
        self.Refresh_label.setObjectName("Refresh_label")
        
        self.gif = QtGui.QMovie('loadingBar.gif')
        self.Refresh_label.setMovie(self.gif)
        self.gif.start()
        
        loop = QtCore.QEventLoop()
        self.time = QtCore.QTimer()
        self.time.singleShot(8000,loop.quit)
        self.time.singleShot(4000,self.Checkfile)
        
        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)
        
    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "更新"))
        self.status_label.setText(_translate("MainForm","確認檔案中...."))
        
    def Universal_Cralwer(self):
        """
        Through the website to scrap table of Securities information
        """
        url = 'https://goodideamin.com.tw/blog/post/115043712'
        headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
                      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
                      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
                      "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
                      "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
                      "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]
        random_list = random.choice(headerlist)
        headers = {'user-agent': random_list}
        r = requests.get(url,headers=headers)
        r.encoding = 'utf_8_sig'
        soup = BeautifulSoup(r.text,'lxml')
        table = soup.find_all('tbody')
        html_table = table[0]
        #tr = tab.find_all('tr')
        #td = tab.find_all('td')
        return html_table
    
    def Creatmd5(self,html_table):
        """
        Encrypt the website table
        """
        m = hashlib.md5()
        m.update(str(html_table).encode(encoding='UTF-8'))
        h = m.hexdigest()
        return h
    
    def CreatCsv(self,html_table):
        """
        Transform website data to dataframe and save to csv
        """
        column1 = []
        column2 = []
        column3 = []
        column4 = []
        column5 = []
        column6 = []
        column7 = []
        i = 0
        for td in html_table.find_all('td'):
            if i ==0:
                column1.append(td.getText())
                i+=1
            elif i==1:
                column2.append(td.getText())
                i+=1
            elif i==2:
                column3.append(td.getText())
                i+=1
            elif i==3:
                column4.append(td.getText())
                i+=1
            elif i==4:
                column5.append(td.getText())
                i+=1
            elif i==5:
                column6.append(td.getText())
                i+=1
            elif i==6:
                column7.append(td.getText())
                i=0
        
        Securities = {column1[0]:column1,column2[0]:column2
                      ,column3[0]:column3,column4[0]:column4
                      ,column5[0]:column5,column6[0]:column6
                      ,column7[0]:column7}
        SetoCsv = pd.DataFrame(Securities)
        SetoCsv.drop(SetoCsv.index[0],inplace=True)
        SetoCsv.replace(to_replace = r'^\s*$',value = np.nan,regex=True,inplace=True)
        SetoCsv = SetoCsv.dropna(how='all')
        SetoCsv.to_csv('./SetoCsv.csv',encoding='utf_8_sig',index=0)
        return SetoCsv
        
    def Checkfile(self):
        """
        Check file does exits or not
        """
        import os
        csvpath = './SetoCsv.csv'
        md5path = './md5.txt'
        
        if os.path.isfile(csvpath) and os.path.isfile(md5path):
            html_table = self.Universal_Cralwer()
            h = self.Creatmd5(html_table)
            self.status_label.setText("檔案更新中...")
            with open('./md5.txt','r') as f:
                exit_md5 = f.read()
                if h == exit_md5:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_MainForm()
                    self.ui.setupUi(self.window)
                    self.window.show()
                    MainWindow.close()
                else:
                    self.CreatCsv(html_table)
                    with open('./md5.txt','w') as f:
                        f.write(h)
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_MainForm()
                    self.ui.setupUi(self.window)
                    self.window.show()
                    MainWindow.close()      
        else:
            self.status_label.setText("檔案更新中...")
            html_table = self.Universal_Cralwer()
            self.CreatCsv(html_table)
            h = self.Creatmd5(html_table)
            with open("./md5.txt","w") as f:
                f.write(h)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainForm()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.close()
            
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_refresh = Ui_MainForm1()
    ui_refresh.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())  

    
    