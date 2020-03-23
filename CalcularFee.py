# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcularFee.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import math
import requests
import numpy as np
import pandas as pd
import random
from bs4 import BeautifulSoup
from decimal import localcontext, Decimal, ROUND_HALF_UP
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator,QPixmap,QImage,QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem,QLCDNumber


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(640, 223)
        self.Buy_lineEdit = QtWidgets.QLineEdit(MainForm)
        self.Buy_lineEdit.setGeometry(QtCore.QRect(150, 90, 131, 31))
        self.Buy_lineEdit.setObjectName("Buy_lineEdit")
        self.Buy_lineEdit.setValidator(QDoubleValidator(0,99,2))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Buy_lineEdit.setFont(font)
        
        self.Sell_lineEdit = QtWidgets.QLineEdit(MainForm)
        self.Sell_lineEdit.setGeometry(QtCore.QRect(290, 90, 131, 31))
        self.Sell_lineEdit.setObjectName("Sell_lineEdit")
        self.Sell_lineEdit.setValidator(QDoubleValidator(0,99,2))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sell_lineEdit.setFont(font)
        
        self.NumberofStock_lineEdit = QtWidgets.QLineEdit(MainForm)
        self.NumberofStock_lineEdit.setGeometry(QtCore.QRect(430,90,71,31))
        self.NumberofStock_lineEdit.setObjectName("NumberofStock_lineEdit")
        self.onlyInt = QIntValidator()
        self.NumberofStock_lineEdit.setValidator(self.onlyInt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumberofStock_lineEdit.setFont(font)
        
        self.Comfirm_button = QtWidgets.QPushButton(MainForm)
        self.Comfirm_button.setGeometry(QtCore.QRect(510, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Comfirm_button.setFont(font)
        self.Comfirm_button.setObjectName("Comfirm_button")
        self.Comfirm_button.clicked.connect(self.CountFee)
        
        self.NumberofStock_label = QtWidgets.QLabel(MainForm)
        self.NumberofStock_label.setGeometry(QtCore.QRect(440, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.NumberofStock_label.setFont(font)
        self.NumberofStock_label.setObjectName("NumberofStock_label")
        
        self.ChoiceSecurities_combobox = QtWidgets.QComboBox(MainForm)
        self.ChoiceSecurities_combobox.setGeometry(QtCore.QRect(150, 20, 471, 31))
        font = self.ChoiceSecurities_combobox.font()
        font.setPointSize(20)
        self.ChoiceSecurities_combobox.setFont(font)
        self.ChoiceSecurities_combobox.setObjectName("ChoiceSecurities_combobox")
        self.ChoiceSecurities_combobox.activated[str].connect(self.SwitchSecurities)
        self.ChoiceSecurities_combobox.addItems(self.getNameData())
        
        self.Securities_label = QtWidgets.QLabel(MainForm)
        self.Securities_label.setGeometry(QtCore.QRect(60,20,81,31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Securities_label.setFont(font)
        self.Securities_label.setObjectName("Securities_label")
        
        self.Title_label = QtWidgets.QLabel(MainForm)
        self.Title_label.setGeometry(QtCore.QRect(15, 122, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Title_label.setFont(font)
        self.Title_label.setObjectName("Title_label")
        
        self.buy_label = QtWidgets.QLabel(MainForm)
        self.buy_label.setGeometry(QtCore.QRect(180, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buy_label.setFont(font)
        self.buy_label.setObjectName("buy_label")
        
        self.Sell_label = QtWidgets.QLabel(MainForm)
        self.Sell_label.setGeometry(QtCore.QRect(320, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Sell_label.setFont(font)
        self.Sell_label.setObjectName("Sell_label")
        
        self.DisResult_label = QtWidgets.QLabel(MainForm)
        self.DisResult_label.setGeometry(QtCore.QRect(156, 122, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DisResult_label.setFont(font)
        self.DisResult_label.setObjectName("DisResult_label")
        
        self.Nowadays_lcdNumber = QtWidgets.QLCDNumber(MainForm)
        self.Nowadays_lcdNumber.setGeometry(QtCore.QRect(230, 170, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.Nowadays_lcdNumber.setFont(font)
        self.Nowadays_lcdNumber.setObjectName("Nowadays_lcdNumber")
        self.Nowadays_lcdNumber.setDigitCount(19)
        self.Nowadays_lcdNumber.setMode(QLCDNumber.Dec)
        self.Nowadays_lcdNumber.setStyleSheet("background-siliver: yellow;color:black;")
        Datetime = QtCore.QDateTime.currentDateTime()
        self.Nowadays_lcdNumber.display(Datetime.toString('yyyy-MM-dd hh:mm:ss'))
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.fortime)
        self.time.start(1000)
        
        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "台股手續費計算"))
        self.Securities_label.setText(_translate("MainForm", "證券商:"))
        self.Comfirm_button.setText(_translate("MainForm", "確認"))
        self.Title_label.setText(_translate("MainForm", "獲利or賠售:"))
        self.buy_label.setText(_translate("MainForm", "買進價"))
        self.Sell_label.setText(_translate("MainForm", "賣出價"))
        self.NumberofStock_label.setText(_translate("MainForm","張數"))
        self.Buy_lineEdit.setPlaceholderText(_translate("MainForm", "輸入買進價"))
        self.Sell_lineEdit.setPlaceholderText(_translate("MainForm", "輸入賣出價"))
        self.NumberofStock_lineEdit.setPlaceholderText(_translate("MainForm","輸入張數"))
        
    def CountFee(self,MainForm):
        """
        First edition:
        Simply count the fee of Taiwanese stock without apply discount.
        Second edition:
        Plus other functions, likes choice Securities and time. 
        """
        BuyPrice = self.Buy_lineEdit.text()
        SellPrice = self.Sell_lineEdit.text()
        NumberofStock = self.NumberofStock_lineEdit.text()
        try:
            discount11 = self.value
            if BuyPrice and SellPrice and NumberofStock:
                with localcontext() as ctx:
                    ctx.rounding = ROUND_HALF_UP
                    BuyFee = (Decimal(BuyPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.001425))*(Decimal(discount11))
                    FinalBuyFee = BuyFee.to_integral_value()
                    SellFee = ((Decimal(SellPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.001425))*(Decimal(discount11)))+((Decimal(SellPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.003)))
                    FinalSellFee = SellFee.to_integral_value()
                    FinalFee = FinalBuyFee + FinalSellFee
                    FinalEarn = ((Decimal(SellPrice)*1000)*(Decimal(NumberofStock)))-((Decimal(BuyPrice)*1000)*(Decimal(NumberofStock)))-FinalFee
                    if FinalEarn >0:
                        self.DisResult_label.setText("+ "+str(format(FinalEarn,',')))
                        self.DisResult_label.setStyleSheet('color:red')
                        self.Buy_lineEdit.clear()
                        self.Sell_lineEdit.clear()
                        self.NumberofStock_lineEdit.clear()
                    elif FinalEarn == 0:
                        self.DisResult_label.setText(str(format(FinalEarn,',')))
                        self.Buy_lineEdit.clear()
                        self.Sell_lineEdit.clear()
                        self.NumberofStock_lineEdit.clear()
                    else:
                        self.DisResult_label.setText(str(format(FinalEarn,',')))
                        self.DisResult_label.setStyleSheet('color:green')
                        self.Buy_lineEdit.clear()
                        self.Sell_lineEdit.clear()
                        self.NumberofStock_lineEdit.clear()
            else:
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
                error_dialog.setText("請輸入買進價、賣出價與股票張數!!!")
                error_dialog.addButton(QtWidgets.QMessageBox.Ok)
                error_dialog.exec()
        except:
            self.value = 1
            discount11 = self.value
            if BuyPrice and SellPrice and NumberofStock:
                with localcontext() as ctx:
                    ctx.rounding = ROUND_HALF_UP
                    BuyFee = (Decimal(BuyPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.001425))*(Decimal(discount11))
                    FinalBuyFee = BuyFee.to_integral_value()
                    SellFee = ((Decimal(SellPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.001425))*(Decimal(discount11)))+((Decimal(SellPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.003)))
                    FinalSellFee = SellFee.to_integral_value()
                    FinalFee = FinalBuyFee + FinalSellFee
                    FinalEarn = ((Decimal(SellPrice)*1000)*(Decimal(NumberofStock)))-((Decimal(BuyPrice)*1000)*(Decimal(NumberofStock)))-FinalFee
                    if FinalEarn >0:
                        self.DisResult_label.setText("+ "+str(format(FinalEarn,',')))
                        self.DisResult_label.setStyleSheet('color:red')
                        self.Buy_lineEdit.clear()
                        self.Sell_lineEdit.clear()
                        self.NumberofStock_lineEdit.clear()
                    elif FinalEarn == 0:
                        self.DisResult_label.setText(str(format(FinalEarn,',')))
                        self.Buy_lineEdit.clear()
                        self.Sell_lineEdit.clear()
                        self.NumberofStock_lineEdit.clear()
                    else:
                        self.DisResult_label.setText(str(format(FinalEarn,',')))
                        self.DisResult_label.setStyleSheet('color:green')
                        self.Buy_lineEdit.clear()
                        self.Sell_lineEdit.clear()
                        self.NumberofStock_lineEdit.clear()
            else:
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
                error_dialog.setText("請輸入買進價、賣出價與股票張數!!!")
                error_dialog.addButton(QtWidgets.QMessageBox.Ok)
                error_dialog.exec()

    def fortime(self):
        Datetime = QtCore.QDateTime.currentDateTime()
        self.Nowadays_lcdNumber.display(Datetime.toString('yyyy-MM-dd hh:mm:ss'))
    
    def getNameData(self):
        csvpath = './SetoCsv.csv'
        df = pd.read_csv(csvpath)
        df1 = pd.DataFrame(df)
        namelist = ['請選擇券商','不選擇券商']
        for name in df1['券商']:
            namelist.append(name)
        return namelist
        
    def SwitchSecurities(self,MainForm):
        if self.ChoiceSecurities_combobox.currentText() == '不選擇券商':
            SecuritiesName = self.ChoiceSecurities_combobox.currentText()
            self.value = 1
            #print("未選擇券商，故手續費未折扣")
        else:
            SecuritiesName = self.ChoiceSecurities_combobox.currentText()
            dict_SecuritiesName_discount = self.Creatdict()
            self.value = dict_SecuritiesName_discount.get(self.ChoiceSecurities_combobox.currentText())
            #print(SecuritiesName+" :"+self.value+" 折扣")
            
    def Creatdict(self):
        import re
        csvpath = './SetoCsv.csv'
        dict_df = pd.read_csv(csvpath)
        dict_df1 = pd.DataFrame(dict_df)
        discountlist = []
        for i in range(len(dict_df1)):
            newdiscount = re.findall(r'-?\d+\.?\d*e?-?\d*?',dict_df1['折扣'][i])[0]
            a = round(float(newdiscount)/10,3)
            b = str(a)
            discountlist.append(b)
        dict_df1['折扣'] = discountlist
        dictofdf1 = dict_df1.set_index('券商').to_dict()['折扣']
        return dictofdf1
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_Fee = Ui_MainForm()
    ui_Fee.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())  




















