#data�������,��r��(.csv, .txt, .tsv, .json)=> can be open with editor & Binary File(�G�i�� => �@�w�n�z�L�۲ŦX�����ε{���~�ॴ���})(.xlsx, .xls, .sas7bdat, .spss, .stata) => open with specific software
#.csv��
url <- "https://storage.googleapis.com/r_rookies/iris.csv" #�|�h�U������csv��
iris_csv_df <- read.table(url, sep = ",", header = TRUE)
head(iris_csv_df)

iries_df = read.csv(url, header = TRUE)
head(iries_df)
#read.table �M read.csv���t�O�A��Aread.table�γ~�����s�x�A�S�����w���j���Ÿ�
str(iries_df)
iris_csv_df <- read.table(url, sep = ",", header = TRUE, stringsAsFactors = FALSE)  #�Ƴ̫�@�檺factor ��character
str(iris_csv_df)  
iris_csv_df <- read.table(url, sep = ",", header = TRUE, colClasses = c("numeric", "numeric" ,"numeric","numeric", "character"))  #�����b�פJ���ɭԴN�i���C�@�檺�ܼ�����
str(iris_csv_df)

#.tsv��  ��tab�h���j���
url <- "https://storage.googleapis.com/r_rookies/iris.tsv" # �b���ݤW�x�s�F�@�� tsv �ɮ�
iris_tsv_df <- read.table(url, sep = "\t", header = TRUE)
head(iris_tsv_df)

#.txt��  ��:�h���j���
url <- "https://storage.googleapis.com/r_rookies/iris.txt" # �b���ݤW�x�s�F�@�� txt �ɮ�
iris_colon_sep_df <- read.table(url, sep = ":", header = TRUE)
head(iris_colon_sep_df)

#.json�� (Javascript Object Notation)
#�κ����s�������}�o���s���u��ܦn�}(��python�̪�dict�A���bRstudio���n�}�A�ݥ�list�~��h����)
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
#�]���ŦX�@��data.frame�ҥH�|�۰��ഫ���@��data.frame
head(friends_df)


#���ΰO�ƥ��άO�s���u��ݬݸ�������H�Ψ�۹�ϥΪ����j�Ÿ��ӨM�w�n�άƻ�sep�Ӱ��פJ
#�H�W����r�ɪ�Ū��

#.xlsx��
install.packages("readxl")
library(readxl)
iris_xlsx_df <- read_excel("C:/Users/jeff/Downloads/iris.xlsx")
head(iris_xlsx_df)

#.sas7bdat (SAS�����)
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
#filter �۷���OMySQL����where
twn <- filter(country, Code == "TWN")
#dplyer::filter()
AA = filter(country, Continent == "Asia" & Population > 100000000)

#Native R
logical_vec <- country$Continent == "Asia" & country$Population > 100000000
ans = country[logical_vec,]
#SQL �Y��SQL�g
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

#SELECT ��X�Q�n���ܼ�
library(dplyr)
country_names = select(country, Name)
dim(country_names)
head(country_names)


#mutate �s�W�@���ܼ�
country_density = country %>% #�ݥH�U����
  mutate(
    Pop_Density = Population / SurfaceArea
  )
names(country_density)

#pipe�B��� pipe_operator
age = c(18, 24, 30)
this_year = format(Sys.Date(), "%Y") #�^�ǲ{�b�q�����~���,format�O��ɶ��]���ۤv�Q�n���榡
#this_year = substr(Sys.Date(), start = 1, stop = 4) #�^���@�w������
#this_year = strsplit(as.character(Sys.Date()), split = "-")[[1]][1]
this_year_int = as.integer(this_year)
birth_year = this_year_int - age
#�W�������O���C�@�ӿ�X���O�U�@�檺��J(training funbctions �V�K��@�˦�b�@�_�A�i�ϥ�pipe�B���) "�n��J������ %>% �n��X����� " = "��X�����(�n��J������)"
#�n����dyplr�M��
birth_year = Sys.Date() %>%
  format("%Y") %>% #�]���W���W����bformat��
  as.integer() %>%
  `-` (age)
#�����g�k
summary(iris)
iris %>%
  summary()

twn = select(filter(country, Code == "TWN"), Name, Population)
twn = country %>%
  filter(Code == "TWN") %>%
  select(Name, Population)

twn



