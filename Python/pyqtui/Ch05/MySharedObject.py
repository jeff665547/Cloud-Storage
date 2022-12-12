# PyQt5 進階介面控制項 
# Used in the qt502_webviewJs02.py
# 網頁互動
# JavaScript呼叫PyQt程式碼 (雙向互動)
# 自訂的MySharedObject類別必須繼承QWidget基礎類別，才能呼叫PyQt控制項。
# 如果只是單純傳遞資料，例如Python中的基本資料型別，而不需要叫用PyQt控制項的話，
# 那麼MySharedObject只需繼續繼承QObject類別就行了。
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget, QMessageBox

class MySharedObject(QWidget):
    def __init__(self):
        super(MySharedObject, self).__init__()
        
    def _getStrValue(self):
        # Set the parameters
        return "100"
    
    def _setStrValue(self, AA):
        # Get the parameters
        print("Get the parameters {}".format(AA))
        QMessageBox.information(self, "Information", "Get the parameters {}".format(AA))
        
    # 定義對外開放的方法
    strValue = pyqtProperty(str, fget = _getStrValue, fset = _setStrValue)