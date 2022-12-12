# PyQt5 圖形與特效
# QSS的UI美化
# QSS (Qt Style Sheets)為Qt樣式表，它是自定控制項外觀的一種機制。
# QSS大量參考CSS的內容，但要比CSS薄弱許多，不僅選擇器少，可用的QSS屬性也很少，
# 並且並不是所有的屬性都能夠應用於PyQt的控制項。
# QSS使頁面美化跟程式碼層分開，有利於維護。
# QSS的語法規則幾乎與CSS相同。
# QSS的樣式由兩部分組成，其中一部分是選擇器(Selector)，指定受到影響的控制項;
# 另一部分是宣告(Declaration)，指定應該在控制項設定那些屬性。
# 宣告部分是一系列的"屬性:值"對，並且以分號(;)隔開不同的屬性值對,
# 或以大括號({})包括所有的宣告。 
# 例如:QPushButton {color:red} 表示設定QPushButton及其子類別所有實例的前景為紅色。
# 其中，QPushButton是選擇器，代表套用至所有的QPushButton及其子類別。
# 請注意，凡是繼承QPushButton的子類別都會受到影響，這是與CSS不同的地方，
# 因為CSS都是應用製一些標籤(in HTML)，沒有類別的層級架構，更沒有子類別的概念。
# {color:red}則是規則的定義，表示指定前景色是紅色。
# 此外，還可以使用多個選擇器指定相關的宣告，並以逗號隔開各個選擇器。
# 例如: QPushButton, QLineEdit, QComboBox { color: red }
# 這個相當於:
# QPushButton { color: red }
# QLineEdit { color: red }
# QComboBox { color: red }
# 
# 在此例中，整個視窗載入自訂的QSS樣式，其中按鈕的背景都為紅色。

from PyQt5.QtWidgets import *
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        btn1 = QPushButton(self)
        btn1.setText("Button 1")
        
        btn2 = QPushButton(self)
        btn2.setText("Button 2")
        
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        
        self.setLayout(vbox)
        self.setWindowTitle("QSS style")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    # 定義QSS樣式
    qssStyle = '''
            QPushButton {
                background-color: red
            }
            '''
    # 以win.setStyleSheet()函數載入QSS樣式，該函數可以設定整個視窗的樣式。
    # setStyleSheet本身是QWidget的成員函數，PyQt大多數的控制項都能直接透過該函數
    # 設定樣式。
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())
