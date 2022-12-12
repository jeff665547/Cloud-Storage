#Pandas套件、Numpy套件
import pandas as pd
import numpy as np
#使用Python的dict物件在轉換為pandas表格時會較為容易且快速

#表格式資料
ticker_name = [
        "大立光",
        "國巨",
        "矽力",
        "旭隼",
        "祥碩"
        ]

price = [
        5145,
        836,
        706,
        540,
        499.5
        ]

#Original python(只能進行純量的運算)
stock_dict = {
        "ticker_name": ticker_name,
        "price": price
        }

stock_dict
list(enumerate(ticker_name)) 

#Pandas (pd)(能進行向量的運算)
#使用Python的dict物件在轉換為pandas表格時會較為容易且快速
df = pd.DataFrame(stock_dict, columns = ["ticker_name", "price"])
df.head(n = 3)

#矩陣資料運算
import random

heights = [random.randint(150, 180) for _ in range(10)]  #(cm)
weights = [random.randint(50, 80) for _ in range(10)]   #(kg)

#BMI = weight(kg)/height**2(m)
#compute BMI of these 10 people

#Original python(只能進行純量的運算)
heights_m = [_/100 for _ in heights]
BMI = [ float("{:.2f}".format(w/h**2)) for w, h in zip(weights, heights_m)]

#Numpy (np)(能進行向量的運算)
heights_arr = np.array(heights)
type(heights_arr)    #一個有n維(d)的numpuy陣列
weights_arr = np.array(weights)

bmi_arr = weights_arr / (heights_arr/100)**2
np.around(bmi_arr, decimals = 2)   #將round函數作用在array上

##################################################################
#NumPy (Numerical Python)
#資料結構: numpy.ndarray
#有別於list，array裡面只能容納單一一種型別的資料(e.g. 全部都是數字、文字)
#ndarray的特性
#-向量元素級別(element-wise operation)
#-具有bool篩選的特徵
#-索引值的選擇很彈性
#-可拓展至無限維度
heights = [random.randint(150, 180) for _ in range(10)]  #(cm)
print(type(heights))
heights_arr = np.array(heights)
print(type(heights_arr))

heights_arr/100  #element-wise operation

is_tall = heights_arr > 170
print(type(is_tall))

heights_arr[is_tall]
heights_arr[heights_arr < 170]

heights_arr[0]
heights_arr[-1]
heights_arr[:3]
heights_arr[:4:2]
heights_arr[[2, 6, 8, 9]]

heights_arr.ndim  #看維度
heights_arr.shape #看長度

heights_arr.reshape(2, 5)  #reshape成2 x 5 的matrix
np.concatenate([heights_arr,[np.NaN, np.NaN]])   #原始array加入新的值(2個missing value)
heights_arr.reshape(2, 5).ndim  #row為dim
heights_arr.reshape(2, 5).shape  #row為dim  column為長度

np.arange(10)   #將range函數作用在array上
np.arange(10, dtype = float)   #生出來的都是float

np.linspace(0, 9, 20)  #從0到9(注意:9有包含)分割成20個均等的數值(等分切割, 20個數值包含頭尾(0, 9))
                       #和R裡面的seq相似

np.random.randint(0, 10, 5)  #從0到9隨機產生5個整數

np.zeros(5)   #產生5個0
np.zeros(5, dtype = int)   #產生5個整數0

np.ones(5)   #產生5個1
np.ones(5, dtype = int)   #產生5個整數1

#array單一型別(自動轉換成可以共通的資料型態e.g. string)
my_list = [8.7, True, "Luke Skywalker"]
print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))

my_array = np.array(my_list)
print(type(my_array[0]))
print(type(my_array[1]))
print(type(my_array[2]))

#Numpy常用的方法和屬性{obj.ndim, obj.size, obj.dtype, obj.T, np.transpose(), 
#obj.dot(), np.dot(), obj.reshape(), obj.max(axis), obj.min(axis), obj.mean(axis), 
#obj.std(axis), np.arange(dtype), np.array([ ]), np.identity(dtype), np.linalg.inv()}
#屬性
#.ndim  #告訴維度
#.size  #告訴使用者array的長度(裡面的元素有多少個)
heights_arr.size
#.shape  #告訴外觀
#.dtype  #告訴型別
#.T  #T代表轉置 將矩陣轉置
#np.transpose() #和上一個相同
my_mat = heights_arr.reshape(2, 5)
my_mat.T
my_mat[my_mat > 170]  #選完後會自動轉成一個維度
my_mat[[0, 0], [2, 1]]   #選多個特定值的選法(x放一邊 y放一邊)
#.dot()  #矩陣的乘法, 和R裡的%*%相似
mat_1 = np.arange(1, 5).reshape(2, 2)
mat_2 = np.arange(5, 9).reshape(2, 2)
mat_1*mat_2 #term by term product
np.dot(mat_1, mat_2)  #product for matrix
mat_1.dot(mat_2)   #和上面的結果相同
mat_2.dot(mat_1)   #矩陣的乘法無交換率

##九九乘法表
mat_1 = np.arange(1, 10, dtype = int).reshape(9, 1)
mat_2 = np.arange(1, 10, dtype = int).reshape(1, 9)
mat_1.dot(mat_2)
##Practice
#u = (4, -4, 3), v = (4, 2, 4),  t(u)*v = ?
#A = 1, 2, 3 , I is identity matrix AI, IA?
#    4, 5, 6
#    7, 8, 9

uu = np.array([4, -4, 3]).reshape(3, 1)
uu = np.array([4, -4, 3]).reshape(-1, 1)   #跟打reshape(3, 1)效果一樣
vv = np.array([4, 2, 4]).reshape(3, 1)
uu.T.dot(vv)[0, 0]

AA = np.arange(1, 10).reshape(3, 3)
II = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1]).reshape(3, 3)
II = np.eye(3, dtype = int)   #和上面那行的效果相同  eye 為 Identity 諧音
II = np.identity(3, dtype = int)   #和上面那行的效果相同
AA.dot(II)
II.dot(AA)

#np.linalg.inv()   #計算反矩陣
#.reshape()
#.max()  #最大值
#.min()  #最小值

heights_arr.reshape(2, 5).max()  #把整個array中的最大值給回傳回來
heights_arr.reshape(2, 5).max(axis = 0)  #根據每個column(axis = 0)中的最大值給回傳回來
heights_arr.reshape(2, 5).max(axis = 1)  #根據每個row(axis = 1)中的最大值給回傳回來
heights_arr.reshape(2, 5).min(axis = 0)  #根據每個column(axis = 0)中的最小值給回傳回來
heights_arr.reshape(2, 5).min(axis = 1)  #根據每個row(axis = 1)中的最小值給回傳回來

#.mean()  #計算平均數
heights_arr.reshape(2, 5).mean()  #把整個array中的平均數給回傳回來
heights_arr.reshape(2, 5).mean(axis = 0)  #根據每個column(axis = 0)計算mean
heights_arr.reshape(2, 5).mean(axis = 1)  #根據每個row(axis = 1)計算mean




#Pandas
#Panel Data Analysis
#Providing labeled data structures similar to R data.frame objects
#很多個長度相同的array一起拼湊起來   但每個array可以擁有各自的資料類型(by column來區分)
#pip install pandas
#資料結構:Series(加強版的一維ndarray(多了前面的索引值(標籤))), DataFrame(加強版的二維ndarray),
#        Panel(加強版的三維ndarray)(較少用)
#概念: 多個series可以集合成一個daraframe,
#      多個dataframe可以集合成一個panel
#DataFrame的六個基本技法
#filter(篩選), 
#select(選擇): .loc(), iloc(), 
#mutate(創建變數), 
#arrange(排序): .sort_values(), .sort_index(), 
#summarize(摘要), 
#group by(分組): .groupby()

#Pandas 其他功能:
##輸入輸出
##視覺化

#創建一個Series(從list, np.array建立)
import pandas as pd

avengers = ["Iron Man", "Captain America", "Spider Man", "Scarlet Witch", 
            "Black Widow"]
ser = pd.Series(avengers)
type(ser)
#series繼承了所有nd.array的所有特性 {pd.Series([ ]) ,Series.index, Series.index, 
#Series.map([ ]), {Series.str.upper(), Series.str.contain(" ")}, Series.idxmax(),
#Series.idxmin()}
ser #會預設索引值
avenger_names = ["Tony Stark", "Steve Rogers", "Peter Parker", "Wanda Maximoff",
                 "Natasha Romanoff"]
ser_w_name = pd.Series(avengers, index = avenger_names)

ser_w_name.index
ser.values
ser.index

#彈性選取
ser_w_name[0]
ser_w_name[-1]
ser_w_name[::2]
ser_w_name[[0, 3, 4]]
ser_w_name["Tony Stark"]
ser_w_name["Natasha Romanoff"]
ser_w_name[["Tony Stark", "Wanda Maximoff", "Natasha Romanoff"]]
ser_w_name.str.upper()  #將每一個value都變大寫

