# include <iostream>
# include "9_practice_1.h"

int main(){

    Square s1(10);
    s1.getLen();
    std::cout << "The area of square 1 is " << s1.area() << "." << std::endl;

    Square s2(20);
    s2.setLen(30);
    s2.getLen();
    std::cout << "The area of square 2 is " << s2.area() << "."  << std::endl;

    return 0;
}
