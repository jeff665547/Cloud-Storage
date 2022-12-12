# PyQt5 圖形與特效
# 設定視窗背景
# 視窗背景主要包括:背景顏色和背景圖片，設定視窗背景有三種方法
# 1. 以QSS設定視窗背景
# 2. 以QPalette設定視窗背景
# 3. 實作paintEvent，再以QPainter繪製背景。
# 本例示範以QPalette設定視窗背景圖片 Palette:調色板
# 使用QPalette設定背景圖片時，必須考慮圖片的尺寸(右擊圖片檔，從內容中的詳細資料可以取得(尺寸))，
# 當圖片的寬度和高度大於視窗的寬度和高度時，圖片將平舖整個背景;
# 當圖片的寬度和高度小於視窗的寬度和高度時，則會載入多張圖片。
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, 
                             QPushButton, QMainWindow)
from PyQt5.QtGui import (QPalette, QBrush, QPixmap)
from PyQt5.QtCore import Qt
import sys

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Background color settings")
    win.resize(460, 260)
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./image1.jpg")))
    # 當背景圖片的寬度和高度(930x524)大於或小於視窗的寬度和高度(460x260)時，
    # 使用setPalette()加入背景
    win.setPalette(palette)
    win.show()
    sys.exit(app.exec_())
    