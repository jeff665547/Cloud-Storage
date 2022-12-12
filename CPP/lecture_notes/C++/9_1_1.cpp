#include <iostream>
#include <string>
#include "9_1_1.h"

Pokemon::Pokemon(){
    
    Name = "Pikachu";
    Lv = 10;
    HpMax = 10;
    HpCurrent = 10;

}

Pokemon::Pokemon(std::string name, int lv, 
int hpmax, int hpcurrent){
    
    Name = name;
    Lv = lv;
    HpMax = hpmax;
    HpCurrent = hpcurrent;

}

Pokemon::~Pokemon(){
    std::cout << "Game Over!!" << std::endl;
}

void Pokemon::ShowInfo(){

    std::cout << "Name: " << Name << std::endl;
    std::cout << "LV: " << Lv << std::endl;
    std::cout << "Max Hp: " << HpMax << std::endl;
    std::cout << "Current Hp: " << HpCurrent << std::endl;

}

void Pokemon::Attack(std::string target){
    std::cout << Name << " is attacking " << target << std::endl;
}

void Pokemon::Defence(std::string atkp){
    std::cout << atkp << " is attacking, and " << Name << " is defending." << std::endl;
}

void Pokemon::Cure(){
    HpCurrent = HpMax;
    std::cout << Name << " is cured." << std::endl;
}
