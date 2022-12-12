# PyQt5 圖形與特效
# PyQt的視窗樣式，預設就是目前作業系統的原始視窗樣式。
# 不同的作業系統之下，原始視窗樣式的效果都不一樣。
# 例如，Ubuntu視窗的美化效果極為美觀，而Windows就稍微次之。
# 在本例中，展示如何設定視窗樣式。
# 如果其他Widget未指定QStyle，則預設使用QApplication的QStyle。
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

class AppWidget(QWidget):
    
    def __init__(self, parent = None):
        super(AppWidget, self).__init__(parent)
        horizontalLayout = QHBoxLayout()
        self.styleLabel = QLabel("Set the style")
        self.styleComboBox = QComboBox()
        # 從QStyleFactory增加多個樣式
        self.styleComboBox.addItems(QStyleFactory.keys())
        # 選擇目前視窗樣式
        index = self.styleComboBox.findText(QApplication.style().objectName(),
                                            QtCore.Qt.MatchFixedString)
        # 設定目前視窗樣式
        self.styleComboBox.setCurrentIndex(index)
        # 透過comboBox控制項選擇視窗樣式
        # 重載訊號函數(詳情請看Ch07資料夾中的範例及相關說明)
        self.styleComboBox.activated[str].connect(self.handleStyleChanged)
        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.styleComboBox)
        self.setLayout(horizontalLayout)
        
    # 改變視窗樣式
    def handleStyleChanged(self, style):
        # 設定QApplication的QStyle樣式。
        QApplication.setStyle(style)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    widgetApp = AppWidget()
    widgetApp.show()
    sys.exit(app.exec_())
    