#Practice:
#bmi < 18: underweight
#18 <= bmi < 25: normal
#25 <= bmi < 30: overweight
#30 <= bmi: obese
#pd.map(要執行的公式(不加括號), NAN值的處理方式)
bmi_ser = pd.Series(bmi_arr)
def get_bmi_label(bmi):
    if(bmi < 18):
        return("underweight")
    elif(18 <= bmi < 25):
        return("normal")
    elif(25 <= bmi < 30):
        return("overweight")
    else:
        return("obese")
        
bmi_labels = bmi_ser.map(get_bmi_label , na_action=None).values
bmi_ser.index = bmi_labels


#DataFrame的資料結構
from pyquery import PyQuery as pq

def get_top_100():
    """
    Get top 100price
    """
    ticker_name_css = ".name a"
    price_css = ".name+ td"
    stock_url = "https://tw.stock.yahoo.com/d/i/rank.php?t=pri&e=tse&n=100"
    html_doc = pq(stock_url)
    ticker_name = [tn.text for tn in html_doc(ticker_name_css)]
    price = [float(p.text) for p in html_doc(price_css)]
    return ticker_name, price

ticker_name, price = get_top_100()
#創建DataFrame的兩種方式
#第一種 #從list, np.array, pd.Series建立
df = pd.DataFrame()  #先建立一個空的dataframe
df["ticker_name"] = ticker_name  #直接指定內容
df.head()  #show 出前5個觀測值
df["price"] = price
df.shape

#第二種 #從dict建立
stock_dict  = {
        "ticker_name": ticker_name,
        "price": price
        }
df = pd.DataFrame(stock_dict, columns = ["ticker_name", "price"])  #可指定欄位順序
df.shape
type(df)

#DataFrame資料架構的層狀關係
# list/ndarray
#   Series
#     DataFrame

df[["ticker_name"]]  #出來是DataFrame
df["ticker_name"]   #單選一個dataframe的column出來後會是一個series
df["ticker_name"].index  #出來的是ndarray
df["ticker_name"].values[0]  #出來的是單一值


#DataFrame基本技法 {df.loc[ , ], df.iloc[ , ], df.reset_index(drop), 
#df.sort_index(ascending), df.sort_values([ ], ascending), df.max(axis), df.std(axis),
#df.min(axis), df.set_index([ ]), df.groupby(), {df.groupby([ ])[ ].max(), 
#df.groupby([ ])[ ].mean(), df.groupby([ ])[ ].nlargest()}}
#新增一個欄位(變數) mutate操作
ticker_name[:5]
ticker_name[0].split()

#把ticker和name給分開
ticker, name = [], []
for tn in ticker_name:
    ticker.append(tn.split()[0])
    name.append(tn.split()[1])

ticker[:5]
name[:5]

df = pd.DataFrame()
df["ticker"] = ticker
df["name"] = name
df["price"] = price
df.head()

#map() + function
def get_label(name):
    return("KY" in name)        
#or 上下等價寫法  下方為lambda表達式
lambda x: "KY" in x
df["ky_listed"] = df["name"].map(lambda x: "KY" in x)
df.head()

df["ky_listed"] = df["name"].str.contains("KY")

#filter  (針對(樣本)觀測值做)篩選 (row selection)
#需先生成一個column來指示哪一個row為符合篩選條件的row
df[df["ky_listed"]]  #選擇有KY的
df[df["ky_listed"] == False]  #選擇沒有KY的
df[~df["ky_listed"]]   #選擇沒有KY的

#select   (變數)選擇 (column selection)
df["ticker"] #選出來為Series的形式  長度為100的series
df[["ticker"]] #選出來仍為DataFrame的形式  100x1的dataframe
df[["ticker", "ky_listed"]].head()  #選多個column

#  .loc[] (原表格資訊),  &  .iloc[] (新的索引值資訊)  同時選擇變數以及觀測值
ky_stocks = df[df["ky_listed"]]
ky_stocks.head()
#若要提取上表中第3列的資訊
ky_stocks.head().loc[13, :] #需輸入要提取的欄跟列位置(原始表格的資訊)
                            #並用series回傳回來(若有多個值的話)
ky_stocks.head().loc[13, "price"] #需輸入要提取的欄跟列位置(原始表格的資訊)
                                  #並用series回傳回來(若有多個值的話)  
#":"代表全選
ky_stocks.head().iloc[2, :]  #使用iloc採用重新編碼, i 為新的索引值
ky_stocks.head().iloc[2, 2]  #使用iloc採用重新編碼, i 為新的索引值

ky_stocks.head().loc[[3, 8, 13], :]
ky_stocks.head().iloc[:3, :] #只取0~2 3個row
ky_stocks.head().loc[:, "name": "ky_listed"] #select "name" ~ "ky_listed" 3 columns.
ky_stocks.head().iloc[:, 1: 4] #只取1~3 3個欄位

ky_stocks.reset_index(drop = True)  
#自動reset index 並且將舊的index 給丟掉(如果有亂掉的話)

#arrange   排序
df.head()  #股價由高到低
df.sort_index(ascending = False)  #用index由大到小
df.sort_values("ticker")  #用index由小到大
df.sort_values(["ky_listed", "price"], ascending = [True, False])  
#根據多個column下去排
#(先排ky_listed(由小到大), 接著再根據price來排(由高到低))

#summarize 摘要(統計)
print(df["price"].max()) 
print(df["price"].median()) 
df["price"].std()
heights = [152, 154, 175, 169, 167, 162, 178, 150, 174, 178]
weights = [52, 78, 55, 76, 77, 78, 53, 68, 78, 64]
hw_df = pd.DataFrame()
hw_df["height"] = heights
hw_df["weight"] = weights
#多個column同時去看摘要統計
hw_df.max()
hw_df.max(axis = 1)  #byrow的max

df["price"].idxmax() #return最大值的索引位置
df_indexed = df.set_index("ticker")  #把索引值變成是有意義的ticker
df_indexed["price"].idxmax() #return price最大值的索引值(ticker)
df_indexed["price"].idxmin() #return price最小值的索引值(ticker)


#groupby 分組摘要
grouped = df.groupby("ky_listed")
print(grouped)   #在此可以發現無法直接看到裡面的內容  
#需要直接做其他的事情才能看到結果
grouped["price"].max()  #會回傳有KY和無KY兩組內的最大值
grouped["price"].mean()  #會回傳有KY和無KY兩組內的平均值
grouped["price"].nlargest(3)  #groupby完後依照某變數去挑出蓋變數底下的3個最大值


#filter 函數
#從price中選出超過200的數值
price
list(filter(lambda x: x > 200, price))

#Practice
#奧運獎牌練習
#以下 from web
import pandas as pd

