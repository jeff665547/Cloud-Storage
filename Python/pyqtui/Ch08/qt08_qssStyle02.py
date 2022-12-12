# PyQt5 圖形與特效
# QSS的UI美化
# QSS選擇器類型
# QSS選擇器有下列幾種類型。
# (1) 通用選擇器: *, 配對所有的控制項
# (2) 類型選擇器: QPushButton，配對所有的QPushButton及其自類別的實例。
# (3) 屬性選擇器: QPushButton[name = "myBtn"] ，配對所有name屬性是myBtn的
#                 QPushButton實例。請注意，可以自訂該屬性，不一定非得是類別本身的屬性。
# (4) 類別選取器: .QPushButton，配對所有的QPushButtoon實例，但是不包括其子類別。
#                 注意前面有一個小數點，這是和CSS類別選取器不一樣的地方。
# (5) ID選擇器: #myButton，配對所有ID為myButton的控制項，
#               這裡的ID實際上就是objectName指定的值。
# (6) 後代選擇器： QDialog QPushButton，配對所有QDialog容器中的QPushButton，
#                不管是直接或是間接。
# (7) 子選擇器：QDialog > QPushButton，配對所有QDialog容器中的QPushButton，
#              其中要求QPushButton的直接父容器是QDialog。
# 另外,可以聯合使用上面所有的選擇器，並且支援一次設定多種選擇器類型，中間用逗號隔開。
# 例如: #frameCut,#frameInterrupt,#rameJoin,表示這些ID使用上一個規則;
#       #mytable QPushButton，表示選擇所有ID為mytable的容器中包含的QPushButton控制項。
# 本例為按鈕btn2設定了屬性名稱
#
from PyQt5.QtWidgets import *
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        btn1 = QPushButton(self)
        btn1.setText("Button 1")
        
        btn2 = QPushButton(self)
        btn2.setProperty("name", "myBtn")
        btn2.setText("Button 2")
        
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        
        self.setLayout(vbox)
        self.setWindowTitle("QSS style")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    # 將所用的QSS修改為屬性名稱為myBtn的QPushButton，以便改變背景顏色。
    qssStyle = '''
            QPushButton[name = "myBtn"] {
                background-color: red
            }
            '''
    # 以win.setStyleSheet()函數載入QSS樣式，該函數可以設定整個視窗的樣式。
    # setStyleSheet本身是QWidget的成員函數，PyQt大多數的控制項都能直接透過該函數
    # 設定樣式。
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())
