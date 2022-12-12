# Practice 01
class student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
    
    def avg(self):
        summ = 0
        ct = 0
        
        for i in self.grades:
            summ += i
            ct += 1
        return summ/ct
        
    def add(self, grade):
        self.grades.append(grade)
        
    def fcount(self):
        ct = 0
        for i in self.grades:
            if(i < 60):
                ct += 1
        return ct

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

s1.avg()
s1.fcount()
s2.avg()
s2.fcount()
s3.avg()
s3.fcount()
s4.avg()
s4.fcount()

def top(stu_list):
    for i in range(len(stu_list) - 1):
        if(stu_list[i].avg() > stu_list[i+1].avg()):
            tmp = stu_list[i]
            stu_list[i] = stu_list[i+1]
            stu_list[i+1] = tmp
        
    return stu_list[len(stu_list) - 1].name

top([s1, s2, s3, s4, s5])


#%%
# Practice 02
class person:
    
    def __init__(self, name, gender, age):
        self.name = name
        self.__gender = gender
        self.__age = age
        
    def getGender(self):
        return self.__gender
    
    def getAge(self):
        return self.__age
    
    def sayHello(self):
        print("Hello, I am ", self.name, ", the gender is ", self.getGender(), 
              ", the age is ", self.getAge())
        
class course:
    
    def __init__(self, name):
        self.name = name
        self.teacher = "none"
        self.students = []
        self.grades = []
    
    def listMembers(self):
        print("The Teacher is ")
        print(self.teacher.name)
        print("Students: ")
        for i in self.students:
            print(i.name)
    
    def sayHello(self):
        print("Hello, I am {}, I am teaching {} course.".format(self.teacher.name, 
              self.name))
    
    def avg(self):
        summ = 0
        ct = 0
        for i in range(len(self.grades)):
            ct += 1
            summ += self.grades[i]
            
        return summ/ct

class student(person):
    
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.grade_list = []
    
    def addCourse(self, cc):
        if(self not in cc.students):
            cc.students.append(self)
                    
    def addGrades(self, cc, grade):
        cc.grades.append(grade)
        self.grade_list.append(grade)
        
    def removeCourse(self, cc):
        cc.students.remove(super().name)
        
    def avg(self):
        summ = 0
        ct = 0
        for i in range(len(self.grade_list)):
            ct += 1
            summ += self.grade_list[i]
            
        return summ/ct
    
    def fcount(self):
        ct = 0
        for i in range(len(self.grade_list)):
            if(self.grade_list[i] < 60):
                ct += 1
        
        return ct

class teacher(person):
    
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.course_list = []
        
    
    def addCourse(self, cc):
        cc.teacher = self
        self.course_list.append(cc)
        
    def removeCourse(self, cc):
        cc.teacher = ""
        self.course_list.remove(cc)
        
    def listStudents(self):
        for i in self.course_list:
            i.listMembers()
            
    def listNoPass(self):
        for i in range(len(self.course_list)):
            for j in range(len(self.course_list[i].students)):
                if(self.course_list[i].students[j].avg() < 60):
                    print(self.course_list[i].students[j].name)

#%%            
#student
s1 = student("Tom","M","20")
s2 = student("Jane","F","21")
s3 = student("John","M","21")
s4 = student("Ann","F","19")
s5 = student("Peter","M","20")
#teacher
t1 = teacher("JieFan","M","29")
t2 = teacher("Mary","F","26")
#course
c1 = course('python')
c2 = course('c++')
c3 = course('Java')

s2.name
#%%
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
s1.addCourse(c1)
s2.addCourse(c1)
s3.addCourse(c1)
s2.addCourse(c2)
s3.addCourse(c2)
s4.addCourse(c2)
s1.addGrades(c1,100)
s1.addGrades(c1,80)
s2.addGrades(c1,30)
s2.addGrades(c1,49)
s3.addGrades(c1,66)
s3.addGrades(c1,90)
s2.addGrades(c2,88)
s2.addGrades(c2,65)
s3.addGrades(c2,30)
s3.addGrades(c2,88)
s4.addGrades(c2,47)
s4.addGrades(c2,98)
#%%
t1.listStudents()
t1.listNoPass()
c1.listMembers()
c1.avg()
c2.avg()
c1.sayHello()
