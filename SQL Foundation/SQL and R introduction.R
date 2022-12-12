print("Hello R!!")
#在console 打 control + L 清空命令列的東西
# alt(option) + - 自動產生assign符號 " <- "

my_name = "Tony"

say_hello = function() {
  return("Hello R!!")
}

say_hello()

getwd() #回傳工作路徑
head(iris)
View(iris)
write.csv(iris, "iris.csv")
iris_csv = read.csv("iris.csv")
iris_csv = iris
plot(iris)#五個變數兩兩成對的散佈圖


install.packages("ggplot2")
library(ggplot2)

install.packages("dplyr")
library(dplyr)

#viewer產出html檔時可以看

q()

#建立R語言(外部應用程式，e.g. MySQL Workbench, R)與SQL資料庫的連結
#不同的主機會有不同的連結方式 MySQL@AWS RDS
#不同的語言會用不同的packages去連接  MSQL的話就是 RMySQL

install.packages("RMySQL")
library(DBI)  #Database Interface

con = dbConnect(RMySQL::MySQL(),     # 相當於前幾堂課MySQL的加號
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com", #主機
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

dbListTables(con)  #列出資料庫裡的所有表格

dbDisconnect(con)  #中斷連線

#把table 讀到R裡面,讀完之後就對資料庫進行離線
country <- dbReadTable(con, "country") # dbReadTable(connection 名稱,table name)
dbDisconnect(con)
View(country)

dim(country)
class(country) #回傳該物件是甚麼東西
nrow(country)  #回傳該物件的row數
ncol(country)  #回傳該物件的column數

head(country[, 1:6])
tail(country[, 1:6])  #回傳該物件資料最末6筆資料
names(country)     #回傳該物件資料所有的column names
summary(country)   #回傳該物件資料個個column的描述性統計
str(country)   #顯示詳細內容以及各個column的資料內型以及詳細內容

#讀入部分的資料集合
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

twn <- dbGetQuery(con, statement = "SELECT * FROM country WHERE Continent = 'Asia'")  #MySQL 的指令要包在statemtnt裡面
dim(twn)
sum(country$Continent == "Europe")

europe = dbGetQuery(con, statement = "
                    SELECT * FROM country WHERE Continent = 'Europe' 
                    ")  


europe = dbGetQuery(con, statement = '
                    SELECT * FROM country WHERE Continent = \'Europe\' 
                    ')    #注意，若在statement是使用"'" ，則在內部需要使用"\'" 來做跳脫字元，雙引號的話也是一樣

dim(europe)
class(europe)
write.csv(europe, "europe.csv")

dbDisconnect(con)

'I\'m loving it'

