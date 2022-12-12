# PyQt5 訊號與槽
# 本例使用以下兩種方式進行示範
# (1) 重新實作事件函數
# (2) 重新實作QObject.event()
# 基本上能夠滿足事件處理的絕大部分需求
# 
# 本例首先是類別的建立，接著產生text和message兩個變數，再以paintEvent函數輸出到視窗中
# update 函數的作用是更新視窗。由於視窗更新過程只會觸發一次paintEvent函數
# (它是視窗基礎類別QWidget的內建函數)，因此本例中update函數的作用等同於paintEvent函數
import sys
from PyQt5.QtCore import * #(QEvent, QTimer, Qt)
from PyQt5.QtWidgets import * #(QApplication, QMenu, QWidget)
from PyQt5.QtGui import QPainter

class Widget(QWidget):
    def __init__(self, parent = None):
        super(Widget, self).__init__(parent)
        self.justDoubleClicked = False
        self.key = ""
        self.text = ""
        self.message = ""
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("Events")
        
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.btn1 = QPushButton(self)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout.addWidget(self.btn1)
        self.btn1.setFocusPolicy(Qt.NoFocus)
        
        self.btn2 = QPushButton(self)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout.addWidget(self.btn2)
        self.btn2.setFocusPolicy(Qt.NoFocus)
        
        
        # 避免受視窗大小重繪事件的影響，可將參數0改成3000(3秒)，
        # 然後再執行，就可以明白這行程式碼的意思了
        QTimer.singleShot(0, self.giveHelp)
        
    def giveHelp(self):
        self.text = "請點擊這裡觸發滑鼠追蹤功能"
        self.update()  # 重繪事件，也就是觸發paintEvent函數
        
    """重新實作關閉事件"""
    def closeEvent(self, event):
        print("Closed")
    
    """重新實作快顯功能表事件"""
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        oneAction = menu.addAction("&One")
        twoAction = menu.addAction("&Two")
        oneAction.triggered.connect(self.one)
        twoAction.triggered.connect(self.two)
        
        if not self.message:
            menu.addSeparator()
            threeAction = menu.addAction("&Three")
            threeAction.triggered.connect(self.three)
            
        menu.exec_(event.globalPos())
        
    """快顯功能表的槽函數"""
    def one(self):
        self.message = "Menu option One"
        self.update()
        
    def two(self):
        self.message = "Menu option Two"
        self.update()
        
    def three(self):
        self.message = "Menu option Three"
        self.update()
    
    """重新實作繪製事件"""
    def paintEvent(self, event):
        text = self.text
        i = text.find("\n\n")
        if i >= 0:
            text  = text[0:i]
        if self.key: # 若觸發鍵盤按鍵，則在訊息文字中紀錄案件資訊
            text += "\n\n 您按下了: {}".format(self.key)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        
        # 繪製訊息文字的內容
        painter.drawText(self.rect(), Qt.AlignCenter, text)
        
        # 若訊息文字存在，則在底部致中顯示，5秒後清空重繪
        if self.message:
            painter.drawText(self.rect(), Qt.AlignBottom |
            Qt.AlignHCenter, self.message)
            QTimer.singleShot(5000, self.clearMessage)
            QTimer.singleShot(5000, self.update)
            
    """清空訊息文字的槽函數"""
    def clearMessage(self):
        self.message = ""
    
    """重新實作調整視窗大小的事件"""
    def resizeEvent(self, event):
        self.text = "調整後的視窗大小為QSize({}, {})".format(event.size().width(), 
                                                    event.size().height())
        self.update()
        
    """重新實作滑鼠釋放事件"""
    def mouseReleaseEvent(self, event):
        # 若為按兩下釋放，則不追蹤滑鼠移動
        # 若改為按一下釋放，則得改變追蹤功能的狀態，如果開啟追蹤功能就跟蹤，
        # 否則就不追蹤
        if self.justDoubleClicked:
            self.justDoubleClicked = False
        else:
            self.setMouseTracking(not self.hasMouseTracking()) # 按一下滑鼠
            if self.hasMouseTracking():
                self.text = "開啟滑鼠追蹤功能\n" + "請移動一下滑鼠\n" + \
                    "按一下滑鼠就可以關閉這個功能"
            else: 
                self.text = "關閉滑鼠追蹤功能\n" + "按一下滑鼠就可以開啟這個功能"
            self.update()
            
    """重新實作滑鼠移動事件"""
    def mouseMoveEvent(self, event):
        if not self.justDoubleClicked:
            globalPos = self.mapToGlobal(event.pos()) #將視窗座標轉換為螢幕座標
            self.text = """滑鼠位置
            視窗座標為: QPoint({}, {})
            螢幕座標為: QPoint({}, {})""".format(event.pos().x(), 
            event.pos().y(), globalPos.x(), globalPos.y())
            self.update()
            
    """重新實作滑鼠按兩下事件"""
    def mouseDoubleClickEvent(self, event):
        self.justDoubleClicked = True
        self.text = "您按了兩下滑鼠"
        self.update()
        
    """重新實作鍵盤按下事件"""
    def keyPressEvent(self, event):
        self.key = ""
        if event.key() == Qt.Key_Home:
            self.key = "Home"
        elif event.key() == Qt.Key_End:
            self.key = "End"
        elif event.key() == Qt.Key_Up:
            self.key = "Up"    
        elif event.key() == Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl + PageUp"
            else:
                self.key = "PageUp"
        elif event.key() == Qt.Key_PageDown:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl + PageDown"
            else:
                self.key = "PageDown"
        elif Qt.Key_A <= event.key() <= Qt.Key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key = "Shift+"
            self.key += event.text()
        if self.key:
            self.key = self.key
            self.update()
        else:
            QWidget.keyPressEvent(self, event)
            
    """重新實作其他事件，適用於PyQt沒有提供該事件的處理函數的情況，由於Tab鍵涉及焦點切換，
    不會傳遞給keyPressEvent，因此必須在這裡重新定義"""
    def event(self, event):
        if (event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab):
            self.key = "在event()中捕獲Tab鍵"
            self.update()
            return True
        return QWidget.event(self, event)
    
    # 視窗中所有事件都會傳遞給event函數，event函數會根據事件的類型，把事件分配給
    # 不同的函數處理。
    # 例如:
    # 1. 繪圖事件：event 會交給 paintEvent 函數
    # 2. 滑鼠移動事件: event 會交給 keyPressEvent 函數
    # 注意: event函數對Tab鍵的處理事件和上述邏輯不同，其會把焦點從目前控制項的位置，
    # 切換到Tab鍵後下一個視窗控制項的位置，並返回True，而不是交給 keyPressEvent 函數。
    # 因此，這個函數就是去重新定義這件事情，讓它的行為與鍵盤上一般按鍵相同。
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
    # sys.exit(app.exec_())

