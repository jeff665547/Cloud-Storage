print("Hello R!!")
#�bconsole �� control + L �M�ũR�O�C���F��
# alt(option) + - �۰ʲ���assign�Ÿ� " <- "

my_name = "Tony"

say_hello = function() {
  return("Hello R!!")
}

say_hello()

getwd() #�^�Ǥu�@���|
head(iris)
View(iris)
write.csv(iris, "iris.csv")
iris_csv = read.csv("iris.csv")
iris_csv = iris
plot(iris)#�����ܼƨ�⦨�諸���G��


install.packages("ggplot2")
library(ggplot2)

install.packages("dplyr")
library(dplyr)

#viewer���Xhtml�ɮɥi�H��

q()

#�إ�R�y��(�~�����ε{���Ae.g. MySQL Workbench, R)�PSQL��Ʈw���s��
#���P���D���|�����P���s���覡 MySQL@AWS RDS
#���P���y���|�Τ��P��packages�h�s��  MSQL���ܴN�O RMySQL

install.packages("RMySQL")
library(DBI)  #Database Interface

con = dbConnect(RMySQL::MySQL(),     # �۷���e�X���MySQL���[��
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com", #�D��
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

dbListTables(con)  #�C�X��Ʈw�̪��Ҧ�����

dbDisconnect(con)  #���_�s�u

#��table Ū��R�̭�,Ū������N���Ʈw�i�����u
country <- dbReadTable(con, "country") # dbReadTable(connection �W��,table name)
dbDisconnect(con)
View(country)

dim(country)
class(country) #�^�ǸӪ���O�ƻ�F��
nrow(country)  #�^�ǸӪ���row��
ncol(country)  #�^�ǸӪ���column��

head(country[, 1:6])
tail(country[, 1:6])  #�^�ǸӪ����Ƴ̥�6�����
names(country)     #�^�ǸӪ����ƩҦ���column names
summary(country)   #�^�ǸӪ����ƭӭ�column���y�z�ʲέp
str(country)   #��ܸԲӤ��e�H�ΦU��column����Ƥ����H�θԲӤ��e

#Ū�J��������ƶ��X
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "world",
                 host = "rsqltrain.ced04jhfjfgi.ap-northeast-1.rds.amazonaws.com",
                 port = 3306,
                 user = "trainstudent",
                 password = "csietrain")

twn <- dbGetQuery(con, statement = "SELECT * FROM country WHERE Continent = 'Asia'")  #MySQL �����O�n�]�bstatemtnt�̭�
dim(twn)
sum(country$Continent == "Europe")

europe = dbGetQuery(con, statement = "
                    SELECT * FROM country WHERE Continent = 'Europe' 
                    ")  


europe = dbGetQuery(con, statement = '
                    SELECT * FROM country WHERE Continent = \'Europe\' 
                    ')    #�`�N�A�Y�bstatement�O�ϥ�"'" �A�h�b�����ݭn�ϥ�"\'" �Ӱ�����r���A���޸����ܤ]�O�@��

dim(europe)
class(europe)
write.csv(europe, "europe.csv")

dbDisconnect(con)

'I\'m loving it'