df = pd.read_csv('https://storage.googleapis.com/py_ml_datasets/olympics.csv', 
index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID 
                                    #(take first 3 characters from that)

df = df.drop('Totals')
#以上from web

df.shape
df.head()
#index: 國家名稱  
##Summer: 該國家參加過幾屆夏季奧運  
#Gold, ..., Total 代表該國家在所有夏季奧運中所獲得的各種獎牌數
##Winter: 該國家參加過幾屆冬季奧運
#Gold.1, ..., Total.1 代表該國家在所有冬季奧運中所獲得的各種獎牌數
#Games: 該國家總共參加過幾屆夏季以及冬季奧運
#Gold.2, ..., Total.2 代表該國家在所有冬季以及夏季奧運中所獲得的各種獎牌數總和


#Q1  哪個國家贏得的夏季奧運金牌數最多?
#sol 1
def answer_one():
    """
    這個函數應該回傳一個文字，國家名
    """
    return(df[["Gold"]].idxmax()[0])

answer_one()

#sol 2
df.sort_values("Gold", ascending = False).iloc[0, :].name



#Q2  哪個國家夏季奧運與冬季奧運的金牌數差距最大?
def answer_two():
    """
    這個函數應該回傳一個文字，國家名
    """
    return((df["Gold"] - df["Gold.1"]).abs().idxmax())
    
answer_two()


#Q3  哪個國家夏季奧運與冬季奧運的金牌數差距除以總金牌數的比例最大？
#（僅考慮至少有一個夏季金牌與一個冬季金牌的國家）
# (Summer Gold - Winter Gold) / Total Gold
def answer_three():
    """
    這個函數應該回傳一個文字，國家名
    """
    summer_label = np.array((df["Gold"] != 0).values)
    winter_label = np.array((df["Gold.1"] != 0).values)
    all_label = summer_label*winter_label

    return ((df["Gold"][all_label] - df["Gold.1"][all_label])/df["Gold.2"][all_label]).abs().idxmax()

answer_three()


#Q4 計算 146 個國家的獎牌點數，其中金牌 3 點、銀牌 2 點、銅牌 1 點。
def answer_four():
    '''
    這個函數應該回傳一個 Series，長度為 146
    '''
    df["score"] = df.apply(lambda x: x["Gold.2"]*3 + x["Silver.2"]*2 + x["Bronze.2"]*1, axis = 1)
    
    return df["score"]

answer_four()

#若更改dataframe中的值  需要寫一個function再用map函式去把它給做替換


#美國普查練習
#資料結構
#SUMLEV若是40代表該列的資料為stat級的資料
#SUMLEV若是50代表該列的資料為county級的資料
import pandas as pd

census_df = pd.read_csv('https://storage.googleapis.com/py_ml_datasets/census.csv')
census_df.shape
census_df.iloc[ 3166:3173, 3:6 ]
census_df.columns
census_df.head()
#Q1: 哪一個州（state）的郡（county）數最多？（注意 SUMLEV 變數）
AA = census_df.groupby("STATE")
count = AA["COUNTY"].size()
new_data = set(census_df["STNAME"][census_df["STATE"] == count.idxmax()].values).pop()
new_data

#Q2: 如僅考慮每州（state）人口最多的三個郡（county）計算人口總和，
#    哪三個州總和數最多？（利用 CENSUS2010POP 變數）
df = census_df.sort_values(["STATE", "CENSUS2010POP"], ascending = [True, False])
allset = set()
no = list()
for i in range(len(df)):
    if (df.loc[i, :]["STATE"] in allset):
        ct += 1        
    else:
        allset.add(df.loc[i, :]["STATE"])
        ct = 0
    no.append(ct)

df["NO"] = no

df = df[(0 < df["NO"]) & (df["NO"] <= 3)]
result = df.groupby("STATE")["CENSUS2010POP"].sum().sort_values(ascending = False)
list(result[:3].index)

final = list()
for i in list(result[:3].index):
    print(i)
    temp = set(census_df["STNAME"][census_df["STATE"] == i].values).pop()
    final.append(temp)

final

#Q3 哪個郡（county）在 2010-2015 期間人口改變數量的絕對值最高？
#  （考慮 POPESTIMATE2010 到 POPESTIMATE2015 這六個變數） 
#   提示：如果 6 年的人口數分別為 100, 120, 80, 105, 100, 130, 120 
#   則人口改變數量的絕對值為 |130-80| = 50
df = census_df[["SUMLEV","STATE", "COUNTY", "STNAME", "CTYNAME", 
                "POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012",
                "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015"]]
df = df[df["SUMLEV"] == 50]

df_values = df[["POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012",
                "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015"]]

df.loc[df_values.apply((lambda x: abs(x.max() - x.min())), axis = 1).idxmax(), "CTYNAME"]



#Q4 篩選出屬於 REGION 1 或 2、開頭名稱為 Washington 並且 
#   POPESTIMATE2015 大於 POPESTIMATE2014 的郡（county）
df = census_df[["REGION", "STATE", "COUNTY", "STNAME", "CTYNAME", 
                "POPESTIMATE2015", "POPESTIMATE2014"]]
census_df.columns

df_REG = df[(df["REGION"] == 1) | (df["REGION"] == 2)]
df_REG_Wash = df_REG[df_REG["CTYNAME"].map(lambda x: "Washington" in x)]
ANS = df_REG_Wash[df_REG_Wash["POPESTIMATE2015"] > df_REG_Wash["POPESTIMATE2014"]][["STNAME", "CTYNAME"]]
ANS.reset_index(drop = True, inplace = True) #inplace代表不用再回傳新的值了，
                                             #直接將原本的表格值給更新覆蓋過去
#Series 用map加上function來計算一整條的結果
#DataFrame 用apply加上function來計算一整表格的結果(axis = 0 指直行, 1指橫列)
#篩選樣本(橫列)  請用結果含有false/True的[Series]
#篩選變數(值列)  請用[[多個變數名稱]]]
#要用數字選  記得使用.loc[ , ] or .iloc[ , ]
#若是複合型資料即一個欄位有多個種類，然後在別欄有細項則用.groupby(總變數)來拿出資料
#可使用set(array 或是 list)).pop() or Series.unique()來篩選出重複結果的獨一值
#Series的index 可以有兩層 那麼就要用兩次的index將值給取出
#groupby()[變數名稱].nlargest(3)   groupby完後依照某變數去挑出蓋變數底下的3個最大值
#or 和 and是用在純量上  | 和  &是作用在向量以及純量上
#注意: 若要將開頭為特定字詞時使用以下用法:
test_ser = pd.Series(["Washington County", 
                      "County Washington"])
test_ser.str.contains("Washington") #只要有Washington就回True
test_ser.str.contains("^Washington") #限定開頭為Washington(使用正規表達式^)
test_ser.str.contains("Washington$") #限定結尾為Washington(使用正規表達式$)

group = census_df.groupby("STNAME")
group["CENSUS2010POP"].nlargest(3)["Alabama"][37]




#Visulaization for Python
import pandas as pd

csv_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
gapminder = pd.read_csv(csv_file)
gapminder.shape
gapminder.head()  #每5年跳一筆資料

#Matplotlib
import matplotlib.pyplot as plt

#描繪一個數值: histogram (直方圖)
gdp_percap = gapminder["gdpPercap"]
plt.hist(gdp_percap, bins = 60)  #bin指箱 指最大和最小之間切成30個區段
plt.xlabel("GDP Per Capita")  #加入X軸的名稱
plt.ylabel("Frequency")  #加入X軸的名稱
plt.title("GDP Per Capital is left-skewed")  #加入標題
plt.show() 
##若有加axis或是title請務必要在.show()之前更動完成
##在terminal執行時使用此行函數會跳出另一個視窗

#描繪兩個數值: scatter plot (散佈圖)
point_colors = ["r", "g", "b", "c", "m"]
gapminder["continent"].unique()
for i in range(5):
    subset = gapminder[gapminder["continent"] == gapminder["continent"].unique()[i]]
    gdp_percap = subset["gdpPercap"]
    life_exp = subset["lifeExp"]
    plt.scatter(gdp_percap, life_exp, s = 7, c = point_colors[i], alpha = 0.5,
                label = gapminder["continent"].unique()[i])
    ##s: 點大小 ,c:color, alpha: 透明度

plt.xlabel("GDP Per Capita")
plt.ylabel("Life Expectancy")
plt.show()
##以下寫法與上面等價
point_colors = ["r", "g", "b", "c", "m"]
continents = gapminder["continent"].unique()
for pc, cont in zip(point_colors, continents):
    subset = gapminder[gapminder["continent"] == cont]
    gdp_percap = subset["gdpPercap"]
    life_exp = subset["lifeExp"]
    plt.scatter(gdp_percap, life_exp, s = 7, c = pc, alpha = 0.5,
                label = cont)    
    ##s: 點大小 ,c:color, alpha:透明度, label:圖例(需要搭配plt.legend來做)

plt.xlabel("GDP Per Capita")
plt.ylabel("Life Expectancy")
plt.legend(loc = "lower right")  #把圖例給呼叫出來  loc為圖例位置
plt.title("GDP per capita vs. life expectancy by continents")
plt.show()

#描繪一個類別: bar plot (長條圖)
grouped = gapminder.groupby("continent")
country_cnt = grouped["country"].count() #依照每組去數列數
plt.bar(range(1, 6), country_cnt.values)  #先放x軸 再放y軸
for xx, yy in zip(range(1, 6), country_cnt.values):
    plt.annotate(yy, (xx, yy), (xx-0.1, yy + 25))  
#在每個bar上方進行標記文字 第一個座標(xx, yy)為資料點的位置
#第二個座標(xx-0.1, yy + 25)則為annotation文字的位置
plt.xticks(range(1, 6), country_cnt.index) #更改x軸的刻度名稱
plt.ylim(0, country_cnt.max() + 70)  #調整y軸的上界
plt.show()

##Horizontal bar plot(Pandas 內建呼叫matplotlib)
country_cnt.plot.barh()
plt.show()

#描繪一個數值與一個類別: box plot (盒鬚圖)
##下方資料若使用histgram來畫會顯得很雜亂，可使用boxplot來更清楚地表達
##分不同的continent來看distribution
fill_colors = ["r", "g", "b", "c", "m"]
continents = gapminder["continent"].unique()
for fc, cont in zip(fill_colors, continents):
    subset = gapminder[gapminder["continent"] == cont]
    gdp_percap = subset["gdpPercap"]
    plt.hist(gdp_percap, bins = 30, alpha = 0.5, label = cont, 
             color = fc)    

plt.show()

gapminder.head()
##long format表格資料換成wide format (pivot()) (long data to wide data)
long_format = gapminder
##先造出一個key的欄位，此key欄位需要具有獨一性(提供對照)
##若原始的資料欄位以及型態不好辨識或是不具意義也可另外造一個key欄位
##另外，若表格資料中有欄位資料是有這樣的性質則不需要再另外造欄位
long_format["key"] = long_format["country"] + long_format["year"].astype(str)
long_format.head()
wide_format = long_format.pivot(index = "key", columns = "continent", values = "gdpPercap")
wide_format.plot.box()  
#注意在這邊是直接在資料後接上plot方法，而非另外抓一個plot來畫
#這樣的寫法可以先自動過濾NaN，若另外開一個plot方法，則要先去除NaN才能繪圖
plt.ylim(0, 50000)
plt.show()
#pandas.melt() 資料型態wide format轉成long format

#描繪日期時間與數值: line plot (線圖)
tw = gapminder[gapminder["country"] == "Taiwan"]
jp = gapminder[gapminder["country"] == "Japan"]
cn = gapminder[gapminder["country"] == "China"]

plt.plot(tw["year"], tw["lifeExp"], label = "Taiwan") 
#不能輸入x = , y = 否則圖形出不來, label為圖例名稱
plt.plot(jp["year"], jp["lifeExp"], label = "Japan")
plt.plot(cn["year"], cn["lifeExp"], label = "China")
plt.legend(loc = "lower right")
plt.show()



#子圖: subplots (分成兩個元素，圖和軸)
##若將continent的資料分成很多個subplot,並在每個subplot中畫直方圖，
##此法也是解決眾多圖表疊再一起的方法之一
fig, axes = plt.subplots(2, 3)
subset = gapminder[gapminder["continent"] == "Asia"]
axes[0, 1].hist(subset["gdpPercap"], color = "g")
plt.show()

#把每個都畫出來
fill_colors = ["r", "g", "b", "c", "m"]
continents = gapminder["continent"].unique()
srows = [0,0,0,1,1]
scols = [0,1,2,0,1]

fig, axes = plt.subplots(2, 3)
for fc, cont, sr, sc in zip(fill_colors, continents, srows, scols):
    subset = gapminder[gapminder["continent"] == cont]
    axes[sr, sc].hist(subset["gdpPercap"], color = fc)
    axes[sr, sc].set_title(cont)

axes[1, 2].set_visible(False)  #將右下角的子圖設為隱形    
plt.tight_layout(rect = [0, 0.03, 1, 0.95])  
#將上下層子圖的間距給分開 rect內順序為左下右上
plt.suptitle("GDP per capia by continents")  #所有子圖的大標
plt.show()


#運用subplot來疊圖 (長條圖 + 線圖) (雙軸(不同參考值)的處理)
fig, ax1 = plt.subplots()
ax1.bar(tw["year"], tw["gdpPercap"], color = "red", alpha = 0.6)
ax1.grid(False, axis = "y")
ax1.set_xlabel("Year")
ax1.set_ylabel('GDP Per Capita')

ax2 = ax1.twinx()
ax2.plot(tw["year"], tw["lifeExp"])
ax2.grid(False, axis = "y")
ax2.set_ylabel("Life Expectancy")
fig.tight_layout()
plt.xticks(tw["year"].values, tw["year"].values) #對齊x軸的刻度名稱
plt.show()


#互動式地圖: folium
#http://python-visualization.github.io/folium/
##參考Python畫互動式地圖(http://medium.com/datainpoint/eda-other-vuz-a87dd52e7905) 
#Gapminder的動畫效果(散佈圖隨時間變化效果)
#plotly: https://plot.ly/python (建議使用R去畫)
#Dash: https://plot.ly/products/dash


#標題、標籤、刻度、圖例(以合併在上述的示範程式碼內)
#畫素、圖片大小
plt.figure(figsize = (12, 4), dpi = 500) 
#在畫圖流程一開始使用figure方法時可以調圖片大小(figsize)以及畫素(dpi)
plt.scatter(gapminder["gdpPercap"], gapminder["lifeExp"])
plt.show()

#背景顏色
##灰背景
import seaborn as sns
sns.set_style("darkgrid") #更改畫布背景
plt.figure(figsize = (12, 4), dpi = 500)
plt.scatter(gapminder["gdpPercap"], gapminder["lifeExp"])
plt.show()

##黑色主題風格
sns.set_style("ticks") #更改畫布背景
plt.style.use("dark_background") #更改主題風格
plt.figure(figsize = (12, 4), dpi = 500)
plt.scatter(gapminder["gdpPercap"], gapminder["lifeExp"])
plt.show()

#X軸與Y軸的保留
sns.set_style("darkgrid") #更改畫布背景
fig = plt.figure(dpi = 500)
ax = fig.gca()
ax.grid(False, axis = "y") #保留y軸
ax.scatter(gapminder["gdpPercap"], gapminder["lifeExp"])
plt.show()

#圖片檔案儲存
plt.savefig()

#指派圖形內容顏色
#https://matplotlib.org/users/colors.html

#指定中文字體
#https://medium.com/datainpoint/eda-components-984ccabef57d

#更改單一軸的字體
#hfont = {'fontname': 'Times New Roman'}
hfont = {'fontname': 'Helvetea'}
plt.xlabel('AAA', **hfont)




#機器學習簡介 Machine Learning (ML)
#人工智慧(包含機器學習(包含深度學習))
#延伸閱讀(1) 基礎線性代數: Linear Algebra for Dummies
#延伸閱讀(2) 完整線性代數: Linear Algebra (MIT)
#延伸閱讀(3) 深度學習: Deep Learning (MIT)
#延伸閱讀(4) 機器學習: Andrew Ng: Machine Learning 
#延伸閱讀(5) 林軒田(機器學習基石)  ---->  最難

#機器學習又分為
#監督式學習：預測數值、類別 (迴歸問題、分類問題)
#e.g. Gmail幫忙分類垃圾信件 
#e.g. 利用月收入來核定信用額度
#e.g. 利用坪數來預測房價
#e.g. 利用每日最高溫來預測飲料店的冰紅茶銷量
#非監督式學習：挖掘出data的特徵 (==> 無標準答案)
#e.g. cluster analysis (e.g. 把相似度高的客人集合成一個客群), 
#     PCA(把相似度高的變數拉成同一個主成分)

#Scikit-Learn
#https://scikit-learn.org/stable/index.html
#六大功能模組 (預處理、降維、迴歸、分群、分類、模型評估)


#迴歸問題
#y = f(x) 為假想的母體迴歸式
#y^ = h(x) = theta_0*1 + theta_1*x_1 + ... + theta_n*x_n 為建模出來的預測值
#Cost function 成本函數 為所有樣本的誤差的總和的平均，也就是損失函數的總和的平均
#Loss function 損失函數 為單一樣本的誤差，為一個(y^-y)的函數

#定義Cost Function 為 (1/2m) * summation(y^_i -y_i)^2 = 1/2*MSE
#上式後面即為sum(residual^2)

#y^ = h(x) = theta_0*1 + theta_1*x_1 + ... + theta_n*x_n 
#   = t(theta) %*% x = t(x) %*% theta
#上式為只有一個觀測值的時候
#x和theta都是(n+1)x1的向量
#若有m個觀測值時y^ = x %*% theta, 
#此時的x第一個col全部都是1(x_0), 第二個col為n個樣本的x_1, ....依此類推
#x為一個mx(n+1)的矩陣, theta則是(n+1)x1的向量
#Toy Example
#Observations: (x, y):{(1, 2), (2, 2), (3, 4)} 共3組觀測值
#theta向量為2x1的向量，另外x和y矩陣分別為
import numpy as np
x = np.array([[1, 1],
              [1, 2],
              [1, 3]]).reshape(-1, 2)
y = np.array([2,2,4]).reshape(-1, 1)

#接下來求出theta的樣子
#min(J(theta)), where J(theta) = Cost function 
#                              = (1/2m)*t(x%*%theta - y) %*% (x%*%theta - y)
#找到theta向量使得Cost function 最小 (最佳化問題)
#可使用兩種方式來解決此問題(1. Normal Equation, 2. Gradient Descent)
#1. Normal Equation(正規方程式):
#partial(J(theta))/partial(theta) = (1/2m)(2(t(x)%*%x)%*%theta-2t(x)%*%y)
# = 1/m ((t(x)%*%x)%*%theta - t(x)%*%y) set 0
# => (t(x)%*%x)%*%theta - t(x)%*%y = 0 => (t(x)%*%x)%*%theta = t(x)%*%y
# => theta = solve(t(x)%*%x)%*%(t(x)%*%y)
theta = np.dot(np.linalg.inv(np.dot(x.T, x)), np.dot(x.T, y))

#2. Gradient Descent:
#Gradient: partial(J(theta))/partial(theta)
#          = 1/m ((t(x)%*%x)%*%theta - t(x)%*%y)
#Gradient Descent Algorithm:
#Goal: Find the local minimun of Cost function
#theta_new = theta_old - alpha*(partial(J(theta_old))/partial(theta_old))
#          = theta_old - alpha*Gradient
#          = theta_old - alpha*1/m((t(x)%*%x)%*%theta_old - t(x)%*%y)
#          = theta_old - (alpha/m)*(t(x)%*%(x%*%theta_old - y)), 
#where alpha is called learning rate (學習速率)
#意思是gradient幫我們決定好了下一個點要走的方向
#但要沿著這個方向前進的距離(長度)是alpha在決定的
#因此theta_new的修正速度與alpha相關，太大或太小都不好，需要依照每個案例去試
def cost_function(x, y, theta):
    y_hat = np.dot(x, theta)
    sse = np.sum((y_hat - y) ** 2)
    cost = sse / (2*x.shape[0])
    return cost

cost_function(theta = theta)[0][0]

def gradient_descent(x, y, alpha, iteration = 15000):
    thetas = np.array([0, 0]).reshape(-1, 1)
    m = x.shape[0]
    cost_hist = np.zeros(iteration)
    
    for i in range(iteration):
        h = np.dot(x, thetas)
        loss = h - y
        gradient = np.dot(x.T, loss) / m
        thetas = thetas - alpha * gradient
        cost = cost_function(x, y, theta = thetas)
        cost_hist[i] = cost
        
        if i % 100 == 0:
            print("第{}次迭代，cost function的值為{}".format(i, cost_hist[i]))
    return thetas, cost_hist

theta, hist = gradient_descent(x, y, alpha = 0.01)

#繪製Cost function 迭代時發生的變化
plt.plot(hist)
plt.xlabel("Iterations")
plt.ylabel("Cost Function")
plt.show()

#SK-learn 套件
from sklearn.linear_model import LinearRegression
#使用時需要先初始化及下一行的指令動作
reg = LinearRegression()

#配適模型 不須彌補常數項的x 即11111
X = np.array([1, 2, 3]).reshape(-1, 1)
Y = np.array([2, 2, 4]).reshape(-1, 1)
reg.fit(X, Y)
reg.intercept_
reg.coef_

#預測新的值
X_arr = np.linspace(X.min()-1, X.max()+1).reshape(-1, 1)
Y_hats_skl = reg.predict(X_arr)
Y_hats_skl[:5]

#資料散佈狀況以及迴歸線繪製
import matplotlib.pyplot as plt
X = np.array([1, 2, 3])
Y = np.array([2, 2, 4])
plt.scatter(X, Y)
X_arr = np.linspace(X.min() - 1, X.max() + 1).reshape(-1, 1)
#從0到4打50個均分的資料點
ones = np.ones(X_arr.shape[0]).reshape(-1, 1)
X_arr = np.concatenate([ones, X_arr], axis = 1)
Y_hats = np.dot(X_arr, theta)
plt.plot(X_arr[:, 1], Y_hats)
plt.xlim(X.min() - 1, X.max() + 1)
plt.ylim(Y.min() - 1, Y.max() + 1)
plt.show()


#3D模型圖
#繪製各種不同theta在帶入cost function後對cost function的影響
#意即確認我們找到的theta是否能使cost function達到local minimum
theta_0_arr = np.linspace(0, 1) #在0~1之中均分成50個點來當50個theta_0
theta_1_arr = np.linspace(0, 2) #在0~1之中均分成50個點來當50個theta_1
print(theta_0_arr)
print(theta_1_arr)
#將每一個theta_0的值match到theta_1的值，意即創造50*50(共2500)個不同的theta組合
xx, yy = np.meshgrid(theta_0_arr, theta_1_arr)  #meshgrid最主要用來產生座標

Z = np.zeros((50, 50)) #先創造一個matrix(用來擺放每組theta所得到的成本函數值)
#產生每個組合的成本函數值
def cost_function(x, y, theta):
    y_hat = np.dot(x, theta)
    sse = np.sum((y_hat - y) ** 2)
    cost = sse / (2*x.shape[0])
    return cost

for i in range(len(theta_0_arr)):
    for j in range(len(theta_1_arr)):
        theta_0 = theta_0_arr[i] 
        theta_1 = theta_1_arr[j]
        thetas_arr = np.array([theta_0, theta_1]).reshape(-1, 1)
        Z[i, j] = cost_function(
                x = np.array([[1, 1],
                              [1, 2],
                              [1, 3]]).reshape(-1, 2), 
                y = np.array([2, 2, 4]).reshape(-1, 1), 
                theta = thetas_arr)

#繪製3D Cost function (適用於兩個變數(e.g. 常數項的theta_0，x_1的theta_1))
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')  #111代表只要畫一個子圖
ax.plot_surface(xx, yy, Z, alpha = 0.5, 
                cmap = plt.cm.jet) #cmap代表色票 color map(red: 大的, blue: 小的)
ax.set_zlabel("Cost")
ax.set_xticks(np.linspace(theta_0_arr.min(), 
              theta_0_arr.max(), 5)) #打5個點
ax.set_yticks(np.linspace(theta_1_arr.min(), 
              theta_1_arr.max(), 5)) #打5個點
ax.set_xlabel(r'$\theta_0$')
ax.set_ylabel(r'$\theta_1$')
ax.set_title("Cost function during gradient descent")
plt.show() #可以發現theta_0方向的遞減程度較為明顯，
#           但theta_1方向的遞減程度較不明顯
#           因此若不確定所找的點是否為極值，可以畫其他的點



#Exercise: 房屋價格預測的資料
#Data連結:https://www.kaggle.com/c/house-prices-advanced-regression-techniques

import pandas as pd

train_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
test_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/test.csv"
labeled = pd.read_csv(train_url)
test = pd.read_csv(test_url)
print(labeled.shape)
print(test.shape)

labeled.head()
test.head()

#資料的切割(資料比例) Cross Validation
#訓練: 0.7 ~ 0.8
#驗證: 0.3 ~ 0.2
#觀測值隨機排序後，(shuffle)
#前T%給訓練樣本，後100-T%分給驗證樣本

row_indice = list(labeled.index)
np.random.shuffle(row_indice) 

labeled_shuffle = labeled.loc[row_indice, :]  #指定每一行的編號(隨機排列)
labeled_shuffle
m = labeled.shape[0]
train_threshold = int(m*0.7)
train = labeled.iloc[:train_threshold, :]
validation = labeled.iloc[train_threshold:, :]
print(train.shape)
print(validation.shape)

#使用SKlearn模組去做分資料的動作
from sklearn.model_selection import train_test_split

train, validation = train_test_split(labeled, test_size = 0.3, random_state = 123)  #random_state就是set.seed的概念
train.shape
validation.shape

#選取變數(通常考量相關性以及因果性，以考量相關性為最大宗)
#考慮X和Y之間的相關性(先從相關性強的開始取)
saleprice_corr = train.corr()["SalePrice"] 
#train.corr()出來是一個correlation matrix data frame 用["SalePrice"]取出想看的column
saleprice_corr[:10]
saleprice_corr.abs().nlargest(10)
#可發現"OverallQual"為高度相關, OverallQual為一個房子的客觀評價
train.plot.scatter("OverallQual", "SalePrice")
train.plot.scatter("GrLivArea", "SalePrice") #地上可使用坪數

#使用"GrLivArea"來預測Y
train[["GrLivArea", "SalePrice"]]

Y = train["SalePrice"].values.reshape(-1, 1)
X = np.ones(train.shape[0], dtype = np.int64).reshape(-1, 1)
X = np.concatenate([X, train["GrLivArea"].values.reshape(-1, 1)], axis = 1)

gradient_descent(X, Y,  alpha = 0.0000000001, iteration=100000)

#注意: 
#1. 若cost function在跑的過程中在某一次以後都跑出Nan或是inf代表learning_rate太大，iters太小
#   需要將learning_rate調小，iters調大。調整learning_rate以及iters亦可以藉由畫cost function與iters的圖來判斷
#   需要如何來調整(理想狀態:趨近右半邊的bell shape，若cost_function瞬間掉下來(趨近L形)代表要
#   將learning rate、iters調小，反之則調大(或是增加iters的次數))，先調learning_rate在調iters
#2. 若learning_rate已經到了很小，iters已經到了很大，但仍然沒有好的結果(各個參數收斂速度一致)的話，
#   代表是觀測值的單位量級(X, Y)差距太多了的問題，此時可先經過標準化轉換過後再來配適模型會較為適合。

#標準化 (Normalization) 後做迴歸: 用來解決變數單位不一致問題
#(1) Min-Max Scaler
#x_scaled = (x - min(x))/(max(x)-min(x))

#(2) Standard Scaler
#x_scaled = (x - mean(x))/std(x)
X = X[:, 1].reshape(-1, 1)
X.shape
Y.shape

def standard_scalar(x):
    x_mean = x.mean()
    x_std = x.std()
    return (x - x_mean)/x_std

standard_scalar(X)
standard_scalar(Y)
#若使用package
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
X = ss.fit_transform(X.astype(float))
Y = ss.fit_transform(Y.astype(float))

ones = np.ones(X.shape[0]).reshape(-1, 1)
X = np.concatenate([ones, X], axis = 1)


thetas_scaled, cost_history_scaled = gradient_descent(X, Y,  
                                                      alpha = 0.01, 
                                                      iteration=5000)

plt.plot(cost_history_scaled)
plt.show()
#fit完成後轉為原本的scale (scale back)
Y = train["SalePrice"].values.reshape(-1, 1)
X = np.ones(train.shape[0], dtype = np.int64).reshape(-1, 1)
X = np.concatenate([X, train["GrLivArea"].values.reshape(-1, 1)], axis = 1)
X = X[:, 1].reshape(-1, 1)

#Y = mu_Y + theta_0*sigma_Y - theta_1*(sigma_Y/sigma_X)*mu_X + theta_1*(sugma_Y/sigma_X)*X
theta_0 = (Y.mean() + thetas_scaled[0][0]*Y.std() - thetas_scaled[1][0]*(Y.std()/X.std())*X.mean())
theta_1 = thetas_scaled[1][0]*(Y.std()/X.std())

#正規化 (Regularization): 用來解決Overfitting問題

#Ans for Normal Equation
def get_thetas_ne(X, y):
    LHS = np.dot(X.T, X)
    RHS = np.dot(X.T, y)
    LHS_inv = np.linalg.inv(LHS)
    thetas = np.dot(LHS_inv, RHS)
    return thetas

get_thetas_ne(X, Y)

#使用package (建議使用scikit-learn)
#statsmodels
import statsmodels.api as sm
regressor_sm = sm.OLS(Y, X)
thetas_sm = regressor_sm.fit()
theta_0_sm = thetas_sm.params[0]
theta_1_sm = thetas_sm.params[1]

#scikitlearn
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
X = train["GrLivArea"].values.reshape(-1, 1)  #SKlearn的X不需要加1(常數項的x)
reg.fit(X, Y)
reg.intercept_
reg.coef_

#tenserflow也行


#評估模型的表現
#MSE (Mean Squared Error)
#加入一個變數進來
#Model_1: SalePrice - GrLivArea
#Model_2: SalePrice - GrLivArea + GargeArea
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size = 0.3, random_state = 123)

