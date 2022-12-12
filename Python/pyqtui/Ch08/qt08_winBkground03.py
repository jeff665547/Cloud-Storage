# PyQt5 圖形與特效
# 設定視窗背景
# 視窗背景主要包括:背景顏色和背景圖片，設定視窗背景有三種方法
# 1. 以QSS設定視窗背景
# 2. 以QPalette設定視窗背景
# 3. 實作paintEvent，再以QPainter繪製背景。
# 本例示範以QPalette設定視窗背景顏色 Palette:調色板
# 
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, 
                             QPushButton, QMainWindow)
from PyQt5.QtGui import (QPalette, QBrush, QPixmap)
from PyQt5.QtCore import Qt
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Background color settings")
    win.resize(350, 250)
    palette = QPalette()
    palette.setColor(QPalette.Background, Qt.red)
    win.setPalette(palette)
    win.show()
    sys.exit(app.exec_())