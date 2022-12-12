#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

class student{
    public:
        student(std::string name, char gender);
        std::string NAME;
        char GENDER;
        std::vector<double> GRADES;

        double avg();
        void add(int grade);
        int fcount();
        void show();
};

student::student(std::string name, char gender){
    NAME = name;
    GENDER = gender;
}

void student::add(int grade){
    GRADES.push_back(grade);
};

int student::fcount(){
    int count = 0;
    for(int i = 0; i < GRADES.size(); i++){
        if(GRADES[i] < 60){
            count += 1;
        }
    }
    return count;
}

double student::avg(){
    double sum = 0;
    double tmp;
    for(int i = 0; i < GRADES.size(); i++){
        sum += GRADES[i];
    }
    tmp = sum/GRADES.size();
    return tmp;
}

void student::show(){
    std::cout << "Name: " << NAME << std::endl;
    std::cout << "Gender: " << GENDER << std::endl;
    std::cout << "Grades: [";
    for(int i = 0; i < GRADES.size(); i++){
        std::cout << GRADES[i];
        if(i != GRADES.size() - 1){
            std::cout << ", ";
        }else{
            std::cout << "]" << std::endl;
        }
    }
    printf("Avg: %.1f\n", avg());
    std::cout << "Fail Number: " << fcount();
}

student top(student *ptr, int num){
    
    student tmp("None", 'F');
    for (int i = 0; i < num; i++){
        if(ptr[i].avg() > ptr[i+1].avg()){
            tmp = ptr[i];
            ptr[i] = ptr[i+1];
            ptr[i+1] = tmp;
        }
    }
    
    return ptr[num];
}

int main(){

    student s1("Tom", 'M');
    student s2("Jane", 'F');
    student s3("John", 'M');
    student s4("Ann", 'F');
    student s5("Peter", 'M');

    s1.add(80);
    s1.add(90);
    s1.add(55);
    s1.add(77);
    s1.add(40);
    s2.add(58);
    s2.add(87);
    s3.add(100);
    s3.add(80);
    s4.add(40);
    s4.add(55);
    s5.add(60);
    s5.add(60);

    student ptr[5] = {s1, s2 ,s3, s4, s5};

    for (size_t i = 0; i < 5; i++){
        ptr[i].show();
        std::cout << std::endl << std::endl;
    }
    
    std::cout << "Top Student:" << std::endl;
    student tmp = top(ptr, 5);
    tmp.show();
    std::cout << std::endl;
    std::cout << std::endl;
    return 0;
}
