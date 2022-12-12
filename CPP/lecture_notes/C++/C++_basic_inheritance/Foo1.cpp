# include <iostream>
#include "Foo1.h"

Foo1::Foo1(){
    std::cout << "Foo1建構函式" << std::endl;
}

Foo1::~Foo1(){
    std::cout << "Foo1解構函式" << std::endl;
}
