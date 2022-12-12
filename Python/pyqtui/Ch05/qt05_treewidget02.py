# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTreeWidget的使用
# 為節點增加回應事件(e.g. 展開樹狀結構)
from PyQt5.QtWidgets import *
import sys

class TreeWidgetDemo(QMainWindow):
    def __init__(self, parent = None):
        super(TreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle("TreeWidget Example")
        self.tree = QTreeWidget()
        
        # 設定行數
        self.tree.setHeaderLabels(["Key", "Value"])
        root = QTreeWidgetItem(self.tree)
        root.setText(0, "root")
        root.setText(1, "0")
        
        child1 = QTreeWidgetItem(root)
        child1.setText(0, "child1")
        child1.setText(1, "1")
        
        child2 = QTreeWidgetItem(root)
        child2.setText(0, "child2")
        child2.setText(1, "2")
        
        child3 = QTreeWidgetItem(root)
        child3.setText(0, "child3")
        child3.setText(1, "3")
        
        child4 = QTreeWidgetItem(child3)
        child4.setText(0, "child4")
        child4.setText(1, "4")
        
        child5 = QTreeWidgetItem(child3)
        child5.setText(0, "child5")
        child5.setText(1, "5")
        
        self.tree.addTopLevelItem(root)
        self.tree.clicked.connect(self.onTreeClicked)
        self.setCentralWidget(self.tree)
        
    def onTreeClicked(self, qmodelindex):
        item = self.tree.currentItem()
        print("key = {}, value = {}".format(item.text(0), item.text(1)))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())
