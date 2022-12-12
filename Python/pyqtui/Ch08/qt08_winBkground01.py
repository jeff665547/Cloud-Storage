# PyQt5 圖形與特效
# 設定視窗背景
# 視窗背景主要包括:背景顏色和背景圖片，設定視窗背景有三種方法
# 1. 以QSS設定視窗背景
# 2. 以QPalette設定視窗背景
# 3. 實作paintEvent，再以QPainter繪製背景。
# 本例示範以QSS設定視窗背景。(以setStyleSheet設定視窗背景圖片)
# 在QSS中，可以使用background或者background-color的方式設定背景色。一旦設定之後，
# 子控制項預設會繼承父視窗的背景色。如果想要偽控制項單獨指定背景圖片或圖示，
# 則可透過setPixmap或setIcon完成，有關這方面的使用方式，請參考第四章。

import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Background Photo Setting")
    win.resize(350, 250)
    
    # 設定視窗名稱
    win.setObjectName("MainWindow")
    # 設定圖片的相對路徑
    win.setStyleSheet("#MainWindow{border-image:url(./image1.jpg);}")
    
    # 以setStyleSheet設定視窗背景顏色
    #win.setStyleSheet("#MainWindow{background-color: yellow}")
    win.show()
    sys.exit(app.exec_())
    