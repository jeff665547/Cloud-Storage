/*指令大小寫沒有關係，但要注意各個資料庫名稱以及表格名稱的大小寫*/
SHOW DATABASES;/*回傳資料庫系統*/

USE world;/*使用world資料庫*/

SHOW TABLES;/* 回傳一個資料庫裡面會有多個tables*/

/*SQL查詢結構*/
SELECT *  /* * 代表所有的欄位*/
	FROM world.countrylanguage; /*(DBMS.DBS)*/

/*Limit*/
/*先選幾列出來看(預覽表格)LIMIT 列數*/
SELECT *
  FROM world.country
  LIMIT 10;
  
/*選自己要看的欄位   將某一個欄位改名 as 新欄位名稱*/
SELECT Code as Country_Code,
	Name,
    Continent
    from world.country
    limit 10;

/*看表格有幾個row幾個column count(*)函數計算row */
/*查看city表格的row數*/
select count(*) as no_of_cities
	from world.city;

/*where*/
/*查看country表格的column數*/
SELECT count(*)
	from information_schema.COLUMNS
    where TABLE_NAME = "country";

/*從country表計算POP_Density (a New Variable)*/
select Name,
	Population /SurfaceArea as Pop_Density
    from world.country
    limit 10;

/*從country表計算POP_Density (a New Variable)，並加入篩選條件*/
SELECT name,
       Population /SurfaceArea as Pop_Density
  FROM world.country
  WHERE Population /SurfaceArea > 100
  #(注意: AS 敘述在 WHERE 敘述中不能立刻使用，因此這裡不能寫 "Pop_Density > 100")
  limit 10;  
  

/*從country表計算POP_Density (a New Variable)，並加入篩選條件*/
SELECT name,
       ROUND(Population /SurfaceArea, 2) AS Pop_Density #ROUND(, decimal) 函數可以調整小數點位數
  FROM world.country
  WHERE Population /SurfaceArea > 1000
  limit 10;

/*從country表中執行單一條件的觀察值(row)篩選 (類別、種類篩選)*/
select *
	FROM world.country
    WHERE Code = "TWN";

/*從country表中執行多個條件的觀察值(row)篩選 (類別、種類篩選)*/    
select *
	FROM world.country
    WHERE code IN ("TWN", "JPN", "KOR");

/*和上一個section的等價寫法*/    
select *
	FROM world.country
    WHERE code = "TWN"
    or code = "JPN"
    or code = "KOR";

/*從country表中執行多個條件的觀察值(row)篩選 (類別、種類篩選) (否定 負向篩選)*/
SELECT *
	FROM world.country
    where Continent NOT IN ('Asia', 'Africa', 'Oceania', 'Europe', 'Antarctica');
    
/*從country表中執行單一條件的觀察值(row)篩選 (數值單向區段篩選)*/
SELECT *
  FROM world.country
  WHERE Population > 200000000;
    
/*從country表中執行單一條件的觀察值(row)篩選 (數值雙向區段條件篩選)*/    
SELECT *
	FROM world.country
    WHERE Population BETWEEN 100 AND 10000;

/*和上一個section的等價寫法*/    
SELECT *
	FROM world.country
    WHERE Population >= 100
    AND Population <= 10000;

/*從country表中執行單一條件的觀察值(row)篩選 (類別、種類的開頭文字篩選)*/
SELECT *
  FROM world.country
  WHERE Name LIKE 'United%';
  
/*從country表中執行單一條件的觀察值(row)篩選 (類別、種類的結尾文字篩選)*/  
SELECT *
  FROM world.country
  WHERE Name LIKE '%land'; 

/*從country表中執行單一條件的觀察值(row)篩選 (類別、種類的特定頭尾文字篩選)*/    
SELECT *
  FROM world.country
  WHERE Name LIKE 'T%n';

