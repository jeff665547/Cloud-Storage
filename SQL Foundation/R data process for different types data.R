#data分成兩種,文字檔(.csv, .txt, .tsv, .json)=> can be open with editor & Binary File(二進位 => 一定要透過相符合的應用程式才能打的開)(.xlsx, .xls, .sas7bdat, .spss, .stata) => open with specific software
#.csv檔
url <- "https://storage.googleapis.com/r_rookies/iris.csv" #會去下載那個csv檔
iris_csv_df <- read.table(url, sep = ",", header = TRUE)
head(iris_csv_df)

iries_df = read.csv(url, header = TRUE)
head(iries_df)
#read.table 和 read.csv的差別再於，read.table用途較為廣泛，沒有限定分隔的符號
str(iries_df)
iris_csv_df <- read.table(url, sep = ",", header = TRUE, stringsAsFactors = FALSE)  #化最後一欄的factor 為character
str(iris_csv_df)  
iris_csv_df <- read.table(url, sep = ",", header = TRUE, colClasses = c("numeric", "numeric" ,"numeric","numeric", "character"))  #直接在匯入的時候就告知每一欄的變數類型
str(iris_csv_df)

#.tsv檔  用tab去分隔資料
url <- "https://storage.googleapis.com/r_rookies/iris.tsv" # 在雲端上儲存了一份 tsv 檔案
iris_tsv_df <- read.table(url, sep = "\t", header = TRUE)
head(iris_tsv_df)

#.txt檔  用:去分隔資料
url <- "https://storage.googleapis.com/r_rookies/iris.txt" # 在雲端上儲存了一份 txt 檔案
iris_colon_sep_df <- read.table(url, sep = ":", header = TRUE)
head(iris_colon_sep_df)

#.json檔 (Javascript Object Notation)
#用網路瀏覽器的開發者瀏覽工具很好開(似python裡的dict，但在Rstudio不好開，需用list才能去對應)
friends_json <- '{
  "genre": "Sitcom",
"seasons": 10,
"episodes": 236,
"stars": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
}'

install.packages("jsonlite")
library(jsonlite)
friends_list = fromJSON(friends_json)
friends_list$genre
friends_list$seasons
friends_list$stars
friends_list$stars[5]

starring_json <- '[
  {"character": "Rachel Green", "star": "Jennifer Aniston"},
{"character": "Monica Geller", "star": "Courteney Cox"},
{"character": "Phoebe Buffay", "star": "Lisa Kudrow"},
{"character": "Joey Tribbiani", "star": "Matt LeBlanc"},
{"character": "Chandler Bing", "star": "Matthew Perry"},
{"character": "Ross Geller", "star": "David Schwimmer"}
]'

friends_df <- fromJSON(starring_json)
#因為符合一個data.frame所以會自動轉換成一個data.frame
head(friends_df)


#先用記事本或是瀏覽工具看看資料類型以及其相對使用的分隔符號來決定要用甚麼sep來做匯入
#以上為文字檔的讀取

#.xlsx檔
install.packages("readxl")
library(readxl)
iris_xlsx_df <- read_excel("C:/Users/jeff/Downloads/iris.xlsx")
head(iris_xlsx_df)

#.sas7bdat (SAS資料檔)
install.packages("haven")
library(haven)
smoking_sas_data <- read_sas("http://storage.googleapis.com/r_rookies/smoking.sas7bdat")
head(smoking_sas_data)

###################################################################################
install.packages("dplyer")
library(dplyr)
library(DBI)
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

country <- dbReadTable(con, "country")
dbDisconnect(con)
dim(country)
?filter
#filter 相當於是MySQL中的where
twn <- filter(country, Code == "TWN")
#dplyer::filter()
AA = filter(country, Continent == "Asia" & Population > 100000000)

#Native R
logical_vec <- country$Continent == "Asia" & country$Population > 100000000
ans = country[logical_vec,]
#SQL 若用SQL寫
library(DBI)
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

ans <- dbGetQuery(con, statement = "select * from country where Continent = 'Asia' and Population > 100000000")
dbDisconnect(con)


library(DBI)
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

country <- dbReadTable(con, "country")
dbDisconnect(con)

#SELECT 選出想要的變數
library(dplyr)
country_names = select(country, Name)
dim(country_names)
head(country_names)


#mutate 新增一個變數
country_density = country %>% #看以下說明
  mutate(
    Pop_Density = Population / SurfaceArea
  )
names(country_density)

#pipe運算值 pipe_operator
age = c(18, 24, 30)
this_year = format(Sys.Date(), "%Y") #回傳現在電腦的年月日,format是把時間設成自己想要的格式
#this_year = substr(Sys.Date(), start = 1, stop = 4) #擷取一定的長度
#this_year = strsplit(as.character(Sys.Date()), split = "-")[[1]][1]
this_year_int = as.integer(this_year)
birth_year = this_year_int - age
#上面的指令中每一個輸出都是下一行的輸入(training funbctions 向鐵鏈一樣串在一起，可使用pipe運算值) "要放入的物件 %>% 要輸出的函數 " = "輸出的函數(要放入的物件)"
#要先裝dyplr套件
birth_year = Sys.Date() %>%
  format("%Y") %>% #因為上面上面放在format裡
  as.integer() %>%
  `-` (age)
