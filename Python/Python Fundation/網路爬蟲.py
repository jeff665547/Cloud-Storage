import requests
from bs4 import BeautifulSoup
#Use Chrome and Postman to get the URL of the web 
res = requests.get("https://world.taobao.com/search/json.htm?navigator=all&_ksTS=1500588188617_28&spm=a21bp.7806943.20151106.1&search_type=0&_input_charset=utf-8&json=on&q=%E4%BF%9D%E6%B8%A9%E6%9D%AF&cna=n7b3ESvHAicCAXap4HkG9pdE&callback=__jsonp_cb&abtest=_AB-LR517-LR854-LR895-PR517-PR854-PR895&nid=&type=&uniqpid=")
#print(res.text)  #把網路頁面的資訊(原始碼)給擷取下來
#Use DOM to get the important message from the website.
#soup = BeautifulSoup(res.text)
#print(soup.text) #把裡面全部的內容給印出，過濾有用的資料
#print(soup.select(".item")) #尋找東西  id: #id名稱  class: .class名稱
#正規表達法把法篩出資料
import json 
import re
#re.search("if(window.__jsonp_cb){__jsonp_cb(放入需要尋找的字串)}")
m = re.search("if\(window.__jsonp_cb\)\{__jsonp_cb\((.*?)\)\}", res.text) # .* 代表甚麼都要
print (m.group(1)) #1代表(.*?)
#Use json 將資料讀進來
jd = json.loads(m.group(1))
jd
#不要其他的資訊 我們只要商品的資訊
with open("a.json", "w") as f: #資料寫入
    f.write(json.dumps(jd))  #jd為python的字典  要先變成json格式後再寫入檔案a.json
#用chrome檢視此json檔 並到network的地方去做重新再入接著在到裡面的all找到該當案之後讓他priview, 它會自動排版
#找到要的資料的網頁程式碼位置(itemList), 接著看需要那些東西的資料，並且用for迴圈把它給取出
for item in jd["itemList"]:
    print (item['nick'], item['price'])
#or 利用pandas將此網頁所要的資料整理成一個表格
import pandas
df = pandas.DataFrame(jd["itemList"])
df

############################################
#scrapy  能同時進行多個爬蟲


    