# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildrenForm3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(369, 294)
        self.textEdit = QtWidgets.QTextEdit(ChildrenForm)
        self.textEdit.setGeometry(QtCore.QRect(16, 16, 801, 591))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
        self.textEdit.setHtml(_translate("ChildrenForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我是子視窗內容</p></body></html>"))