#Model 1
reg_1 = LinearRegression()
reg_1.fit(train["GrLivArea"].values.reshape(-1, 1),
          train["SalePrice"].values.reshape(-1, 1))
print(reg_1.intercept_)
print(reg_1.coef_)
y_hat = reg_1.predict(validation["GrLivArea"].values.reshape(-1, 1))
y = validation["SalePrice"].values
print(y_hat[:5])
print(y[:5])
residual = y_hat.reshape(-1, 1) - y.reshape(-1, 1)
mse = np.dot(residual.T, residual)[0, 0]/len(residual)
mse
##MSE其他寫法
#純量寫法
y_err = y_hat - y.reshape(-1, 1)
mse = (np.dot(y_err.T, y_err)/m)[0, 0]
mse
#SKLearn
mse = mean_squared_error(y.reshape(-1, 1), y_hat)
mse

#Model 2
reg_2 = LinearRegression()
reg_2.fit(train[["GrLivArea", "GarageArea"]].values, #一維(1個變數)的話需要reshape，二維的話則不用(出來自己就是一個matrix了)
          train["SalePrice"].values.reshape(-1, 1))
print(reg_2.intercept_)
print(reg_2.coef_)
y_hat = reg_2.predict(validation[["GrLivArea", "GarageArea"]].values)
y = validation["SalePrice"].values
print(y_hat[:5])
print(y[:5])
residual = y_hat.reshape(-1, 1) - y.reshape(-1, 1)
mse = mean_squared_error(y.reshape(-1, 1), y_hat)
mse

