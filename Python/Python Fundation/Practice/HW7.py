class student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
    
    def avg(self):
        return(sum(self.grades)/len(self.grades))
    
    def add(self, grade):
        self.grades.append(grade)
        
    def fcount(self):
        fct = 0
        for g in self.grades:
            if g < 60:
                fct += 1
        return fct
        
    def show(self):
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Grades:", self.grades)
        print("Avg: %.1f" %(self.avg()))
        print("Fail Number:", self.fcount())
        print()
                
def top(*stu):
    lst = []
    for n in stu:
        n.show()
        lst.append(n.avg())
    avgall = dict(zip(tuple(lst), stu))
    sh = avgall[max(lst)]
    print("Top Student:")
    print("Name:", sh.name)
    print("Gender:", sh.gender)
    print("Grades:", sh.grades)
    print("Avg:" , sh.avg())
    print("Fail Number:", sh.fcount())
    print()

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

#stu = [s1, s2, s3, s4, s5]
top(s1, s2, s3, s4, s5)
