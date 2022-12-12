# PyQt5 圖形與特效
# QSS的UI美化
# QSS子控制項
# 實際上,QSS子控制項也是一種選擇器，應用於一些複合控制項上，典型的如QComboBox。
# 該控制項的外觀是:有一個矩形的外邊框，右邊有一個下拉箭頭，點擊之後會彈出下拉清單。
# 例如: QComboBox::drop-down { image: url(dropdown.png) }
# 上述樣式指定所有QCombox下拉箭頭是自訂的圖片，圖形檔為dropdown.png。
# ::drop-down 子控制項選擇器可以與先前提到的選擇器聯合使用。
# 例如: QComboBox#myQComboBox::drop-down { image: url(dropdown.png) }
# 表示針對ID為myQComboBox的QComboBox控制項的下拉箭頭，指定自訂圖片。
# 請注意，子控制項選擇器實際上是選擇複合控制項的一部分，也就是針對一部分的複合控制項套用樣式，
# 例如：為QComboBox的下拉式箭頭，而不是針對QComboBox本身指定圖片。
# 本例為上述之示範
from PyQt5.QtWidgets import *
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()
        self.InitUI();
        
    def InitUI(self):
        combo = QComboBox(self)
        combo.setObjectName('myQComboBox')
        combo.addItem('Window')
        combo.addItem('Ubuntu')
        combo.addItem('Red Hat')
        combo.move(50, 50)
        self.setGeometry(250, 200, 320, 250)
        self.setWindowTitle("QComboBox Style")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    # 定義QComboBox控制項的QSS樣式
    qssStyle = '''
            QComboBox#myQComboBox::drop-down {
                image: url(C:/Users/jeff/Desktop/pyqtui/Ch08/QComboxdown.svg)
            }
            '''
    win.setStyleSheet( qssStyle )
    win.show()
    sys.exit(app.exec_())
    