/*從country表中執行單一條件的觀察值(row)篩選 (類別、種類的特定字數篩選, 一個"_"代表一個字母)*/    
SELECT *  
  FROM world.country
  WHERE Name LIKE '__';
  
/*從country表中執行單一條件的觀察值(row)篩選 (類別、種類的特定字母組合篩選, 開頭數來第二字母為a)*/    
SELECT *  
  FROM world.country
  WHERE Name LIKE '_a%';

/*利用小括號達到類似四則運算中的優先效果*/
SELECT name,
       continent,
       population
    FROM world.country
    WHERE (continent = 'Asia' OR continent = 'Europe') 
    AND population > 10000000;

/*Order By*/
/*從country表中執行觀察值的大小排列 */
/*(依sum_pop變數的大小排列, DESC為遞減, 搭配limit選出符合條件的前10名)*/
SELECT name,
       population
	FROM world.country
	WHERE continent = 'Europe'
	ORDER BY population desc
	LIMIT 10;

#Practice Start
SELECT Name, 
	Continent,
    Region
	FROM world.country
    WHERE Continent = "Asia"
    AND Region = "Eastern Asia";
    
select Name,
	Continent
	FROM world.country
    WHERE Continent = "Europe"
    AND Name LIKE '___';
    
SELECT Name,
  Population,
  Population /SurfaceArea as Density  
  FROM world.country
  WHERE Population > 200000000;
#Practice End


/*從country表中執行觀察值的大小排列 (依sum_pop變數的大小排列, 預設是遞增)*/
SELECT name,
       population
	FROM world.country
	WHERE continent = 'Europe'
	ORDER BY population;

/*從country表中執行觀察值的大小排列 (依sum_pop變數的大小排列, DESC為遞減, 搭配limit選出符合條件的前10名)*/
SELECT name,
       population
	FROM world.country
	WHERE continent = 'Europe'
	ORDER BY population desc
	LIMIT 10;
    
    
/*Group By敘述*/
/*Group By後面的變數在執行完後不會出現重複的值(unique value)，即一個種類只會出現在一筆觀測值上，
該變數通常會搭在select後方，順便把分類的細項給印出來*/
/*從country表中依region去分組，並在region各組中執行其他命令*/
/*(依照各個Region去篩選出Population > 100000的國家數，並依照國家數多到少來排列Region)*/
SELECT Region,
       count(*) as no_countries
  FROM world.country
  WHERE Population > 100000  #此行是針對每個observation(country)去做篩選
  GROUP BY Region
  order by no_countries DESC;


/*子查詢*/
/*找出人口數比澳國多的國家*/
/*先知道澳大力亞人口有多少*/
SELECT population
	FROM world.country
	WHERE name = 'Australia'; /*output為18886000*/

/*然後再寫一個查詢*/
SELECT name
	FROM world.country
	WHERE population >= 18886000;    

/*把上面的兩個section的code合而為一*/
SELECT name
	FROM world.country
	WHERE population >= (
		SELECT population
			FROM world.country
			WHERE name = 'Australia' /*output為18886000*/
    );    


/*找出人均 gnp 比英國高的歐洲國家*/
/*先知道英國人均 GDP 多少*/
SELECT gnp/population
	FROM world.country
	WHERE name = 'United Kingdom'; /*output為0.023117*/

/*然後再寫一個查詢*/
SELECT name
	FROM world.country
	WHERE continent = 'Europe' AND
		gnp/population >= 0.023117;
      
/*把上面的兩個section的code合而為一*/
SELECT name
	FROM world.country
	WHERE continent = 'Europe' AND
		gnp/population >= (
			SELECT gnp/population
				FROM world.country
				WHERE name = 'United Kingdom' /*output為0.023117*/
        );

/*找出與阿根廷、澳洲同洲的國家、洲別*/
/*先知道阿根廷、澳洲在哪個洲*/
SELECT continent
	FROM world.country
	WHERE name IN ('Argentina', 'Australia'); /*South America, Oceania*/

