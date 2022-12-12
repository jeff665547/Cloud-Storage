# PyQt5 訊號與槽
# 斷開和連接訊號與槽
from PyQt5.QtCore import QObject, pyqtSignal

class SignalClass(QObject):
    
    # 宣告無參數的訊號
    signal1 = pyqtSignal()
    
    # 宣告帶一個int類型參數的訊號
    signal2 = pyqtSignal(int)
    
    def __init__(self, parent = None):
        super(SignalClass, self).__init__(parent)
        
        # 將訊號signal1連結到sin1Call和sin2Call這兩個槽函數，
        # 如此一來只要signal1一被觸發，就會依序呼叫後面兩個槽函數
        self.signal1.connect(self.sin1Call)
        self.signal1.connect(self.sin2Call)
        
        # 將訊號signal2連結到訊號signal1
        self.signal2.connect(self.signal1)
        
        # 發射訊號
        self.signal1.emit()
        print("AAAA")
        self.signal2.emit(1)
        print("BBBB")
        
        # 斷開signal1、signal2訊號與各槽函數的連結
        self.signal1.disconnect(self.sin1Call)
        self.signal1.disconnect(self.sin2Call)
        self.signal2.disconnect(self.signal1)
        
        # 將訊號 signal1 和 signal2 連結到同一個槽函數 sin1Call
        self.signal1.connect(self.sin1Call)
        self.signal2.connect(self.sin1Call)
        
        # 再次發射訊號
        self.signal1.emit()
        self.signal2.emit(1)  
        # 訊號發出的參數個數可以大於槽函數接收的參數個數，
        # 此例中槽函數不接收任何參數。
        
    def sin1Call(self):
        print("signal-1 emit")
        
    def sin2Call(self):
        print("signal-2 emit")
        
if __name__ == "__main__":
    signal = SignalClass()