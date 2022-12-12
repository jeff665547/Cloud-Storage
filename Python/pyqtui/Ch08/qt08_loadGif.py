# PyQt5 圖形與特效
# 不規則的視窗顯示
# 不規則的視窗顯示及其動畫效果
# 本例示範載入GIF動畫效果。
# 
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

class LoadingGifWin(QWidget):
    def __init__(self, parent = None):
        super(LoadingGifWin, self).__init__(parent)
        self.label = QLabel("", self)
        self.setFixedSize(128, 128)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie("./loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    loadingGitWin = LoadingGifWin()
    loadingGitWin.show()
    sys.exit(app.exec_())
    