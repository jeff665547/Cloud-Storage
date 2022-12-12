
lst = []

for i in range(0, 5):
    student = input()
    student = student.split(" ")
    stulist = []
    for j in range(0, 3):
        stulist.append(eval(student[j]))
    lst.append(stulist)
    
total = 0
allavg = []
for i in range(0, 5):   
    print("student",i+1)
    student = lst[i]
    for j in range(0, 3):
        print(" ",j+1 , ": ", student[j], sep ="" )
        total += student[j]
    studentsum = sum(student)
    studentavg = studentsum/3
    allavg.append(studentavg)
    print(" sum: ", studentsum, sep = "")
    print(" avg: %.2f"%(studentavg))
      
print("total: ", total, ", avg: %.2f" %(total/15), sep = "")    
map = dict(zip((allavg),(1,2,3,4,5)))  
print("highest avg: student ", map[max(allavg)], ": %.2f"%(max(allavg)), sep = "")    

