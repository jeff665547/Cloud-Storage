# PyQt5 圖形與特效
# 設定視窗透明
# 如果是透明的視窗，那麼透過視窗就能看到桌面的背景。
# 若想實現視窗的透明效果，必須設定視窗的透明度。
# 透明度的取值範圍為 0.0(全透明) ~ 1.0(不透明)，預設值為1.0
#
from PyQt5.QtWidgets import (QApplication, QMainWindow)
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("窗口透明度設置")
    win.setWindowOpacity(0.5)
    
    win.resize(350, 250)
    win.show()
    sys.exit(app.exec_())
    