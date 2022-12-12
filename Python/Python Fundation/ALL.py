import requests
res = requests.get("https://world.taobao.com/search/json.htm?navigator=all&_ksTS=1500588188617_28&spm=a21bp.7806943.20151106.1&search_type=0&_input_charset=utf-8&json=on&q=%E4%BF%9D%E6%B8%A9%E6%9D%AF&cna=n7b3ESvHAicCAXap4HkG9pdE&callback=__jsonp_cb&abtest=_AB-LR517-LR854-LR895-PR517-PR854-PR895&nid=&type=&uniqpid=")
import json 
import re
m = re.search("if\(window.__jsonp_cb\)\{__jsonp_cb\((.*?)\)\}", res.text)
print (m.group(1))
jd = json.loads(m.group(1))
jd

with open("a.json", "w") as f: 
    f.write(json.dumps(jd))
    
for item in jd["itemList"]:
    print (item['nick'], item['price'])
