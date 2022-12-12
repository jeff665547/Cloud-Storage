# PyQt5 訊號與槽
# 本例使用以下方式進行示範
# (4) 在QApplication安裝事件篩選程式
#
# 第四種事件的程式碼和第三種非常相似
# 其差別在於
# 1. 註解掉原本的 installEventFilter 用法。
# 2. 在 QApplication 安裝 installEventFilter。
# 而造成的差異為第四種事件確實過濾了所有事件，
# 然而第三種只篩選了三個標籤控制項的事件
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
import sys

class EventFilter(QDialog):
    def __init__(self, parent = None):
        super(EventFilter, self).__init__(parent)
        self.setWindowTitle("事件篩選程式")
        
        self.label1 = QLabel("請點擊")
        self.label2 = QLabel("請點擊")
        self.label3 = QLabel("請點擊")
        self.LabelState = QLabel("test")
        
        self.image1 = QImage("logo-45.png")
        self.image2 = QImage("logo-45.png")
        self.image3 = QImage("logo-45.png")
        
        self.width = 600; self.height = 300
        
        self.resize(self.width, self.height)
        
        # installEventFilter 用法
        # self.label1.installEventFilter(self)
        # self.label2.installEventFilter(self)
        # self.label3.installEventFilter(self)
        
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.label1, 500, 0)
        mainLayout.addWidget(self.label2, 500, 1)
        mainLayout.addWidget(self.label3, 500, 2)
        mainLayout.addWidget(self.LabelState, 600, 1)
        self.setLayout(mainLayout)
        
    def eventFilter(self, watched, event):
        
        #　查看篩選的事件種類
        print(type(watched))
        
        # 只過濾label1的點擊事件(MouseButtonPress)以及釋放事件(MouseButtonRelease)，
        # 重寫其行為，並忽略其他事件
        if watched == self.label1:
        
            # 這裡過濾滑鼠點擊事件，重寫其行為
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.LabelState.setText("按下滑鼠左鍵")
                elif mouseEvent.buttons == Qt.MidButton:
                    self.LabelState.setText("按下滑鼠中間鍵")
                elif mouseEvent.buttons() == Qt.RightButton:
                    self.LabelState.setText("按下滑鼠右鍵")
                    
                """轉換圖片大小"""
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp = self.image1.transformed(transform)
                self.label1.setPixmap(QPixmap.fromImage(tmp))
                # 此段程式碼意思為按下滑鼠鍵，就會對label1乘載的圖片進行縮放
                # (長和寬各縮放一半)
                
            # 這裡過濾滑鼠釋放事件，重寫其行為
            if event.type() == QEvent.MouseButtonRelease:
                self.LabelState.setText("釋放滑鼠按鈕")
                self.label1.setPixmap(QPixmap.fromImage(self.image1))
                
        # 對於其他情況，將返回系統預設的事件處理方法
        return QDialog.eventFilter(self, watched, event)
    
if __name__ == "__main__":
    os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch07")
    app = QApplication(sys.argv)
    dialog = EventFilter()
    
    # 此程式碼意義為dialog的所有事件都要經過eventFilter函數處理，而不僅僅是三個
    # 標籤控制項的事件。
    app.installEventFilter(dialog)
    
    dialog.show()
    app.exec_()
    