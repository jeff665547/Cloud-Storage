# PyQt5 進階介面控制項 
# 網頁互動
# PyQt呼叫JavaScript腳本
# 透過QWebEnginePage類別的runJavaScript(str, Callable)函數，便可方便地完成PyQt和
# HTML/JavaScript的雙向通訊，同時實現Python程式碼和HTML/JavaScript腳本的分離，有利於
# 開發人員分工協作。
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

# 建立一個應用程式實例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Web頁面的JavaScript與QWebEngineView互動範例")

# 建立一個垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)

# 建立一個QWebEngineView物件
view = QWebEngineView()
view.setHtml('''
<html>
  <head>
    <title>A Demo Page</title>

    <script language = "javascript">
        // 取得輸入的姓名，然後在頁面顯示提交按鈕
        function completeAndReturnName(){
          var fname = document.getElementById('fname').value;
          var lname = document.getElementById('lname').value;
          var full = fname + ' ' + lname;
          
          document.getElementById('fullname').value = full;
          document.getElementById('submit-btn').style.display = 'block';
          
          return full;
        }
    </script>
  </head>

  <body>
    <form>
      <label for="fname">First name:</label>
        <input type="text" name="fname" id="fname"></input>
        <br />
        <label for="lname">Last name:</label>
        <input type="text" name="lname" id="lname"></input>
        <br />
        <label for="fullname">Full name:</label>
        <input disabled type="text" name="fullname" id="fullname"></input>
        <br />
        <input style="display: none;" type="submit" id="submit-btn"></input>
      </form>
    </body>
  </html>
''')

# 建立一個按鈕，以便呼叫JavaScript腳本
button = QPushButton("設定全名")

def js_callback(result):
    print(result)
    
def complete_name():
    # 透過view.page()函數取得一個QWebEnginePage物件，於是就可以存取整個Web頁面。
    # 此QWebEnginePage物件有一個非同步的runJavaScript()函數，要求一個callback函數
    # (槽函數)接收結果。
    view.page().runJavaScript('completeAndReturnName();', js_callback)
    
# 按鈕連接"complete_name"槽函數，按一下按鈕時便觸發訊號
button.clicked.connect(complete_name)

# 把QWebEngineView控制項和按鈕控制項載入layout佈局
layout.addWidget(view)
layout.addWidget(button)

# 顯示視窗和執行
win.show()
sys.exit(app.exec_())