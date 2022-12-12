
n = input()
m = input()

pos = 0

while (True):
        
    pos = n.find(m, pos)
    
    if (pos == -1):
        break
    else:
        print(pos)
    pos = pos + len(m)
    

    
