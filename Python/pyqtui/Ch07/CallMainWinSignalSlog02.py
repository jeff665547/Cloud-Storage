# PyQt5 訊號與槽
# 此例示範訊號與槽如何與Qt Designer結合(此檔為人工coding)
# Remark: 
# 1. 自訂訊號必須定義在__init__()函數前
# 2. 自訂訊號可以傳遞如str, int, list, object, float, tuple, dict等眾多類型的參數
# 3. 留意signal和slot的呼叫邏輯，避免signal和slot之間出現無窮循環，例如在slot方法繼
#    續發射該訊號。
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch07")
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from MainWinSignalSlog02 import Ui_Form
from PyQt5.QtCore import pyqtSignal, Qt

class MyMainWindow(QMainWindow, Ui_Form):
    
    # 定義三個訊號
    helpSignal = pyqtSignal(str)  # 參數類型: str
    printSignal = pyqtSignal(list) # 參數類型: list
    
    # 宣告一個多重載版本的訊號，包括一個帶(int, str)類型參數的訊號，
    # 以及帶str類型參數的訊號
    previewSignal = pyqtSignal([int, str], [str])
    
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)  # 介面初始化
        self.initUI()       # 訊號與槽功能建置
    
    # 訊號連結
    def initUI(self):
        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)
        
        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)
    
    # 發射預覽訊號
    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int, str].emit(1080, " Full Screen")
        elif self.previewStatus.isChecked() == False:
            self.previewSignal[str].emit("Preview")
    
    # 發射列印訊號
    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)
    
    def printPaper(self, list):
        self.resultLabel.setText("列印：" + " 份數 " + str(list[0]) + 
                                 " 紙張 " + str(list[1]))
    
    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)
    
    def previewPaper(self, text):
        self.resultLabel.setText(text)
    
    # 重載按鍵事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")
    
    # 顯示說明訊息
    def showHelpMessage(self, message):
        self.resultLabel.setText(message)
        self.statusBar().showMessage(message + " on the status bar.") # 顯示在最下方的狀態列
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
    
# 本例 pyqt5 程式架構
#
#    　emitter    ==> signal (emit（內）, connect（外）) ==>     slot{2nd signal}
#
#  printButton    ==> 　　　　　　clicked                ==> emitPrintSignal{printSignal}
#  previewButto   ==> 　　　　　　clicked                ==> emitPreviewSignal{previewSignal}
#  event(key)     ==> 　　　　　　helpSignal             ==> showHelpMessage
#
#                 ==>        printSignal            ==> printPaper = resultLabel.setText
#                 ==>        previewSignal          ==> previewPaper = resultLabel.setText
#