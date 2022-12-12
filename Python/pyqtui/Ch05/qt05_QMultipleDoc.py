# PyQt5 進階介面控制項 (容器: 承載更多的控制項)
# 多文件介面的使用
# 在GUI應用程式呈現多個視窗，基本上有三種方式，一為索引標籤控制項，二為堆疊視窗控制項
# 第三種則是多文件介面的使用，前兩種方式有些時候不是很有用，因為其他視窗的視圖被隱藏起來
# 多文件介面的使用為同時顯示多個視窗，可再細分成兩種，一為建立多個獨立的視窗，這些獨立的視窗
# SDI(Single Document Interface, 單文件介面)，每個視窗都能擁有自己的功能表、工具列等，
# 但需要占用較多的記憶體資源。
# 另一種為MDI(Multiple Documents Interface, 多文件介面)，應用程式佔用較少的記憶體資源，
# 每個子視窗都位於主視窗容器中，這個容器控制項稱為QMdiArea。
# QMdiArea控制項通常佔據QMainWindow物件的中央位置，子視窗在這個區域是QMdiSubWindow類別的實例。
# 一般可以設定任何QWidget作為子視窗物件的內部控制項，
# 子視窗在MDI區域可以被階梯式並排或是磚塊式並排進行佈局。
# 此例展示如何在PyQt5的視窗使用QMdiArea控制項。
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    count = 0
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        # 主視窗QMainWindow擁有一個功能表控制項，以及一個MdiArea控制項
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tiled")
        
        # 按一下功能表控制項時，將觸發triggered訊號，以便連接到槽函數windowaction()
        file.triggered[QAction].connect(self.windowaction)
        
        self.setWindowTitle("MDI Demo")
        
    def windowaction(self, q):
        print("triggered")
        
        # 當選擇功能表的"New"指令時，便加入一個新的MDI。
        # 每個MDI都有標題，主視窗內部會增加MDI的數量。
        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow" + str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        
        # 當選擇功能表的"Cascade"和"Tiled"指令時，便在主視窗顯示子視窗的排列方式
        # -- 階梯式並排(Cascade)，或是磚塊式並排(Tiled)顯示子視窗。
        if q.text() == "Cascade":
            self.mdi.cascadeSubWindows()
            
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
