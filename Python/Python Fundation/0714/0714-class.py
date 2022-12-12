"apple".strip
st1 = "        1234      \n\t     "
print(st1)
eval(st1)
st1.strip() # 把前後(但中間沒有)非文字或數字的東西給清理掉，這樣才可以轉，但list不行，為字串專用  () 內放要刪除的東西
n1 = [1,2,3]
n1.strip
"Apple".swapcase #把全部的字元大小寫互換
st1.strip("  \t\n34")
st1.lstrip("  \t\n34") #刪左邊
st1.rstrip("  \t\n34") #刪右邊

st2 = "This is an apple."
st2.title()
st2.upper()
st2.lower()
#n2 = 0987654321
n2 = 987654321
n2
st3 = str(n2)
st4 = "0987654321"

st4.zfill(10)
#
string = input()
print(string.upper())

b = print(123)
repr(b)#去看函數真正的樣子

st1.upper()[1]

st1 = "Apple"
st1.isupper()

images = "xbox.gif,iphone.jpg"
st2 = "This is an Apple"
st2.isalnum() #因為有空白, 所以false
"123".isdigit()
"-123".isdigit() #只有字串才能做此判斷，若為數值就不能判斷
"123.46".isdigit()
"".isspace()#為空字串，並非空白
" ".isspace()
"\t".isspace()

n1 = input()

while(n1.isdigit()==0):
    print("is not a number")
    n1 = input()
    continue
    if (n1.isdigit()):
        break
print("n={}".format(n1))

st1 ="apple"
AA = " apple"
BB = "apple123"
CC = "     "

st1.isalnum()
st1.isalpha()
st1.islower()

AA.isalnum()
BB.isalnum() #只接受字元(小寫a~z, 大寫A~Z, 0~9)
BB.isalpha() 
st1.isalpha() #只接受英文字母
st1.isspace()
CC.isspace()

images = "xbox.gif, iphone.jpg"
images.endswith(".jpg")
images.endswith(" .gif", 0, 8)   #str.endswith("target", start, end)
images.endswith(".gif", 0, 8)
images.endswith(".gif")


#適合作文字檔名清理
f1 = "01_2017_7_14.jpg"
f1.split()
f1.split("_")
f1.split("_", maxsplit = 1)
f1.partition("_")

s = "A clear conscience laughs at false accusation."
print(s.count("a"))

for i in range(len(s)):
    print(i , s[i])

print(s.count("a"))
print(s.count("a",6))
print(s.count("a",36))

s = "A friend in need is a friend indeed."

for i in range(len(s)):
    print(i , s[i])
    
print(s.find("firend"))
print(s.find("friend", 2+1))
print(s.find("friend", 22+1))

print()
 


s1 = "Welcome to Python World Game."
s2 = "Can you can a can as a canner can can a can?"
s3 = "Few free fruit flies fly from flames."
s4 = "Czngrxtulxtizns, yzu hxve pxssed the czmpetitizn."

A1 = s1.split(" ")
A2 = s2.count("a")
A3 = s3.find("fly")
A4 = s4.replace("z", "o")
A4 = A4.replace("x","a")

print(s1, A1, s2, A2, s3, A3, s4, A4, sep = "\n")

s = "An uncut gem goes not sparkle."
s.index("o")
s.index("t", 15)
s.index("t", 5, 15)  #第一個輸入為target, 再來是start, 再來是end的位置
s.index("A", 0, 15)  #輸出的結果(注意:第一個字母的索引值為0)是從start的索引值開始找起(包含起始所引值(0)也要找)


s1 = """
漢皇重色思傾國，	　御宇多年求不得。
楊家有女初長成，	　養在深閨人未識。
天生麗質難自棄，	　一朝選在君王側。
回眸一笑百媚生，	　六宮粉黛無顏色。
春寒賜浴華清池，	　溫泉水滑洗凝脂。
侍兒扶起嬌無力，	　始是新承恩澤時。
雲鬢花顏金步搖，	　芙蓉帳暖度春宵。
春宵苦短日高起，	　從此君王不早朝。
承歡侍宴無閒暇，	　春從春遊夜專夜。
後宮佳麗三千人，	　三千寵愛在一身。
金屋妝成嬌侍夜，	　玉樓宴罷醉和春。
姊妹兄弟皆列土，	　可憐光彩生門戶。
遂令天下父母心，	　不重生男重生女。
驪宮高處入青雲，	　仙樂風飄處處聞。
緩歌慢舞凝絲竹，	　盡日君王看不足。
漁陽鼙鼓動地來，	　驚破霓裳羽衣曲。
九重城闕煙塵生，	　千乘萬騎西南行。
翠華颻颻行復止，	　西出都門百餘里。
六軍不發無奈何，	　宛轉蛾眉馬前死。
花鈿委地無人收，	　翠翹金雀玉搔頭。
君王掩面救不得，	　回看血淚相和流。
黃埃散漫風蕭索，	　雲棧縈紆登劍閣。
峨嵋山下少人行，	　旌旗無光日色薄。
蜀江水碧蜀山青，	　聖主朝朝暮暮情。
行宮見月傷心色，	　夜雨聞鈴腸斷聲。
天旋日轉回龍馭，	　到此躊躇不能去。
馬嵬坡下泥土中，	　不見玉顏空死處。
君臣相顧盡霑衣，	　東望都門信馬歸。
歸來池苑皆依舊，	　太液芙蓉未央柳。
芙蓉如面柳如眉，	　對此如何不淚垂。
春風桃李花開日，	　秋雨梧桐葉落時。
西宮南內多秋草，	　落葉滿階紅不掃。
梨園弟子白髮新，	　椒房阿監青娥老。
夕殿螢飛思悄然，	　孤燈挑盡未成眠。
遲遲鐘鼓初長夜，	　耿耿星河欲曙天。
鴛鴦瓦冷霜華重，	　翡翠衾寒誰與共。
悠悠生死別經年，	　魂魄不曾來入夢。
臨邛道士鴻都客，	　能以精誠致魂魄。
為感君王輾轉思，	　遂教方士殷勤覓。
排雲馭氣奔如電，	　昇天入地求之遍。
上窮碧落下黃泉，	　兩處茫茫皆不見。
忽聞海上有仙山，	　山在虛無縹緲間。
樓閣玲瓏五雲起，	　其中綽約多仙子。
中有一人字太真，	　雪膚花貌參差是。
金闕西廂叩玉扃，	　轉教小玉報雙成。
聞道漢家天子使，	　九華帳裏夢魂驚。
攬衣推枕起徘徊，	　珠箔銀屏迤邐開。
雲髻半偏新睡覺，	　花冠不整下堂來。
風吹仙袂飄颻舉，	　猶似霓裳羽衣舞。
玉容寂寞淚闌干，	　梨花一枝春帶雨。
含情凝睇謝君王，	　一別音容兩渺茫。
昭陽殿裏恩愛絕，	　蓬萊宮中日月長。
回頭下望人寰處，	　不見長安見塵霧。
唯將舊物表深情，	　鈿合金釵寄將去。
釵留一股合一扇，	　釵擘黃金合分鈿。
但教心似金鈿堅，	　天上人間會相見。
臨別殷勤重寄詞，	　詞中有誓兩心知。
七月七日長生殿，	　夜半無人私語時。
在天願作比翼鳥，	　在地願為連理枝。
天長地久有時盡，	　此恨綿綿無絕期。
"""

qstr = input()
qct = s1.count(qstr)
print(qct)










