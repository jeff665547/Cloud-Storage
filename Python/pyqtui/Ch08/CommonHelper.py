# PyQt5 圖形與特效
# 載入QSS
# Qt經常需要使用樣式，為了降低耦合性(與邏輯程式碼分離)，
# 通常會定義一個QSS檔，然後編寫控制項(如QLable、QLineEdit、QPushButton)的樣式。
# 接著以QApplication或QMainWindow載入樣式，這樣就能讓整個應用程式共用同一種樣式。
# 另外，為了方便日後的使用，可先編寫一個載入樣式的公共類別CommonHelper。
# 然後在主函數載入
# 這樣一來，當變換樣式需要進行全域修改時，
# 只需利用CommonHelper.readQss()讀取的QSS檔即可。
#
class CommonHelper:
    def __init__(self):
        pass
    
    @staticmethod
    def readQss(style):
        with open(style, "r") as f:
            return f.read()
        
        