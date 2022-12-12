# PyQt5 圖形與特效
# 繪圖
# 雙緩衝繪圖
# 本例示範以雙緩衝技術繪製矩形，避免出現重影。
# 這裡有兩個QPixmap物件，或者說有兩個緩衝區，所以稱之為雙緩衝繪圖。
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("Draw Rectangle Example")
        
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()
        #1 增加兩個變數。
        # 輔助畫布
        self.tempPix = QPixmap()
        # 標示是否正在繪圖
        self.isDrawing = False
        self.initUI()
        
    def initUI(self):
        # 設定視窗大小600*500
        self.resize(600, 500)
        # 設定畫布大小400*400，背景為白色
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        
    #2 覆寫paintEvent()函數，如果正在畫圖，就在輔助畫布上進行，將pix的內容複製到tempPix，
    #  以保留先前的內容。
    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x() - x
        h = self.endPoint.y() - y
        
        # 如果正在繪圖，就在輔助畫布上繪製
        if self.isDrawing:
            # 將以前pix的內容複製到tempPix，保留先前的內容
            self.tempPix = self.pix
            pp = QPainter(self.tempPix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.tempPix)
            
        else:
            pp = QPainter(self.pix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.pix)
    
    #3 覆寫mousePressEvent()函數，更改按下滑鼠鍵時的處理邏輯。
    def mousePressEvent(self, event):
        # 按下滑鼠左鍵
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            self.isDrawing = True
    
    #4 覆寫mouserrReleaseEvent()函數，更改按下滑鼠鍵時的處理邏輯。
    def mouseReleaseEvent(self, event):
        # 釋放滑鼠左鍵
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 重新繪製
            self.update()
            self.isDrawing = False
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