#Model 3 (Non-linear Regression, Polynomial Regression)
#若持續使用linear reg的架構來用在非線性的predictor上
#則得到的MSE結果會更不好
reg_yr = LinearRegression()
reg_yr.fit(train["YearBuilt"].values.reshape(-1, 1), #一維(1個變數)的話需要reshape，二維的話則不用(出來自己就是一個matrix了)
          train["SalePrice"].values.reshape(-1, 1))
y_hat = reg_yr.predict(validation["YearBuilt"].values.reshape(-1, 1))
y = validation["SalePrice"].values
print(y_hat[:5])
print(y[:5])
mse = mean_squared_error(y.reshape(-1, 1), y_hat)
mse

#Polynomial Model
#y = theta_0 + theta_1*x_1 + theta_2*x_1^2
from sklearn.preprocessing import PolynomialFeatures

#製造二次項的column
(train["YearBuilt"].values.reshape(-1, 1))**2
#package 寫法 (直接和其他的變數併再一起)
poly = PolynomialFeatures(degree = 2)
poly.fit(train["YearBuilt"].values.reshape(-1, 1))
poly.transform(train["YearBuilt"].values.reshape(-1, 1))
#or
poly = PolynomialFeatures(degree = 2)
poly.fit_transform(train["YearBuilt"].values.reshape(-1, 1))