#等價寫法
summary(iris)
iris %>%
  summary()

twn = select(filter(country, Code == "TWN"), Name, Population)
twn = country %>%
  filter(Code == "TWN") %>%
  select(Name, Population)

twn



#Practice
#dplyr()寫法
Asia = select(filter(country, Continent == "Asia" & Population > 100000000), Name, Population)
Asia = country %>%
  filter(Continent == "Asia" & Population > 100000000) %>%
  select(Name, Population) %>%
  arrange(desc(Population)) #arrange為遞增函數, desc()變遞減, 對應到SQL的order by

#SQL query  #要先去連DB
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")
big_asian_countries = dbGetQuery(con, statement = "
select Name, Population 
from country 
where Continent = 'Asia' and Population > 100000000
order by Population desc
                                 ")


#Native R script
logical_vector = country$Continent == "Asia" & country$Population > 100000000
big_asian_countries = country[logical_vector, c("Name", "Population")]
big_asian_countries = big_asian_countries[order(big_asian_countries$Population, decreasing = T),]


#summarise
country %>% summarise(Ttl_Pop = sum(as.numeric(Population)))
country %>%
  group_by(Continent) %>%
  summarise(Ttl_Pop = sum(as.numeric(Population))) %>%
  arrange(desc(Ttl_Pop))

#join 連接表格
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

# 左表格 
twn_jpn_country <- dbGetQuery(con, statement = "SELECT * FROM country WHERE Code in ('TWN', 'JPN')")

# 右表格
twn_kor_city <- dbGetQuery(con, statement = "SELECT * FROM city WHERE CountryCode in ('TWN', 'KOR')")

dbDisconnect(con)

#結合之後請先檢查資料的個數以及各項項目
#內部連結(交集) 用by去做指定
joined_df <- inner_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))

#左外部連結  把左邊表格的資料值都保留
joined_df <- left_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))

#右外部連結  把右邊表格的資料值都保留
joined_df <- right_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))

#全外部連結(聯集) 在SQL沒有此項服務
joined_df <- full_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))


#使用 sqldf 套件
#在 R 裡頭寫 SQL 查詢
install.packages("sqldf")
library(sqldf)
#sqldf("SQL指令")
big_asian_countries = sqldf("select Name, Population 
                            from country 
                            where Continent = 'Asia' and Population > 100000000
                            order by Population desc")


#R 繪圖功能
#散步圖
plot(cars$speed, cars$dist, main = "Scatter", xlab = "speed", ylab = "Dist",
     col = "red", pch = 2)
#時間序列線圖
temperature <- round(runif(30) * 10 + 25)
dates <- as.Date("2017-06-01"):as.Date("2017-06-30")
dates <- as.Date(dates, origin = "1970-01-01")
plot(x = dates, y = temperature, type = "l") #x擺時間, y擺想觀測的數值變數
#Histagram  看一個數值變數散布的情況
n <- 100
par(mfrow = c(2, 1)) # 建立一個 2x1 的網格畫布
hist(runif(n), main = paste("Distribution of", n, "uniformly distributed variables")) # 試著增加隨機數的個數 n
hist(rnorm(n), main = paste("Distribution of", n, "normally distributed variables")) # 試著增加隨機數的個數 n

random_norm = rnorm(10000)
hist(random_norm)

#Box plot某一個數值對不同類別的散布情況觀察 (數值變數vs類別變數)
str(iris)
par(mfrow = c(2, 2))
boxplot(iris$Sepal.Length ~ iris$Species, main = "Sepal length by species")
boxplot(iris$Sepal.Width ~ iris$Species, main = "Sepal width by species")
boxplot(iris$Petal.Length ~ iris$Species, main = "Petal length by species")
boxplot(iris$Petal.Width ~ iris$Species, main = "Petal width by species")

#Bar plot  看一個類別變數散布的情況
tbl_gear <- table(mtcars$gear)  #把data給group起來，似excel中的樞鈕分析表
barplot(tbl_gear, main = "Vehicle counts by gear types",
        xlab = "Gear", ylab = "Vehicle counts")

#可以搜尋r graph gallery 會有很多資源
#使用Rmarkdown
#plotly 3D互動式圖表  shiny 2D互動式圖表
install.packages("plotly")
library(plotly)
packageVersion('plotly')

add_surface(plot_ly(z = ~volcano, colors = c("lightblue", "green", "yellow", "orange") )) #%>% add_surface()
p

#使用R markdown 去開啟(HTML最順暢)
#做出來的結果需要用html的格式去儲存它
#然後可以上傳到GitHub的網頁
#使用Git Bash Here 去上傳
#相關文檔教學 參考 https://read01.com/zh-tw/gxzQjK.html#.Wb80zsgjFdg 
#& 
#https://gogojimmy.net/2012/01/17/how-to-use-git-1-git-basic/

