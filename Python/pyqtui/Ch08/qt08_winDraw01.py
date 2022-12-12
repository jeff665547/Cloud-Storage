# PyQt5 圖形與特效
# 繪圖
# PyQt常用的圖形類別有4種，即QPixmap, QImage, QPicture 和 QBitmap
# QPixmap: 專門為繪圖而設計，繪製圖片時需要使用QPixmap
# QImage: 提供一個與硬體無關的圖形表示函數，應用於存取圖片的像素。
# QPicture: 為一個繪圖設備類別，他繼承QPainter類別。可以使用QPainter的
#           begin()函數在QPicture繪圖，再以end()函數結束繪圖。QPicture的save()
#           函數，會將QPainter使用過的繪圖指令儲存到檔案中。
# QBitmap: 為一個繼承QPixmap的簡單類別，它提供1bit深度的二值圖形類別。
#          QBitmap擁有的單色圖形，可應用於製作游標(QCursor)或者筆刷(QBrush)。
# 簡單繪圖
# 本例示範最基本的畫線功能，按下滑鼠左鍵在白色畫布開始畫線，完成簡單的塗鴉功能。
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("Simple Painter Example")
        
        #1 點的容器初始化
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()
        
    def initUI(self):
        # 設定視窗大小為600*500
        self.resize(600, 500)
        # 設定畫布大小為400*400，背影為白色
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        
    #2 覆寫paintEvent()函數
    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # 根據滑鼠游標前後的兩個位置繪製直線
        pp.drawLine(self.lastPoint, self.endPoint)
        # 讓前一個座標值等於後一個座標值，就能畫出連續的線
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)
        
    #3 覆寫mousePressEvent()函數，使用兩點繪製線條，這兩點從下面的滑鼠事件中取得
    def mousePressEvent(self, event):
        # 按下滑鼠左鍵
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            
    #4 覆寫mouseMoveEvent()函數，當按下滑鼠左鍵時取得開始點，每次繪製都讓結束點和開始點重疊，
    #  以便確保這兩個點都是預期的值。
    def mouseMoveEvent(self, event):
        # 然後移動滑鼠游標
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # 重新繪製
            self.update()
            
    #5 覆寫mouseReleaseEvent()函數，當移動滑鼠游標時取得結束點，並更新繪製。這裡的
    #  buttons()函數用來取得滑鼠移動過程中按下的所有按鍵，然後以Qt.LeftButton判斷
    #  是否按下左鍵。mouseReleaseEvent()必須使用該函數判斷按鍵按下的滑鼠按鍵，最後
    #  呼叫update()函數，以便執行paintEvent()函數重新繪製。
    def mouseReleaseEvent(self, event):
        # 釋放滑鼠左鍵
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # 重新繪製
            self.update()
            
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
    