#Construct Polynomial Model(二次項)
reg_yr_poly = LinearRegression()
reg_yr_poly.fit(poly.fit_transform(train["YearBuilt"].values.reshape(-1, 1)),
          train["SalePrice"].values.reshape(-1, 1))
y_hat = reg_yr_poly.predict(poly.fit_transform(validation["YearBuilt"].values.reshape(-1, 1)))
y = validation["SalePrice"].values
print(y_hat[:5])
print(y[:5])
mse = mean_squared_error(y.reshape(-1, 1), y_hat)
mse

#Construct Polynomial Model(三次項)
X_train = train["YearBuilt"].values.reshape(-1, 1)
y_train = train["SalePrice"].values.reshape(-1, 1)

X_train_poly = PolynomialFeatures(degree = 3).fit_transform(X_train)
reg_poly = LinearRegression()
reg_poly.fit(X_train_poly, y_train)
X_validation = validation["YearBuilt"].values.reshape(-1, 1)
X_validation_poly = PolynomialFeatures(3).fit_transform(X_validation)
y_validation = validation["SalePrice"].values.reshape(-1, 1)
y_hat = reg_poly.predict(X_validation_poly)
mse = mean_squared_error(y_validation, y_hat)
mse
#會發現驗證資料集的MSE下降了 => 代表model不適合
#degree應為2就好了 (Apporpriate fitting)
#degree為1時 (under-fitting)

#繪製fit lines and data
plt.scatter(labeled["YearBuilt"], labeled["SalePrice"])
plt.xlabel("Year Built")
plt.ylabel("Sale Price")
X_arr = np.linspace(labeled["YearBuilt"].min(), labeled["YearBuilt"].max()).reshape(-1, 1)
X_arr_poly = PolynomialFeatures(3).fit_transform(X_arr)
y_arr = reg_poly.predict(X_arr_poly)
plt.plot(X_arr, y_arr, color = "r", linewidth = 2)
plt.show()

#Construct Different Degree Polynomial Model, and
#choose the best model.
def get_mse_by_degrees(labeled, degrees = range(1, 11)):
    train, validation = train_test_split(labeled, test_size = 0.3)
    X_train = train["YearBuilt"].values.reshape(-1, 1)
    y_train = train["SalePrice"].values.reshape(-1, 1)
    X_validation = validation["YearBuilt"].values.reshape(-1,1)
    y_validation = validation["SalePrice"].values.reshape(-1,1)
    mse_train_arr = np.zeros(len(degrees))
    mse_valid_arr = np.zeros(len(degrees))
    for d in degrees:
        X_train_poly = PolynomialFeatures(d).fit_transform(X_train)
        reg_poly = LinearRegression()
        reg_poly.fit(X_train_poly, y_train)
        X_validation_poly = PolynomialFeatures(d).fit_transform(X_validation)
        y_hat = reg_poly.predict(X_validation_poly)
        mse_valid = mean_squared_error(y_validation, y_hat)
        y_hat = reg_poly.predict(X_train_poly)
        mse_train = mean_squared_error(y_train, y_hat)
        mse_valid_arr[d-1] = mse_valid
        mse_train_arr[d-1] = mse_train
    best_degree = mse_valid_arr.argmin() + 1
    return mse_valid_arr, mse_train_arr, best_degree

degrees = range(1, 11)
mse_valid_arr, mse_train_arr, best_degree = get_mse_by_degrees(labeled, degrees)

print("Best Degree: {}".format(best_degree))
plt.plot(degrees, mse_valid_arr, color = "r", label = "Validation")
plt.plot(degrees, mse_train_arr, color = "g", label = "Train")
plt.legend()
plt.show()

#從上面的結果可發現每次執行所選出來的最佳model都不同  因此，
#需要使用k-fold cross validation來消彌掉此問題
#在上面的例子中若要加入4-fold cross validation概念的話
#需要在每一個degree的polynomial model中去計算4-fold cross validation
#的MSE結果，並將4次的MSE平均起來，因此總共需計算10*4次MSE
#最後再由這10個MSE中去挑出最小的MSE來選擇最佳多項式模型的次方數

