# PyQt5 訊號與槽
# 傳遞視窗資料
# 開發程式時，若程式只有一個視窗，只需關心視窗裡面各個控制項之間如何傳遞資料
# 但在設計PyQt程式的過程中，經常會遇到輸入或選擇多個參數的問題。
# 若將多個參數寫到一個視窗，主視窗會顯得很臃腫。因此，
# 一般是加入一個按鈕然後調用對話方塊，接著在對話方塊挑選參數，
# 當關閉對話方塊時再將參數值返回主視窗。
#
# 為此，PyQt提供一些標準的對話方塊類別，應用於輸入資料、修改資料、更改應用程式的設定等，
# 常見的有QFileDialog, QInputDialog, QColorDialog, QFontDialog等。
#
# 在不同的視窗之間傳遞參數，一般有兩種解決辦法。
# 1. 由主視窗取得子視窗控制項的屬性(即在自訂對話方塊之間透過屬性傳遞)
# 2. 透過訊號與槽機制，子視窗以發射訊號的形式傳遞資料，
#    再由主視窗的槽函數接收這些資料。(即在視窗之間以訊號與槽的機制完成)
#
# 本例示範訊號與槽的機制完成不同的視窗之間傳遞參數。
# 對於多視窗的資料傳遞，一般是透過子視窗發射訊號，由主視窗透過槽函數捕捉此訊號，
# 然後取得其內的資料。子視窗發射的訊號有兩種，第一種是發射PyQt內建的訊號；
# 另一種是發射自訂的訊號。本例將介紹這兩種方式的訊號與槽機制。
#
# 自訂訊號的好處是：可以自訂它的參數類型。當發射一個自訂訊號時，參數類型可以是
# int, str, dict, list等； 如果發射內建訊號，則只能是幾個特定的參數。
#
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
    Signal_OneParameter = pyqtSignal(str)
    
    def __init__(self, parent = None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle("子視窗 用來發射訊號")
        
        # 在佈局中加入控制項
        layout = QVBoxLayout(self)
        
        self.label = QLabel(self)
        self.label.setText("前者發射內建訊號\n後者發射自訂訊號")
        
        self.datetime_inner = QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())
        
        self.datetime_emit = QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())
        
        layout.addWidget(self.label)
        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)
        
        # 使用兩個button(Ok 和 Cancel)分別連結accept()和reject()槽函數
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        # 只有按下OK鍵時時間才會觸發子視窗的槽函數emit_signal，而這個槽函數中又會發射自訂訊號
        # Signal_OneParameter。就這個訊號函數而言，便是為了傳遞date_str參數
        # 給主視窗的槽函數。
        buttons.accepted.connect(self.emit_signal)
        # self.datetime_emit.dateTimeChanged.connect(self.emit_signal)
        # 上面此行程式碼表示當控制項datetime_emit的時間發生變化時，
        # 就會觸發子視窗的槽函數emit_signal，而這個槽函數中又會發射自訂訊號
        # Signal_OneParameter。就這個訊號函數而言，便是為了傳遞date_str參數
        # 給主視窗的槽函數。
        
    def emit_signal(self):
        date_str = self.datetime_emit.dateTime().toString()
        self.Signal_OneParameter.emit(date_str)
