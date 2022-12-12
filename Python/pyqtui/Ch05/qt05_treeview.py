# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTreeWidget的使用 (with QTreeView的使用)
# 系統制式模式
# 在先前的範例中，一項一項加入QTreeWidgetItem類別的節點。
# 這樣做有時很不方便，特別是有複雜的樹狀結構時，此時一般來說都是使用
# QTreeView類別來完成，而非QTreeWidget類別。
# QTreeView類別與QTreeWidget類別最大的區別是:
# 前者可以使用作業系統提供的制式模式，例如: 檔案系統的樹狀列表。
import sys
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Windows 系統提供的模式
    model = QDirModel()
    
    # 建立一個QTreeView控制項
    tree = QTreeView()
    
    # 為控制項增加模式
    tree.setModel(model)
    tree.setWindowTitle("QTreeView Example")
    tree.resize(640, 480)
    tree.show()
    sys.exit(app.exec_())
    