#PolynomialFeatures的功用
X_train = train.loc[:, "YearBuilt"].values.reshape(-1, 1)
PolynomialFeatures(2).fit_transform(X_train)

X_train = train.loc[:, ["YearBuilt", "GrLivArea"]].values
PolynomialFeatures(2).fit_transform(X_train).shape  #常數項(1)、兩個變數的一次項、二次項，以及交互作用X_1*X_2

X_train = train.loc[:, ["YearBuilt", "GrLivArea","GarageArea"]].values
PolynomialFeatures(2).fit_transform(X_train).shape  #常數項(1)、三個變數的一次項、二次項，以及三個交互作用項X_1*X_2

#Training Data Model Over-fitting Problem (過度配適)
def get_mse_by_degrees(labeled, degrees = range(1, 11)):
    train, validation = train_test_split(labeled, test_size = 0.3)
    X_train = train[["YearBuilt", "GrLivArea", "GarageArea"]].values
    y_train = train["SalePrice"].values.reshape(-1, 1)
    X_validation = validation[["YearBuilt", "GrLivArea", "GarageArea"]].values
    y_validation = validation["SalePrice"].values.reshape(-1,1)
    mse_train_arr = np.zeros(len(degrees))
    mse_valid_arr = np.zeros(len(degrees))
    for d in degrees:
        X_train_poly = PolynomialFeatures(d).fit_transform(X_train)
        reg_poly = LinearRegression()
        reg_poly.fit(X_train_poly, y_train)
        X_validation_poly = PolynomialFeatures(d).fit_transform(X_validation)
        y_hat = reg_poly.predict(X_validation_poly)
        mse_valid = mean_squared_error(y_validation, y_hat)
        y_hat = reg_poly.predict(X_train_poly)
        mse_train = mean_squared_error(y_train, y_hat)
        mse_valid_arr[d-1] = mse_valid
        mse_train_arr[d-1] = mse_train
    best_degree = mse_valid_arr.argmin() + 1
    return mse_valid_arr, mse_train_arr, best_degree

degrees = range(1, 11)
mse_valid_arr, mse_train_arr, best_degree = get_mse_by_degrees(labeled, degrees)

print("Best Degree: {}".format(best_degree))
plt.plot(degrees, mse_valid_arr, color = "r", label = "Validation")
plt.plot(degrees, mse_train_arr, color = "g", label = "Train")
plt.legend()
plt.show()
#從上面的圖可以看到overfitting的問題

#解決方法: Regularization 正規化 (決定超參數(hyperparameter))
#Ridge Regression
#加入regression function 後方加入Penalty 來控制 (把曲線(面)平滑化)
#Y = f(X) + lambda*sum(theta_i^2, i = 0,1,2,3,...)
#lambda*sum.....該項即為限制式
#意思即是限定theta_0, theta_1, theta_2, ...滿足
#sum(theta_i^2, i = 0,1,2,3,...) < C
#其中C為一給定的常數
#當lambda上升，代表正規化的效果會越強，配適的曲線(曲面)會越趨近直線(平面)，
#theta_i也們會顯著的降低
#Q: How to choose lambda?
#Ans: GridSearch in SKLearn
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

X_train = labeled[["YearBuilt", "GrLivArea", "GarageArea"]].values
y_train = labeled["SalePrice"].values.reshape(-1, 1)
reg = Ridge()
parameters = {"alpha": [1, 10, 10**2, 10**3, 10**4, 10**5]} 
gridclassifier = GridSearchCV(reg, 
                              param_grid = parameters, 
                              cv = 4, 
                              scoring = "neg_mean_squared_error")
gridclassifier.fit(X_train, y_train)

#show 出超參數的選擇
gridclassifier.best_estimator_
gridclassifier.best_params_
gridclassifier.best_score_ #negative MSE，若要MSE則需再取一次負號，讓質變正的

best_alpha = gridclassifier.best_params_['alpha']
regressor = Ridge(alpha=best_alpha).fit(X_train,y_train)

#logistic regression
#分類問題
import pandas as pd
import matplotlib.pyplot as plt

labeled_url = "https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv"
test_url = "https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/test.csv"
labeled_df = pd.read_csv(labeled_url)
test_df = pd.read_csv(test_url)
print(labeled_df.shape)
print(test_df.shape)

labeled_df.head()
labeled_df.info()  #查看變數名稱
test_df.head()

labeled_df = labeled_df[labeled_df["Age"].notna()] #將age為NA的刪除
#遺失值可使用補值的方法把數值給補回來(e.g.補值方法:連續資料: 中位數, 眾數, 平均數, 建模預測
#                                               類別資料: 按照整體類別的比例去補，按照最多種類類別的去補)
labeled_df.describe()  #各變數描述性統計量

#畫資料散佈的情況
def plot_data(data, label_x, label_y, label_pos, label_neg, label_target):
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))
    neg = data[label_target] == 0
    pos = data[label_target] == 1
    ax.scatter(data[pos][label_x], data[pos][label_y], marker='+', c='k', s=60, linewidth=2, label=label_pos)
    ax.scatter(data[neg][label_x], data[neg][label_y], c='y', s=10, label=label_neg, alpha = 0.5)
    ax.set_xlabel(label_x)
    ax.set_ylabel(label_y)
    ax.legend(frameon= True, fancybox = True)    


plot_data(labeled_df, "Fare", "Age", "Survived", "Dead", "Survived")
plt.show()

#Goal: 將黃色的點和加號給分開來
#分類問題是迴歸問題的延伸
#sigmoid 函數: 1/(1 + e^(- X*theta)) 出來的值域落在[0, 1]之間 
#接著以0.5為臨界值(大部分情況) 下去做切割成 0, 1 來預測結果
#logistic regression 成本函數:
#J(theta) = -(1/m)*(t(log(g(X%*%theta)))%*%y + t(log(1 - g(X%*%theta)))%*%(1 - y))
#g(X%*%theta) = 1/(1 + e^(- X*theta))
#注意: J(theta) 可以想像成是由-log(H(z))和-log(1 - H(z))兩個部分組合而成，
#其中z = X%*%theta
#當y = 1時, J(theta) = -log(H(z))，此時若H(z) = 0(預測錯誤) 則J(theta)會衝到無限大
#反之則是J(theta) = -log(1 - H(z))，此時若H(z) = 1(預測錯誤) 則J(theta)會衝到無限大

#若將J(theta)對theta做偏微則會得到(1/m)*t(X)%*%(g(X%*%theta) - y)
#sigmoid函數:
def sigmoid(z):
    return(1 / (1 + np.exp(-z)))

#Cost function for logistic regression
def cost_function(theta, X, y):
    m = y.shape[0]
    h = sigmoid(X.dot(theta))
    J = -1*(1/m)*(np.log(h).T.dot(y)+np.log(1-h).T.dot(1-y))
    if np.isnan(J[0]):
        return(np.inf)
    return(J[0])
    
#Gradient Descent for Logistic regression
def gradient_descent(theta, X, y):
    m = y.shape[0]
    h = sigmoid(X.dot(theta.reshape(-1, 1)))
    grad =(1/m)*X.T.dot(h-y)
    return(grad.ravel())

#手寫找theta
from sklearn.model_selection import train_test_split

train_df, validation_df = train_test_split(labeled_df, test_size=0.3, random_state=123)
X_train = train_df[["Fare", "Age"]].values
y_train = train_df["Survived"].values.reshape(-1, 1)
ones = np.ones(X_train.shape[0]).reshape(-1, 1)
X_train = np.concatenate([ones, X_train], axis=1)
initial_theta = np.zeros(X_train.shape[1])
cost = cost_function(initial_theta, X_train, y_train)
grad = gradient_descent(initial_theta, X_train, y_train)
print('Cost: \n', cost)
print('Grad: \n', grad)

#利用 scipy 的 optimize() 函數來幫忙迭代找theta
from scipy.optimize import minimize

res = minimize(cost_function, 
               initial_theta, 
               args=(X_train, y_train), 
               method=None, 
               jac=gradient_descent, 
               options={'maxiter':400})

thetas = res.x.reshape(-1, 1)

#預測一筆資料
# 將 validation_df 中的第一個觀測值拿出來試試看
X_validation = validation_df[["Fare", "Age"]].values
ones = np.ones(X_validation.shape[0]).reshape(-1, 1)
X_validation = np.concatenate([ones, X_validation], axis=1)
x_validation_0 = X_validation[0, :].reshape(-1, 1)
print(sigmoid(np.dot(thetas.T, x_validation_0))[0, 0])

def predict(thetas, X, threshold=0.5):
    p = sigmoid(np.dot(X, thetas)) >= threshold
    return(p.astype(int))

is_survived = predict(thetas, x_validation_0.ravel())[0]
print("羅吉斯迴歸模型的預測是: {}".format(is_survived))
print("真實的情況是 :{}".format(validation_df["Survived"].values[0]))

