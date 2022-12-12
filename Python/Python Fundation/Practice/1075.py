
m = input()
n = input()

AA = []
if (m == "0-1.txt" or n == "0-1.txt"):
    f01 = open("../app/0-1.txt", "r")
    #f01 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/0-1.txt", "r", encoding = "UTF-8")
    data01 = f01.readlines()
    AA.append(data01)
    f01.close()
  
if(m == "0-2.txt" or n == "0-2.txt"):
    f02 = open("../app/0-2.txt", "r")
    #f02 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/0-2.txt", "r", encoding = "UTF-8")
    data02 = f02.readlines()
    AA.append(data02)
    f02.close()
'''    
if(m == "1-1.txt" or n == "1-1.txt"):
    f11 = open("../app/1-1.txt", "r", encoding = "UTF-8")
    #f11 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-1.txt", "r", encoding = "UTF-8")
    data11 = f11.readlines()
    AA.append(data11)
    f11.close()
    
if(m == "1-2.txt" or n == "1-2.txt"):
    f12 = open("../app/1-2.txt", "r", encoding = "UTF-8")    
    #f12 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-2.txt", "r", encoding = "UTF-8")
    data12 = f12.readlines()
    AA.append(data12)
    f12.close()
    
if(m == "2-1.txt" or n == "2-1.txt"):
    f21 = open("../app/2-1.txt", "r", encoding = "UTF-8")
    #f3 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-1.txt", "r", encoding = "UTF-8")
    data21 = f21.readlines()
    AA.append(data21)
    f21.close()
    
if(m == "2-2.txt" or n == "2-2.txt"):
    f22 = open("../app/2-2.txt", "r", encoding = "UTF-8")    
    #f4 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-2.txt", "r", encoding = "UTF-8")
    data22 = f22.readlines()
    AA.append(data22)
    f22.close()
    
if(m == "3-1.txt" or n == "3-1.txt"):
    f31 = open("../app/3-1.txt", "r", encoding = "UTF-8")
    #f3 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-1.txt", "r", encoding = "UTF-8")
    data31 = f31.readlines()
    AA.append(data31)
    f31.close()
    
if(m == "3-2.txt" or n == "3-2.txt"):
    f32 = open("../app/3-2.txt", "r", encoding = "UTF-8")    
    #f4 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-2.txt", "r", encoding = "UTF-8")
    data32 = f32.readlines()
    AA.append(data32)
    f32.close()
    

if(m == "4-1.txt" or n == "4-1.txt"):
    f41 = open("../app/4-1.txt", "r", encoding = "UTF-8")
    #f3 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-1.txt", "r", encoding = "UTF-8")
    data41 = f41.readlines()
    AA.append(data41)
    f41.close()
    
if(m == "4-2.txt" or n == "4-2.txt"):
    f42 = open("../app/4-2.txt", "r", encoding = "UTF-8")    
    #f4 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-2.txt", "r", encoding = "UTF-8")
    data42 = f42.readlines()
    AA.append(data42)
    f42.close()

if(m == "5-1.txt" or n == "5-1.txt"):
    f51 = open("../app/5-1.txt", "r", encoding = "UTF-8")
    #f3 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-1.txt", "r", encoding = "UTF-8")
    data51 = f51.readlines()
    AA.append(data51)
    f51.close()
    
if(m == "5-2.txt" or n == "5-2.txt"):
    f52 = open("../app/5-2.txt", "r", encoding = "UTF-8")    
    #f4 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1-2.txt", "r", encoding = "UTF-8")
    data52 = f52.readlines()
    AA.append(data52)
    f52.close()
'''    
BB = AA[0][0] + AA[1][0]
data = BB.split(" ")
data.pop()

out = []
for i in data:
    out.append(eval(i))

out.sort()
for j in range(0, len(out)):
    print(out[j], end = " ")
print()