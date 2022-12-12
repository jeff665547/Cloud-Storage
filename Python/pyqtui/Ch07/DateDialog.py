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
# 本例示範調用屬性來傳遞多個視窗資料(即由主視窗取得子視窗控制項的屬性)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
    def __init__(self, parent = None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle("DateDialog")
        
        # 在佈局中加入控制項
        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)
        
        # 使用兩個按鈕(OK和Cancel)，分別連結 accept() 和 reject() 槽函數
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
    # 從對話方塊取得目前日期和時間
    def dateTime(self):
        return self.datetime.dateTime()
    
    # 使用靜態函數建立對話塊，並返回(date, time, accepted)
    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        date = dialog.dateTime()
        return (date.date(), date.time(), result == QDialog.Accepted)
    # @staticmethod 有三作用
    # 1. static method 不需要也不能將類別實體以引數self的方式傳入，
    #    意即getDateTime()的()內沒有self。
    # 2. static method 可以由類別直接呼叫(意即DateDialog.getDateTime)，
    #    而不一定需要用到類別實例去呼叫。
    # 3. static method 也可以使用類別實例去呼叫，但是引數一樣是不帶有self。
    #
    # 在類別定義一個靜態函數getDateTime()，以便返回3個時間值。
    # 原理是利用靜態函數的特性，先產生DateDialog物件，並呼叫dialog.exec_()函數
    # 明確執行對話方塊。然後透過dialog.exec_()的返回值，判斷使用者按的是OK按鈕或
    # Cancel按鈕，再進行下一步。
