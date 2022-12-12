#include <iostream>
#include <string>
#include <stdio.h>

class student{
    public:
        std::string name;
        char gender;
        double grades[3];

        double avg();
        void add(int grade);
        int fcount();
        void show();
    
};

double student::avg(){
    
    double count = sizeof(grades)/sizeof(double);
    double sum = 0;

    for(int i = 0; i < count; i++){
        sum += grades[i];
    }

    double tmp = sum/count;
    return tmp;
}

void student::add(int grade){

    int count = sizeof(grades)/sizeof(double);
    grades[count] = grade;

}

int student::fcount(){

    int count = sizeof(grades)/sizeof(double);
    int ct_fail = 0;

    for(int i = 0; i < count; i++){
        if(grades[i] < 60){
            ct_fail += 1;
        }
    }
    return ct_fail;
}

void student::show(){
    std::cout << name << std::endl;
}

int main(){
    std::string input_name;
    char input_gender;

    std::cin >> input_name;
    std::cin >> input_gender;
    
    student A;
    A.name = input_name;
    A.gender = input_gender;
    for(int i = 0; i < 3; i++){
        std::cin >> A.grades[i];
    }

    
    std::cout << A.name << std::endl;
    printf("%.2f\n", A.avg());
    std::cout << A.fcount() << std::endl;

    return 0;
}