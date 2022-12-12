# PyQt5 圖形與特效
# 不規則的視窗顯示
# 前一個例子(qt08_paint02.py)的不規則視窗是不可以拖動的，這裡示範可以拖動的功能
#
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPixmap, QPainter, QCursor, QBitmap)
from PyQt5.QtCore import Qt

class ShapeWidget(QWidget):
    def __init__(self, parent = None):
        super(ShapeWidget, self).__init__(parent)
        self.setWindowTitle("不規則，但可以拖動的視窗")
        self.mypix()
        
    # 顯示不規則的圖片pix
    def mypix(self):
        
        # 獲得圖片自身的遮罩
        self.pix = QBitmap("./mask.png")
        
        # 將獲得圖片的大小作為窗口的大小
        self.resize(self.pix.size())
        
        # 增加一個遮罩
        self.setMask(self.pix)
        
        self.dragPosition = None
        
    # 重新定義按下滑鼠的回應函數mousePressEvent(QMouseEvent)，
    # 以及移動滑鼠游標的回應函數mouseMoveEvent(QMouseEvent)，
    # 使不規則視窗能回應滑鼠事件，隨意拖動視窗。
    def mousePressEvent(self, event):
        # 滑鼠按下左鍵
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

        if event.button() == Qt.RightButton:
            self.close()
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            # 當以左鍵移動視窗時修改偏移值
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    # 當視窗首次繪製時，會載入paintEvent()函數
    # 需要重新繪製windows時使用 self.update() or self.repaint()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), 
                           QPixmap("./image1.jpg"))
        
    def mouseDoubleClickEvent(self, event):
        self.mypix()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ShapeWidget()
    form.show()
    sys.exit(app.exec_())