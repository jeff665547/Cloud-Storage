# PyQt5 圖形與特效
# QSS的UI美化
# QSS偽狀態
# QSS偽狀態選擇器是以冒號開頭的選擇運算式，偽狀態選擇器限制當控制項處於某種狀態時，
# 才可以使用QSS規則，例如:hover，表示當滑鼠游標經過時的狀態。
# 他只能描述一個控制項，或者一個複合控制項內子控制項的狀態，所以僅能放在選擇器的最後面。
# 例如: QComboBox:hover{background-color:red;} 表示當滑鼠游標經過QComboBox時，將
# 其背景指定成紅色，該偽狀態:hover描述的是QComboBox的狀態。除了描述選擇器選擇的控制項外，
# 偽狀態還能描述子控制項選擇器的複合控制項，其內子控制項的狀態。
# 例如: QComboBox::drop-down:hover{background-color:red;} 表示當滑鼠游標經過QComboBox的
# 下拉箭頭時，變將下拉箭頭的背景變成紅色。
# 此外，偽狀態還能使用驚嘆號表示狀態，例如:hover表示滑鼠游標經過的狀態，
# 而:!hover表示滑鼠游標沒有經過的狀態。 可以同時使用多種偽狀態。
# 例如: QCheckBox:hover:checked { color:white }
# 表示當滑鼠游標經過選中的QCheckBox時，設定其文字的前景為白色。
# QSS提供很多偽狀態，有些只能應用於特定的控制項，具體有哪些偽狀態，詳見Qt的說明文件。
# Link: https://doc.qt.io/qt-5/stylesheet-reference.html
