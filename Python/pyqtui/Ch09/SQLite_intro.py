# PyQt5 圖形與特效
# SQLite介紹
# 1. 什麼是SQLite
# SQLite 是一套羽量級的資料庫，提供自給自足、無伺服器、零設定、交易型的SQL資料集引擎，
# 部署的範圍極為廣泛。SQLite原始程式碼不受版權限制。
# SQLite的主要應用場景是作為手機程式以及小型桌面軟體的資料庫。
#
# 2. 安裝與使用SQLite
# SQLite的官方下載網址為http://www.sqlite.org/download.html ，
# 其中提供多種版本的SQLite，下載壓縮檔的名稱為sqlite-tools-win32-x86-xxxxxxx.zip，
# 下載後直接解壓縮到磁碟上，可以看到解壓縮後有splite3.exe。
# 
# 3. SQLite常用操作
# (1) 新建一個資料庫檔
# 先以cd命令切換到要建立資料庫的目錄，然後以sqlite3命令建立資料檔。
# 語法:
# sqlite3 DatabaseName.db  
# 上述命令是在目前的目錄下建立一個testDB.db檔案，該檔將被SQLite引擎作為資料庫。
# 以sqlite3命令成功產生資料庫檔後，將顯示"sqlite>"提示符號。
#
# (2) 查看以建立的資料庫檔
# 成功建立資料庫後，便可使用SQLite的.databases命令檢查資料庫清單。
#
# (3) 開啟已建立的資料庫檔
# 
