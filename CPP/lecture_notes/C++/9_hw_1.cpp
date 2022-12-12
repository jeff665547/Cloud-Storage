#include <iostream>
#include "9_hw_1.h"

eCash::eCash(){
    Money = 0;
}
eCash::~eCash(){
    std::cout << "Bye~" << std::endl;
}
void eCash::store(int m){
    Money += m;
    std::cout << "Money: " << Money << std::endl;
}
void eCash::pay(int m){
    if (m > Money)
    {
        std::cout << "The money is not enough!" << std::endl;
    }else{
        Money -= m;
        std::cout << "Money: " << Money << std::endl;
    }
}
void eCash::display(){
    std::cout << "Money: " << Money << std::endl;
}