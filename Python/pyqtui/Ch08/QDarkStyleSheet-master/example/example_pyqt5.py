# PyQt5 圖形與特效
# QSS的UI美化
# QDarkStyleSheet
# 除了自行編寫QSS以外，網路上還有許多高品質的QSS樣式表，例如:QDarkStyleSheet，它是一個
# 適用於PyQt應用程式的深黑色樣式表。可從GitHub上下載，網址是
# https://github.com/ColinDuquesnoy/QDarkStyleSheet/tree/master/qdarkstyle
#
# 1. 安裝QDarkStyleSheet
# 第一種方式 (使用GitHub安裝)
# 至QDarkStyleSheet的GitHub官網，按下右側的"Clone or download"鍵，
# 將QDarkStyleSheet下載到本地端磁碟，
# 保存在C:\Users\jeff\Desktop\pyqtui\Ch08\QDarkStyleSheet-master的目錄下
# 第二種方式 (使用pip命令安裝)
# pip install qdarkstyle
#
# 2. 使用QDarkStyleSheet
# a. 匯入qdarkstyle模組 import qdarkstyle 
# b. 使用app.StyleSheet()載入qdarkStyle樣式表。
import logging
import sys
from PyQt5 import QtWidgets, QtCore
# make the example runnable without using pip install
#from os.path import abspath, dirname
#sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))
#import os
#os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08\QDarkStyleSheet-master\example")
import qdarkstyle
import example_pyqt5_ui as example_ui

def main():
    """
    Application entry point
    """
    logging.basicConfig(level = logging.DEBUG)
    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    
    # setup ui
    ui = example_ui.Ui_MainWindow()
    ui.setupUi(window)
    ui.bt_delay_popup.addActions([
        ui.actionAction,
        ui.actionAction_C
        ])
    ui.bt_instant_popup.addActions([
        ui.actionAction,
        ui.actionAction_C
        ])
    ui.bt_menu_button_popup.addActions([
        ui.actionAction,
        ui.actionAction_C
        ])
    item = QtWidgets.QTableWidgetItem("Test")
    item.setCheckState(QtCore.Qt.Checked)
    ui.tableWidget.setItem(0, 0, item)
    window.setWindowTitle("QDarkStyle example")
    
    # tabify dock widgets to show bug #6
    window.tabifyDockWidget(ui.dockWidget1, ui.dockWidget2)
    
    # Use app.setStyleSheet to setup the stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    # auto quit after 2s when testing on travis-ci
    if "--travis" in sys.argv:
        QtCore.QTimer.singleShot(2000, app.exit)
        
    # run
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
    