#Practice
#dplyr()�g�k
Asia = select(filter(country, Continent == "Asia" & Population > 100000000), Name, Population)
Asia = country %>%
  filter(Continent == "Asia" & Population > 100000000) %>%
  select(Name, Population) %>%
  arrange(desc(Population)) #arrange�����W���, desc()�ܻ���, ������SQL��order by

#SQL query  #�n���h�sDB
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

#join �s������
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

# ������ 
twn_jpn_country <- dbGetQuery(con, statement = "SELECT * FROM country WHERE Code in ('TWN', 'JPN')")

# �k����
twn_kor_city <- dbGetQuery(con, statement = "SELECT * FROM city WHERE CountryCode in ('TWN', 'KOR')")

dbDisconnect(con)

#���X����Х��ˬd��ƪ��ӼƥH�ΦU������
#�����s��(�涰) ��by�h�����w
joined_df <- inner_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))

#���~���s��  �⥪����檺��ƭȳ��O�d
joined_df <- left_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))

#�k�~���s��  ��k����檺��ƭȳ��O�d
joined_df <- right_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))

#���~���s��(�p��) �bSQL�S�������A��
joined_df <- full_join(twn_jpn_country, twn_kor_city, by = c("Code" = "CountryCode"))


#�ϥ� sqldf �M��
#�b R ���Y�g SQL �d��
install.packages("sqldf")
library(sqldf)
#sqldf("SQL���O")
big_asian_countries = sqldf("select Name, Population 
                            from country 
                            where Continent = 'Asia' and Population > 100000000
                            order by Population desc")


#R ø�ϥ\��
#���B��
plot(cars$speed, cars$dist, main = "Scatter", xlab = "speed", ylab = "Dist",
     col = "red", pch = 2)
#�ɶ��ǦC�u��
temperature <- round(runif(30) * 10 + 25)
dates <- as.Date("2017-06-01"):as.Date("2017-06-30")
dates <- as.Date(dates, origin = "1970-01-01")
plot(x = dates, y = temperature, type = "l") #x�\�ɶ�, y�\�Q�[�����ƭ��ܼ�
#Histagram  �ݤ@�Ӽƭ��ܼƴ��������p
n <- 100
par(mfrow = c(2, 1)) # �إߤ@�� 2x1 ������e��
hist(runif(n), main = paste("Distribution of", n, "uniformly distributed variables")) # �յۼW�[�H���ƪ��Ӽ� n
hist(rnorm(n), main = paste("Distribution of", n, "normally distributed variables")) # �յۼW�[�H���ƪ��Ӽ� n

random_norm = rnorm(10000)
hist(random_norm)

#Box plot�Y�@�Ӽƭȹ藍�P���O���������p�[�� (�ƭ��ܼ�vs���O�ܼ�)
str(iris)
par(mfrow = c(2, 2))
boxplot(iris$Sepal.Length ~ iris$Species, main = "Sepal length by species")
boxplot(iris$Sepal.Width ~ iris$Species, main = "Sepal width by species")
boxplot(iris$Petal.Length ~ iris$Species, main = "Petal length by species")
boxplot(iris$Petal.Width ~ iris$Species, main = "Petal width by species")

#Bar plot  �ݤ@�����O�ܼƴ��������p
tbl_gear <- table(mtcars$gear)  #��data��group�_�ӡA��excel�����϶s���R��
barplot(tbl_gear, main = "Vehicle counts by gear types",
        xlab = "Gear", ylab = "Vehicle counts")

#�i�H�j�Mr graph gallery �|���ܦh�귽
#�ϥ�Rmarkdown
#plotly 3D���ʦ��Ϫ�  shiny 2D���ʦ��Ϫ�
install.packages("plotly")
library(plotly)
packageVersion('plotly')

add_surface(plot_ly(z = ~volcano, colors = c("lightblue", "green", "yellow", "orange") )) #%>% add_surface()
p

#�ϥ�R markdown �h�}��(HTML�̶��Z)
#���X�Ӫ����G�ݭn��html���榡�h�x�s��
#�M��i�H�W�Ǩ�GitHub������
#�ϥ�Git Bash Here �h�W��
#�������ɱо� �Ѧ� https://read01.com/zh-tw/gxzQjK.html#.Wb80zsgjFdg 
#& 
#https://gogojimmy.net/2012/01/17/how-to-use-git-1-git-basic/
