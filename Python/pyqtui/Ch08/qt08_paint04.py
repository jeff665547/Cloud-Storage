# PyQt5 圖形與特效
# 不規則的視窗顯示
# 不規則的視窗顯示及其動畫效果
# 本例示範顯示不同方向的箭頭，並且每500毫秒改變一次箭頭方向，按照上、右、下、左的方向轉動
# 
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPixmap, QPainter, QCursor)
from PyQt5.QtCore import (Qt, QTimer)

class ShapeWidget(QWidget):
    def __init__(self, parent = None):
        super(ShapeWidget, self).__init__(parent)
        self.i = 1
        self.mypix()
        
        # 每次初始化視窗時只執行一次paintEvent()函數，所以每載入一次圖片，
        # 就得重新呼叫一次paintEvent()函數，亦即在更新視窗時調用。
        self.timer = QTimer()
        self.timer.setInterval(500) # 500 毫秒
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()
        
    # 顯示不規則圖片
    def mypix(self):
        # 當計時器時間到期之後，更新視窗的程式碼。
        self.update()
        if self.i == 5:
            self.i = 1
        self.mypic = {1: "./left.svg", 2: "./up.svg", 3: "./right.svg", 4: "./down.svg"}
        self.pix = QPixmap(self.mypic[self.i], "0", Qt.AvoidDither | 
                           Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        
        # pixmap.setMask()函數是為了呼叫他的控制項增加一個遮罩，遮住所選區域以外的部分，
        # 使控制項變成透明。
        # 其參數可以是QBitmap物件或是QRegion物件。
        # 在這裡呼叫QPixmap實例的self.pix.mask()函數，以取得圖片本身的遮罩，
        # 返回值是一個QBitmap物件。
        self.setMask(self.pix.mask())
        self.dragPosition = None
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
        
    # 滑鼠雙擊事件
    def mouseDoubleClickEvent(self, event):
        if event.button() == 1:
            self.i += 1
            self.mypix()
            
    # 視窗每500毫秒執行一次更新操作，重繪視窗
    def timeChange(self):
        self.i += 1
        self.mypix()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ShapeWidget()
    form.show()
    sys.exit(app.exec_())
    