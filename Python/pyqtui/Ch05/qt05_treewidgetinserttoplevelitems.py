# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTreeWidget的使用
# QTreeWidget 類別實現了樹狀結構(檔案總管左側的階層式目錄)
# 樹狀結構是透過QTreeWidget和QTreeWidget和QTreeWidgetItem類別達成，
# 其中QTreeWidgetItem類別用來增加節點
# 除了使用原本的方法來實作樹狀結構以外
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
        root = QTreeWidgetItem()
        root.setText(0, "root")
        
        rootList = []
        rootList.append(root)
        
        # 設定樹狀控制項的子節點 1
        child1 = QTreeWidgetItem()
        child1.setText(0, "child1")
        child1.setText(1, "ios")
        root.addChild(child1)
        
        self.tree.insertTopLevelItems(0, rootList)
        
        # 展開全部節點
        self.tree.expandAll()
        
        self.setCentralWidget(self.tree)
        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())
    