/*然後再寫一個查詢*/
SELECT name,
       continent
	FROM world.country
	WHERE continent IN ('South America', 'Oceania');

/*把上面的兩個section的code合而為一*/
SELECT name,
       continent
	FROM world.country
	WHERE continent IN (
		SELECT continent
			FROM world.country
			WHERE name IN ('Argentina', 'Australia') /*output為South America, Oceania*/
    );


/*子查詢 -- ALL      用 ALL 對一個子查詢為列表的結果進行 >=, >, <, <= 比較 
e.g. A >= B 意即 B 列表中的每一個元素都要小於 A 元素(A is bigger than or equal to every elements in B) */
/*底下意思為找出世界上最大的國家(以人口計算)*/
SELECT name
	FROM world
	WHERE population >= ALL(SELECT population
								FROM world
								WHERE population>0);   #在子查詢的條件中使用 population>0，因為有些國家的記錄中，人口是沒有填入，只有 null值。


/*summerize 聚合函數、運算 (Aggregate Functions)*/
/*計算觀測值數目*/
SELECT count(*)
	from world.country;

/*計算欄位的加總值(各國的總人口數加總)*/
SELECT SUM(population) AS Sum_Pop
  FROM world.country;
  
/*回傳相異continent的分類，可以看有哪些分類，可以用來做資料品質的檢核*/  
/*重複地觀測值會被省略成一筆*/
SELECT DISTINCT(continent) 
  FROM world.country;

/*回傳相異continent的分類數目*/
SELECT count(DISTINCT(continent)) 
  FROM world.country;
  
/*將上面的變數存成一個新的變數*/
SELECT count(DISTINCT(continent)) as how_many_regions 
  FROM world.country;

/*計算欄位的平均值(各國的總人口數平均)*/
select avg(Population)  
	from world.country;

/*回傳欄位中出現的最小值*/  
select min(Population)  /*最小值*/
	from world.country;

/*回傳欄位中出現的最大值*/  
select max(Population)   /*最大值*/
	from world.country;

/*多個運算*/
select name, Population, SurfaceArea, Population/SurfaceArea, max(Population) 
	from world.country;


/*Having*/
/*聚合變數的篩選*/
/*where 是針對聚合前的篩選, where則是針對聚合後的變數去篩選*/
/*對於聚合運算函數所做出來的變數條件指令要使用 having  聚合變數的條件*/
/*找出總人口數超過 1 億的洲(Continent)*/
SELECT Continent
       ,SUM(Population) AS Sum_of_Population
  FROM world.country
  GROUP BY Continent
  having Sum_of_Population > 100000000; 


/*文字型的函數*/
/*substr() 函數可以擷取文字*/
select 
	substr(Name, 1, 3) as short_name /*從第1個字母開始選，然後截的長度為3*/
    from world.country;

select 
	substr(Name, 2, 3) as short_name /*從第2個字母開始選，然後截的長度為3*/
    from world.country;

/*LENGTH() 函數可以得知文字長度*/
SELECT name,
       LENGTH(name)
	from world.country;

/*LEFT(, n) 函數可以取出由左邊數來的 n 個文字*/
SELECT name,
       LEFT(name, 3)
	from world.country;
    
/*CONCAT(欄位(變數)1, "連接符號", 欄位(變數)2)   函數可以連結變數、符號和文字*/
/*CONCAT(欲連接的符號、文字或欄位1, 欲連接的符號、文字或欄位2, 欲連接的符號、文字或欄位3, ......)*/
SELECT Name 
    ,Region, Continent, CONCAT(Region, ', ', Continent) AS Reg_Cont
    FROM world.country
    LIMIT 10;
    
/*將Name全部給大寫化，lower 是小寫化，reverse是倒過來*/
SELECT UPPER(Name) AS Cap_Name 
    , Name
    FROM world.country
    LIMIT 10;

/*Practice Start*/
select
	Continent,
	sum(Population) as sum_pop
    from world.country
    order by sum_pop DESC;

