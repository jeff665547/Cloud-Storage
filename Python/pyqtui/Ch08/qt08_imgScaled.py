# PyQt5 圖形與特效
# 縮放圖片
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")

from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout)
from PyQt5.QtGui import (QImage, QPixmap)
from PyQt5.QtCore import Qt
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        # filename為圖片的路徑
        filename = "./left.svg"
        img = QImage(filename)
        # 設定標籤的寬度為120像素，高度為120像素，
        # 載入的圖片按照標籤的高度和寬度等比例縮放。
        label1 = QLabel(self)
        label1.setFixedWidth(120)
        label1.setFixedHeight(120)
        
        # 縮放圖片，以固定大小顯示
        result = img.scaled(label1.width(), label1.height(), 
                            Qt.IgnoreAspectRatio, Qt.SmoothTransformation);
        # 在標籤控制項顯示圖片
        label1.setPixmap(QPixmap.fromImage(result))
        
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        
        self.setLayout(vbox)
        self.setWindowTitle("圖片大小縮放例子")
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())
    