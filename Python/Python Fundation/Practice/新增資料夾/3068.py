AA = dict(zip(("P", "M", "H"),("Pikachu", "Micky Mouse", "Hello kitty")))

while (True): 
    
    n = input()
    
    if (n == "-1"):
        break
    elif(n == "-2"):
        print(AA.keys())
        print(AA.values())
        continue
    elif(n in AA):
        print(AA[n])
        continue
    else:
        print(n, "does not exist. Enter a new one:")
        m = input()
        AA[n] = m
        continue
        