select
	Continent,
	sum(Population) as sum_pop
    from world.country
    group by Continent 
    order by sum_pop DESC;

select
	Continent,
	count(*) as no_countries
    from world.country
    group by Continent
    order by no_countries DESC;
    
select *
	from world.country
    where Continent = 'North America';
    
    
SELECT Region,
       COUNT(*) AS no_countries
  FROM world.country
  WHERE Population > 10000000
  GROUP BY Region
  order by no_countries DESC;
/*Practice End*/


/*多個資料的串檔與併檔*/
/*Schema文件會儲存資料與資料之間的關係以及關聯性*/
/*在Schema文件中 PK(主鍵) 代表Primary key 記錄資料層級的欄位，此欄位的特徵是每個觀測值都有獨特的值，不會重複
  e.g. 投開票所編號(每個開票所為此資料的紀錄層級), 各個里的名稱(每個里為此資料的紀錄層級)*/
/*               FK(外鍵) 代表Foreign key 用來連接其他表格的欄位*/
/*Join / Inner Join 描述*/
/*EXCEL的(vlookup()) join 自動合成(結合)table(增加column數)、串檔*/
select *
	from world.city
    limit 10;

/*左表格*/
SELECT * FROM world.country
    WHERE Name IN ('Taiwan', 'Japan');

/*右表格*/
SELECT * FROM world.city
    WHERE CountryCode IN ('TWN', 'KOR');

/*取左表格（台灣、日本）跟右表格（台灣、南韓）的交集（台灣）*/
/*Inner Join 內部聯結 (JOIN 意思同 Inner JOIN)*/
/*join 和 on 必須搭配使用*/
/*重要: 利用多個join on 語句可以一次串很多個檔*/       
SELECT world.country.*, world.city.*  #輸入串完檔後要顯示出來的欄位(建議使用原資料表的資訊表達(避免欄位名稱在不同資料中重複))
	from world.country  #待串聯的資料表 A
    join world.city     #待串聯的資料表 B
    on world.city.CountryCode = world.country.code   #資料表A和資料表B的交互對照欄位(FK)
    #此時若要再串其他檔只需接著在下面掛上 join 資料表 C 
    #                                     on   資料表A和資料表C的交互對照欄位(FK)
	where world.city.CountryCode = "TWN";      #輸入串完檔後的篩選條件(建議使用原資料表的資訊表達(避免欄位名稱在不同資料中重複))

/*搭配子查詢的架構*/
SELECT left_tbl.*
      ,right_tbl.*
    FROM (                                   #左表格 子查詢
        SELECT *
        FROM world.country
        WHERE Code IN ('TWN', 'JPN')
    ) left_tbl                               #左表格暱稱名稱
    INNER JOIN (                     #JOIN 或是 INNER JOIN 都行 意思一樣
        SELECT * FROM world.city             #右表格 子查詢
        WHERE CountryCode IN ('TWN', 'KOR')
    ) right_tbl                              #右表格暱稱名稱
    ON left_tbl.Code = right_tbl.CountryCode;


/*LEFT JOIN  左外部聯結*/
/*RIGHT JOIN 右外部聯結*/
/*左表格*/
SELECT * 
	FROM world.country
    WHERE Name IN ('Taiwan', 'Japan');

/*右表格*/
SELECT * 
	FROM world.city
    WHERE CountryCode IN ('TWN', 'KOR');

/*內部聯結*/
/*留下兩表格交集部分的資料*/
SELECT left_tbl.*
      ,right_tbl.*
    FROM (
        SELECT *
        FROM world.country
        WHERE Code IN ('TWN', 'JPN')
    ) left_tbl
    INNER JOIN (     /*Inner join 只會把左右兩個表個交集的部分作保留*/
        SELECT * FROM world.city
        WHERE CountryCode IN ('TWN', 'KOR')
    ) right_tbl
    ON left_tbl.Code = right_tbl.CountryCode;

