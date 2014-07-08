#/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = 'Cristobal Lopez Silla'

import sys
import platform

from math import *
import math as math
from decimal import Decimal, getcontext

import calculator_ui

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

num = 0.0
n = 0.0
newNum = 0.0
sumAll = 0.0
operator = ''

opVar = False
sumIt = 0

class QCalculator(QDialog, calculator_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(QCalculator, self).__init__(parent)
        self.setupUi(self)
        QApplication.setStyle('Fusion')

        nums = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine, self.pi, self.enumber, self.goldnumber]
        operations = [self.sum, self.subtract, self.product, self.div, self.mod, self.pow, self.nroot, self.combinatorial, self.permutation]
        spoperations = [self.cubicroot, self.sqrt, self.percentage, self.factorial, self.inverse, self.powerof10, self.log, self.powerofe, self.logn, self.sin, self.cos, self.tan, self.asin, self.acos, self.atan, self.sec, self.cosec, self.cotg, self.sinh, self.cosh, self.tanh]
        buttons = nums + operations + spoperations + [self.Exe, self.decimal, self.plus_minus, self.butC, self.butCE, self.Del, self.Degrees]

        self.myCss(buttons)

        self.myConections(nums, operations, spoperations)


    def myConections(self, nums, operations, spoperations):
        for i in nums:
            i.clicked.connect(self.numbers)

        self.decimal.clicked.connect(self.decimalClicked)
        for i in operations:
            i.clicked.connect(self.Operator)

        for i in spoperations:
            i.clicked.connect(self.SpecialOperator)

        self.Exe.clicked.connect(self.Equal)
        self.plus_minus.clicked.connect(self.plusMinus)
        self.butC.clicked.connect(self.Clear)
        self.butCE.clicked.connect(self.ClearE)
        self.Del.clicked.connect(self.Delete)

        self.Degrees.clicked.connect(self.grados)


        self.About.clicked.connect(self.MsgBox)

    def grados(self):
        sender = self.sender()
        operator = sender.text()
        num = self.lineEdit.text()
        text = ('{0} \u00b0 {1} \u02bc {2} \u02ee').format(self.toDegrees(num)[0], self.toDegrees(num)[1], self.toDegrees(num)[2])
        self.lineEdit.setText(text)


    def MsgBox(self):
        qmsgBox = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qmsgBox.setWindowIcon(icon)
        qmsgBox.setStyleSheet('QMessageBox {background-color: #2b5b84; color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        QMessageBox.about(qmsgBox, 'SuperPyQtCalculator',
            '''<html><head></head><body><font color='white'><p><b>SuperPyQtCalculator</b></p>
            <p><b>Version:</b> {0}</p>
            <p><b>Author: </b> {1}</p>
            <p>High School Mathematician Teacher.</p>
            <p><b>Web:</b></font><a href='www.linuxmusica.com'><font color='black'>Linux Music 3.0</font></a></p>
            <font color='white'><p><b>Email: </b>lopeztobal@gmail.com</p>
            <p><b>Copyright:</b>  &copy; 2014 Qtrac Ltd.
            All rights reserved.
            <p>This application can be used to calculate
            simple math science operations.</p>
            <p><b>You are using:</b></p>
            <p>Python {2} - Qt {3} - PyQt {4} on {5}</p></font></body></html>'''.format(
            __version__, __author__, platform.python_version(),
            QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))

    def myCss(self, buttons):
        f = open('css/calculator.css', 'r')
        self.styleData = f.read()
        f.close()
        for i in buttons:
            i.setStyleSheet(self.styleData)
        self.lineEdit.setStyleSheet(self.styleData)
        self.setStyleSheet(self.styleData)

    def numbers(self):
        global num
        global newNum
        global opVar

        sender = self.sender()

        newNum = sender.text()
        gold = (1.0 + math.sqrt(5.0)) / 2.0

        if opVar == False:
            if newNum == '\u212e':
                self.lineEdit.setText(self.lineEdit.text() + str(Decimal(math.e)))
            elif newNum == '\u03c0':
                self.lineEdit.setText(self.lineEdit.text() + str(Decimal(math.pi)))
            elif newNum == '\u03c6':
                self.lineEdit.setText(self.lineEdit.text() + str(Decimal(gold)))
            else:
                self.lineEdit.setText(self.lineEdit.text() + newNum)
        else:
            if newNum == '\u212e':
                self.lineEdit.setText(str(Decimal(math.e)))
            elif newNum == '\u03c0':
                self.lineEdit.setText(str(Decimal(math.pi)))
            elif newNum == '\u03c6':
                self.lineEdit.setText(str(Decimal(gold)))
            else:
                self.lineEdit.setText(newNum)
            opVar = False

    def decimalClicked(self):
        if '.' not in self.lineEdit.text():
            self.lineEdit.setText(self.lineEdit.text() + '.')

    def plusMinus(self):
        if '-' not in self.lineEdit.text():
            self.lineEdit.setText('-' + self.lineEdit.text())

    def Operator(self):
        global num, opVar, operator, sumIt
        sumIt += 1
        if sumIt > 1:
            self.Equal()
        num = self.lineEdit.text()
        sender = self.sender()
        operator = sender.text()
        opVar = True

    def Equal(self):
        global num, newNum, sumAll, operator, opVar, sumIt
        sumIt = 0
        newNum = self.lineEdit.text()

        if operator == '+':
            sumAll = Decimal(num) + Decimal(newNum)
        elif operator == '−':
            sumAll = Decimal(num) - Decimal(newNum)
        elif operator == '\u00f7':
            try:
                sumAll = Decimal(num) / Decimal(newNum)
            except ZeroDivisionError:
                sumAll = 'Error. Divide by zero.'
        elif operator == 'Mod':
            try:
                sumAll = Decimal(math.fmod(Decimal(num), Decimal(newNum)))
            except ValueError:
                sumAll = 'Error. Divide by zero.'
        elif operator == '\u00d7':
            sumAll = Decimal(num) * Decimal(newNum)
        elif operator == 'x\u207f':
            sumAll = Decimal(pow(Decimal(num), Decimal(newNum)))
        if operator == '\u207f\u221a':
            try:
                sumAll = Decimal(pow(Decimal(newNum), Decimal(1) / Decimal(num)))
            except ValueError:
                sumAll = 'Math Error. Negative numbers are not valid.'
        if operator == 'nCr':
            num = Decimal(num)
            newNum = Decimal(newNum)
            try:
                denominator = Decimal((math.factorial(newNum) * math.factorial(num -newNum)))
                sumAll = math.factorial(num) / denominator
            except ValueError:
                sumAll = 'Math Error. Negative numbers are not valid.'
        if operator == 'nPr':
            num = Decimal(num)
            newNum = Decimal(newNum)
            try:
                denominator = Decimal(math.factorial(num -newNum))
                sumAll = math.factorial(num) / denominator
            except ValueError:
                sumAll = 'Math Error. Negative numbers are not valid.'
        self.lineEdit.setText(str(sumAll))
        opVar = True

    def Clear(self):
        global newNum, sumAll, operator, num
        self.lineEdit.clear()
        num = newNum = sumAll = 0.0
        operator = ''

    def ClearE(self):
        self.lineEdit.clear()

    def Delete(self):
        self.lineEdit.backspace()

    def SpecialOperator(self):
        sender = self.sender()
        operator = sender.text()
        num = Decimal(self.lineEdit.text())

        if operator == '\u221a':
            try:
                num = Decimal(math.sqrt(num))
            except ValueError:
                num = 'Math Error. Negative numbers are not valid.'
        if operator == '%':
            num = Decimal(num / Decimal(100))
        if operator == 'n!':
            try:
                num = math.factorial(num)
            except ValueError:
                num = 'Math Error. Negative numbers are not valid.'
        if operator == 'x\u2013\u00b9':
            try:
                num = Decimal(1 / num)
            except ZeroDivisionError:
                num = 'Error. Divide by zero.'
        if operator == '\u00b3\u221a':
            if num > 0:
                num = Decimal(math.pow(num, 1 / 3.0))
            elif num < 0:
                num = Decimal(-math.pow(math.fabs(num), 1 / 3.0))
        if operator == '10\u207f':
            num = Decimal(math.pow(10, num))
        if operator == 'Log':
            try:
                num = Decimal(math.log10(num))
            except ValueError:
                num = 'Math Error. Negative numbers are not valid.'
        if operator == '\u212e\u207f':
            num = Decimal(math.exp(num))
        if operator == 'Ln':
            try:
                num = Decimal(math.log(num))
            except ValueError:
                num = 'Math Error. Negative numbers are not valid.'
        if operator == 'sin':
            if math.fmod(num, 180) == 0:
                num = 0
            else:
                num = Decimal(math.sin(math.radians(num)))
        if operator == 'cos':
            if math.fmod(num, 90) == 0:
                num = 0
            else:
                num = Decimal(math.cos(math.radians(num)))
        if operator == 'tan':
            if math.fmod(num, 180) == 0:
                num = 0
            elif math.fmod(num, 90) == 0:
                num = 'Math Error. Divide by zero.'
            else:
                num = Decimal(math.tan(math.radians(num)))
        if operator == 'sec':
            if math.fmod(num, 90) == 0:
                num = 'Math Error. Divide by zero.'
            else:
                num = Decimal(1.0 / math.cos(math.radians(num)))
        if operator == 'cosec':
            if math.fmod(num, 180) == 0:
                num = 'Math Error. Divide by zero.'
            else:
                num = Decimal(1.0 / math.sin(math.radians(num)))
        if operator == 'cotg':
            if math.fmod(num, 90) == 0:
                num = 0
            elif math.fmod(num, 180) == 0:
                num = 'Math Error. Divide by zero.'
            else:
                num = Decimal(1.0 / math.tan(math.radians(num)))
        if operator == 'asin':
            try:
                num = Decimal(math.degrees(math.asin(num)))
            except ValueError:
                num = 'Math Error. Out of Domain.'
        if operator == 'acos':
            try:
                num = Decimal(math.degrees(math.acos(num)))
            except ValueError:
                num = 'Math Error. Out of Domain.'
        if operator == 'atan':
            num = Decimal(math.degrees(math.atan(num)))
        if operator == 'sinh':
            num = Decimal(math.sinh(num))
        if operator == 'cosh':
            num = Decimal(math.cosh(num))
        if operator == 'tanh':
            num = Decimal(math.tanh(num))

        self.lineEdit.setText(str(num))

    def toDegrees(self, num):
        num = float(num)
        grades = math.trunc(num)
        minutes = math.fabs(math.modf(num)[0])
        minutes = minutes * 60

        seconds = math.modf(minutes)[0]
        minutes = math.trunc(minutes)

        seconds = seconds * 60
        seconds = math.trunc(seconds)

        if seconds >= 60:
            seconds -= 60
            minutes += 1

        if minutes >= 60:
            minutes -= 60
            grades += 1

        if grades > 360 or grades:
            grades = math.trunc(math.fmod(grades, 360))

        if grades < 0:
            grades += 360

        return(str(grades), str(minutes), str(seconds))


def main():
    app = QApplication(sys.argv)
    form = QCalculator()
    f = form.windowFlags()
    f &= (Qt.WindowCloseButtonHint & Qt.WindowMinMaxButtonsHint)
    form.setWindowFlags(f)
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
