Ans = input()

while (True):
    m = input()
    countA = 0
    countB = 0
    for i in range(0, 4):
        if(Ans.find(m[i]) != -1):
            if(Ans[i] == m[i]):
                countA += 1
            elif(Ans[i] != m[i]):
                countB += 1
    if(Ans == m):
        print(countA,"A", countB, "B", sep = "")
        print("You Win!")
        break
    
    else:
        print(countA,"A", countB, "B", sep = "")
        continue
    