/*左外部聯結*/
/*留下所有左表格（台灣、日本）的資料*/
SELECT left_tbl.*
      ,right_tbl.*
    FROM (
        SELECT *
        FROM world.country
        WHERE Code IN ('TWN', 'JPN')
    ) left_tbl
    LEFT JOIN (     /*LEFT join 會把左右兩個表格作合併但會以左表格的資訊為主(保留左表格所有資料)*/
        SELECT * FROM world.city
        WHERE CountryCode IN ('TWN', 'KOR')
    ) right_tbl
    ON left_tbl.Code = right_tbl.CountryCode;
#因在city資料表中沒有JPN的相關資料 所以JPN只有原始在country資料表的一筆資料

/*右外部聯結*/
/*留下所有右表格（台灣、韓國）的資料*/
SELECT left_tbl.*
      ,right_tbl.*
    FROM (
        SELECT *
        FROM world.country
        WHERE Code IN ('TWN', 'JPN')
    ) left_tbl
    RIGHT JOIN (     /*RIGHT join 會把左右兩個表格作合併但會以右表格的資訊為主(保留右表格所有資料)*/
        SELECT * FROM world.city
        WHERE CountryCode IN ('TWN', 'KOR')
    ) right_tbl
    ON left_tbl.Code = right_tbl.CountryCode;
#因在country資料表中沒有KOR的相關資料 所以KOR只有原始在city資料表的地方有資料，其餘地方都是NULL


/*full join*/
/*My SQL 不支援full join (聯集)*/
/*full join 就是同時保留兩個表格的資訊 沒有資料的全部都補NULL */


/*Union 垂直整併(併檔、增加row)*/
/*兩個要併檔的表格 column 數目必須要一樣，但欄位名稱可以不相同*/
/*e.g. 表格一使用region欄位, 但表格二使用Name欄位*/
SELECT Region  
    FROM world.country
    WHERE Code = 'TWN'   #Taiwan
UNION
SELECT Name
    FROM world.city
    WHERE CountryCode = 'TWN';   #台灣裡的城市


/*Exercise*/
/*1*/
select Continent,
	sum(Population) as Sum_of_Population
    from world.country
    WHERE Continent IN ('Asia', 'Europe', 'South America')
    group by Continent;
    
/*2*/
select Continent,
	MAX(Population)
    from world.country
    group by Continent;
    
/*3*/
select Name, Continent
    from world.country
    where Continent IN (
		select Continent
			from world.country
			where NAME IN ('Argentina', 'Australia')
    )
    ORDER BY NAME;
    
/*4*/
SELECT left_tbl.Name as City
      ,right_tbl.Name as Country
      ,right_tbl.Continent
    FROM (
        SELECT *
        FROM world.city
        WHERE CountryCode = 'TWN'
    ) left_tbl
    LEFT JOIN (
        SELECT * FROM world.country
        WHERE Code = 'TWN'
    ) right_tbl
    ON left_tbl.CountryCode = right_tbl.Code;

/*5*/
SELECT left_tbl.Name as City
      ,right_tbl.Name as Country
      ,right_tbl.Continent
    FROM (
        SELECT *
        FROM world.city
        WHERE CountryCode in ('TWN', 'USA')
    ) left_tbl
    LEFT JOIN (
        SELECT * FROM world.country
        WHERE Code in ('TWN', 'USA')
    ) right_tbl
    ON left_tbl.CountryCode = right_tbl.Code;
/*Exercise End*/


#####################################總結######################################
/*SQL 查詢敘述的先後順序 (SQL 寫法, SQL 指令擺放順序)*/
#SELECT ... (as, round, {聚合函數: count, sum, ... },  {文字型函數: substr, length, ...}, 子查詢:(SELECT ...))
#    FROM ...
#    JOIN ...  ON ...
#    WHERE ... ({!=, =, >, >=, ... (ALL 接列表)}, in, not, or, and, between _ and _, like, 優先執行(), 子查詢:(SELECT ...))
#    GROUP BY ...
#    HAVING ...
#    ORDER BY ... (desc)
#    LIMIT
#UNION ...
#
#
#{聚合函數: count, sum, avg, min, max, distinct}
#{文字型函數: substr, length, left, concat, upper, lower, reverse}



