# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcularFee.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import math
import numpy as np
import pandas as pd
from decimal import localcontext, Decimal, ROUND_HALF_UP
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator,QPixmap,QImage,QDoubleValidator
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(694, 184)
        self.Buy_lineEdit = QtWidgets.QLineEdit(MainForm)
        self.Buy_lineEdit.setGeometry(QtCore.QRect(160, 90, 131, 31))
        self.Buy_lineEdit.setObjectName("Buy_lineEdit")
        self.Buy_lineEdit.setValidator(QDoubleValidator(0,99,2))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Buy_lineEdit.setFont(font)
        
        self.Sell_lineEdit = QtWidgets.QLineEdit(MainForm)
        self.Sell_lineEdit.setGeometry(QtCore.QRect(300, 90, 131, 31))
        self.Sell_lineEdit.setObjectName("Sell_lineEdit")
        self.Sell_lineEdit.setValidator(QDoubleValidator(0,99,2))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sell_lineEdit.setFont(font)
        
        self.NumberofStock_lineEdit = QtWidgets.QLineEdit(MainForm)
        self.NumberofStock_lineEdit.setGeometry(QtCore.QRect(440,90,71,31))
        self.NumberofStock_lineEdit.setObjectName("NumberofStock_lineEdit")
        self.onlyInt = QIntValidator()
        self.NumberofStock_lineEdit.setValidator(self.onlyInt)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumberofStock_lineEdit.setFont(font)
        
        self.Comfirm_button = QtWidgets.QPushButton(MainForm)
        self.Comfirm_button.setGeometry(QtCore.QRect(520, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Comfirm_button.setFont(font)
        self.Comfirm_button.setObjectName("Comfirm_button")
        self.Comfirm_button.clicked.connect(self.CountFee)
        
        self.NumberofStock_label = QtWidgets.QLabel(MainForm)
        self.NumberofStock_label.setGeometry(QtCore.QRect(450, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.NumberofStock_label.setFont(font)
        self.NumberofStock_label.setObjectName("NumberofStock_label")
        
        self.Title_label = QtWidgets.QLabel(MainForm)
        self.Title_label.setGeometry(QtCore.QRect(25, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Title_label.setFont(font)
        self.Title_label.setObjectName("Title_label")
        self.buy_label = QtWidgets.QLabel(MainForm)
        self.buy_label.setGeometry(QtCore.QRect(190, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buy_label.setFont(font)
        self.buy_label.setObjectName("buy_label")
        self.Sell_label = QtWidgets.QLabel(MainForm)
        self.Sell_label.setGeometry(QtCore.QRect(330, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Sell_label.setFont(font)
        self.Sell_label.setObjectName("Sell_label")
        self.DisResult_label = QtWidgets.QLabel(MainForm)
        self.DisResult_label.setGeometry(QtCore.QRect(166, 122, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DisResult_label.setFont(font)
        #self.DisResult_label.setText("")
        self.DisResult_label.setObjectName("DisResult_label")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "台股手續費計算"))
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
        
        """
        BuyPrice = self.Buy_lineEdit.text()
        SellPrice = self.Sell_lineEdit.text()
        NumberofStock = self.NumberofStock_lineEdit.text()
        if BuyPrice and SellPrice and NumberofStock:
            with localcontext() as ctx:
                ctx.rounding = ROUND_HALF_UP
                BuyFee = (Decimal(BuyPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.001425))
                FinalBuyFee = BuyFee.to_integral_value()
                SellFee = (Decimal(SellPrice)*1000)*(Decimal(NumberofStock))*(Decimal(0.004425))
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  




















