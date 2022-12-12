# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTreeWidget的使用
# QTreeWidget 類別實現了樹狀結構(檔案總管左側的階層式目錄)
# 樹狀結構是透過QTreeWidget和QTreeWidget和QTreeWidgetItem類別達成，
# 其中QTreeWidgetItem類別用來增加節點
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt

os.chdir("C:/Users/jeff/Desktop/pyqtui/Ch05")

class TreeWidgetDemo(QMainWindow):
    def __init__(self, parent = None):
        super(TreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle("TreeWidget Example")
        self.tree = QTreeWidget()
        
        # 設定行數
        self.tree.setColumnCount(2)
        # 設定樹狀控制項標題
        self.tree.setHeaderLabels(["Key", "Value"])
        # 設定根節點
        root = QTreeWidgetItem(self.tree)
        root.setText(0, "root")
        root.setIcon(0, QIcon("Folder.ico"))
        # 設定行寬
        self.tree.setColumnWidth(0, 160)
        
        # 設定節點的背景顏色
        # QBrush類別用來設定節點的背景顏色
        brush_red = QBrush(Qt.red)
        root.setBackground(0, brush_red)   # 0 代表左邊的Key欄位
        brush_green = QBrush(Qt.green)
        root.setBackground(1, brush_green) # 1 代表右邊的Key欄位
        
        # 設定子節點1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, "child1")
        child1.setText(1, "ios")
        child1.setIcon(0, QIcon("ios.ico"))
        # 設定節點是否為選中的狀態(前面有勾選方框
        # Qt.Unchecked為未勾選, Qt.Checked為勾選)
        child1.setCheckState(0, Qt.Unchecked)
        
        # 設定子節點2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, "child2")
        child2.setText(1, "")
        child2.setIcon(0, QIcon("android.ico"))
        
        # 設定子節點3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, "child3")
        child3.setText(1, "android")
        child3.setIcon(0, QIcon("music.ico"))
        
        self.tree.addTopLevelItem(root)
        # 展開全部節點
        self.tree.expandAll()
        
        self.setCentralWidget(self.tree)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())
    