/*R to SQL*/
##安裝及匯入套件
#install.packages("RMySQL")
#library(DBI)
#
##建立連線
#con = dbConnect(RMySQL::MySQL(),
#                dbnmame = "資料庫名稱",
#                host = "資料庫存放位址",
#                port = "資料庫存放通道(通訊埠)",
#                user = "帳號",
#                password = "密碼")
#
##把資料庫中的某個特定資料集丟給R物件
#name = dbReadTable(con, name = "資料集名稱")   
#
##從R中下MySQL指令
#SQL_query = "SQL 查詢語句 (e.g.: SELECT * FROM country WHERE Name IN ("Taiwan", "Japan"))"
#query = dbGetQuery(con, statement = SQL_query)  #query即是查詢結果
#
##R語言裡面的join語法 -- merge
#inner_joined = merge(資料集A, 資料集B, by.x = "資料集A中用來和資料集B對照的欄位名稱", by.y = "資料集B中用來和資料集A對照的欄位名稱")
#left_joined = merge(資料集A, 資料集B, by.x = "資料集A中用來和資料集B對照的欄位名稱", by.y = "資料集B中用來和資料集A對照的欄位名稱", all.x = TRUE)
#right_joined = merge(資料集A, 資料集B, by.x = "資料集A中用來和資料集B對照的欄位名稱", by.y = "資料集B中用來和資料集A對照的欄位名稱", all.y = TRUE)
#full_joined = merge(資料集A, 資料集B, by.x = "資料集A中用來和資料集B對照的欄位名稱", by.y = "資料集B中用來和資料集A對照的欄位名稱", all.x = TRUE, all.y = TRUE)
#以上直接輸入物件名稱即可得到查詢結果(data.frame格式)
#
##拿完資料建議就斷開連線
#dbDisconnect(con)



/*Python to SQL*/
##安裝及匯入套件
#!pip install pymysql
#!pip install pandas
#import pymysql
#import pandas as pd
#
##建立連線
#host = "資料庫存放位址"
#port = "資料庫存放通道(通訊埠)"
#user = "帳號"
#passwd = "密碼"
#db_name = "資料庫名稱"
#con = pymysql.connect(host, prot = port, user = user, passwd = passwd, db = db_name)
#
#
##從Python中下MySQL指令
#SQL_query = "SQL 查詢語句 (e.g.: SELECT * FROM country WHERE Name IN ("Taiwan", "Japan"))"
#query = pd.read_sql(SQL_query, con)  #query即是查詢結果
#
#
##Python語言裡面的join語法 -- merge
#inner_joined = pd.merge(資料集A, 資料集B, left_on = "資料集A中用來和資料集B對照的欄位名稱", right_on = "資料集B中用來和資料集A對照的欄位名稱")
#left_joined = pd.merge(資料集A, 資料集B, left_on = "資料集A中用來和資料集B對照的欄位名稱", right_on = "資料集B中用來和資料集A對照的欄位名稱", how = "left")
#right_joined = pd.merge(資料集A, 資料集B, left_on = "資料集A中用來和資料集B對照的欄位名稱", right_on = "資料集B中用來和資料集A對照的欄位名稱", how = "right")
#full_joined = pd.merge(資料集A, 資料集B, left_on = "資料集A中用來和資料集B對照的欄位名稱", right_on = "資料集B中用來和資料集A對照的欄位名稱", how = "outer")
#以上直接輸入物件名稱即可得到查詢結果(data.frame格式)
#
##拿完資料建議就斷開連線
#con.close()   #con為建立連線步驟的物件