#計算該模型的準確率
y_hat = predict(thetas, X_validation)
y_validation = validation_df["Survived"].values
y_hat.ravel() == y_validation

accuracy = (y_hat.ravel() == y_validation).sum() / y_validation.size
print("預測準確率為 {:.2f}%".format(accuracy * 100))

#使用SK learn來找theta
from sklearn.linear_model import LogisticRegression

train_df, validation_df = train_test_split(labeled_df, test_size=0.3, random_state=123)
X_train = train_df[["Fare", "Age"]].values
y_train = train_df["Survived"].values
X_validation = validation_df[["Fare", "Age"]].values
y_validation = validation_df["Survived"].values
clf = LogisticRegression()
clf.fit(X_train, y_train)
y_hat = clf.predict(X_validation)
accuracy = (y_hat == y_validation).sum() / y_hat.size
print("預測準確率為 {:.2f}%".format(accuracy * 100))

#使用package畫出Decision Boundary 資料點的分割線
!pip install mlxtend  #安裝mlxtend package
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt

validation_x_0 = validation_df.iloc[0, [5, 9]]
plot_decision_regions(labeled_df[["Fare", "Age"]].values, labeled_df["Survived"].values, clf = clf, res = 0.1)
plt.scatter(validation_x_0[1], validation_x_0[0], marker="*", s=500, color="g")
plt.xlabel('Fare')
plt.ylabel('Age')
plt.xlim(0, 300)
plt.title('Logistic Regression on Titanic')
plt.show()

#在圖中的分界線就是X%*%theta
#在分界線右邊的X%*%theta都是>0的
#線的左邊則是<0的，因此在線右邊預測錯的就是false positive(實際為0但預測為1)
#在線左邊預測錯的則是false negative
#這張圖提供的訊息: 整體來說若Fare(船票價)越大，存活機會越大，另外Age越小，
#                 存活的機會也越大
#注意: 可再加入不同次方的變數讓分界線從直線變成曲線甚至是多條的分界線

#自行畫出Decision Boundary 資料點的分割線
#第一種類型的圖
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def step(g_y_hat, threshold=0.5):
    return np.where(g_y_hat >= threshold, 1, 0).reshape(-1, 1)

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
survived = labeled[labeled["Survived"] == 1]
dead = labeled[labeled["Survived"] == 0]
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, ["Fare", "Age"]].values
y_train = train.loc[:, "Survived"].values
logistic_clf = LogisticRegression()
logistic_clf.fit(X_train, y_train)
fit_intercept = logistic_clf.intercept_.reshape(-1, 1)
fit_coef = logistic_clf.coef_.reshape(-1, 1)
thetas = np.concatenate([fit_intercept, fit_coef])
# Decision boundary plot
fare_min, fare_max = labeled["Fare"].min(), labeled["Fare"].max()
age_min, age_max = labeled["Age"].min(), labeled["Age"].max()
fare_arr = np.linspace(fare_min - 5, fare_max + 5, 1000)
age_arr = np.linspace(age_min - 5, age_max + 5, 1000)
xx, yy = np.meshgrid(fare_arr, age_arr)
ones = np.ones(xx.size).reshape(-1, 1)
X_grid = np.concatenate([ones, xx.reshape(-1, 1), yy.reshape(-1, 1)], axis=1)
y_grid = np.dot(X_grid, thetas)
g_y_grid = sigmoid(y_grid)
y_grid_pred = step(g_y_grid)
Z = y_grid_pred.reshape(xx.shape)
plt.scatter(survived["Fare"], survived["Age"], label="Survived", marker="o", color="blue")
plt.scatter(dead["Fare"], dead["Age"], label="Dead", marker="x", color="red")
plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm_r)
plt.legend(loc="upper right")
plt.xlabel("Fare")
plt.ylabel("Age")
plt.show()

#第二種類型的圖
from matplotlib.colors import ListedColormap

def decision_boundary(X, labeled_df, clf):
    x1_min, x1_max = X[:,0].min()-5, X[:,0].max()+5,
    x2_min, x2_max = X[:,1].min()-5, X[:,1].max()+5,
    xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    thetas = np.hstack((clf.intercept_, clf.coef_.ravel())).reshape(-1, 1)
    ones = np.ones(xx1.size).reshape(-1, 1)
    xx_concat = np.concatenate([ones, xx1.reshape(-1, 1), xx2.reshape(-1, 1)], axis=1)
    h = sigmoid(xx_concat.dot(thetas))
    h = h.reshape(xx1.shape)
    plot_data(labeled_df, "Fare", "Age", "Survived", "Dead", "Survived")
    plt.contour(xx1, xx2, h, [0.5], linewidths=3, colors='#FF69B4')
    #cmap=ListedColormap(["y", "k"])
    #plt.contourf(xx1, xx2, h, alpha=0.3, cmap=cmap, antialiased=True)
    plt.xlim(0, x1_max)
    plt.ylim(0, x2_max)

decision_boundary(labeled_df[["Fare", "Age"]].values, labeled_df, clf)
validation_x_0 = validation_df.iloc[0, [5, 9]]
plt.scatter(validation_x_0[1], validation_x_0[0], marker="*", s=500, color="g") #標出某一個特定點
plt.show()

#加入不同的次方向讓分界線不再是直線
from sklearn.preprocessing import PolynomialFeatures

train_df, validation_df = train_test_split(labeled_df, test_size=0.3, random_state=123)
X_train = train_df[["Fare", "Age"]].values
y_train = train_df["Survived"].values
X_validation = validation_df[["Fare", "Age"]].values
y_validation = validation_df["Survived"].values

d = 6
X_train_poly = PolynomialFeatures(d).fit_transform(X_train)
X_validation_poly = PolynomialFeatures(d).fit_transform(X_validation)

clf_poly = LogisticRegression()
clf_poly.fit(X_train_poly, y_train)
y_hat = clf_poly.predict(X_validation_poly)
accuracy = (y_hat == y_validation).sum() / y_hat.size
print("預測準確率為 {:.2f}%".format(accuracy * 100))


def decision_boundary(X, labeled_df, clf):
    x1_min, x1_max = X[:,0].min()-5, X[:,0].max()+5,
    x2_min, x2_max = X[:,1].min()-5, X[:,1].max()+5,
    xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    thetas = np.hstack((clf.intercept_, clf.coef_.ravel())).reshape(-1, 1)
    xx_concat = np.concatenate([xx1.reshape(-1, 1), xx2.reshape(-1, 1)], axis=1)
    d = 6
    xx_concat_poly = PolynomialFeatures(d).fit_transform(xx_concat)
    ones = np.ones(xx1.size).reshape(-1, 1)
    xx_concat_poly = np.concatenate([ones, xx_concat_poly], axis=1)
    h = sigmoid(xx_concat_poly.dot(thetas))
    h = h.reshape(xx1.shape)
    plot_data(labeled_df, "Fare", "Age", "Survived", "Dead", "Survived")
    plt.contour(xx1, xx2, h, [0.5], linewidths=3, colors='#FF69B4')
    #cmap=ListedColormap(["y", "k"])
    #plt.contourf(xx1, xx2, h, alpha=0.2, cmap=cmap, antialiased=True)
    plt.xlim(0, x1_max)
    plt.ylim(0, x2_max)
    
decision_boundary(labeled_df[["Fare", "Age"]].values, labeled_df, clf_poly)
plt.show()

#延伸二元分類至多元分類: One vs. All
#數字文字辨識
import pandas as pd

labeled_df_url = "https://storage.googleapis.com/kaggle_datasets/Digit-Recognizer/train.csv"
test_df_url = "https://storage.googleapis.com/kaggle_datasets/Digit-Recognizer/test.csv"

labeled_df = pd.read_csv(labeled_df_url)
test_df = pd.read_csv(test_df_url)
labeled_df.head()
test_df.head()

X_train_arr = labeled_df.iloc[:, 1:].values.astype(float)
y_train_arr = labeled_df.iloc[:, 0].values.astype(float)
X_test_arr = test_df.values.astype(float)
#資料介紹
#label: 圖片中所代表的數字
#pixel no.: 784個像素(28*28)的資料
#將資料轉成矩陣
first_obs = labeled_df.iloc[0, 1:].values.reshape(28, 28)
fourth_obs = labeled_df.iloc[3, 1:].values.reshape(28, 28)
#將0,1資料視覺化轉乘影像檔
plt.imshow(first_obs, cmap = "gray")
plt.show()
plt.imshow(fourth_obs, cmap = "gray")
plt.show()

#建模
#單純的logistic regression事實上就可以說是一層神經網絡系統
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

clf = LogisticRegression(C=100000) #C代表regularization的lambda參數
acc = np.mean(cross_val_score(clf, 
                              X_train_arr[:3000, :], 
                              y_train_arr[:3000], 
                              cv = 10, 
                              scoring = 'accuracy')) 
# not to takes too long...
print("準確率：{:.2f}%".format(acc*100))
