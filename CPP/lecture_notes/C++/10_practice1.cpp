#include <iostream>
#include "10_practice1_1.h"

int main(){
    Point2D p1(5, 5);
    Point2D p2(10, 10);
    Point2D p3;

    p3 = p2 - p1;
    std::cout << "p3(x, y) = (" << p3.getX() << "\t," << p3.getY() << ")" << std::endl;

    p3 = p2 * p1;
    std::cout << "p3(x, y) = (" << p3.getX() << "\t," << p3.getY() << ")" << std::endl;

    Point2D p4(11, 22), p5;
    p5 = p4 + 10;
    std::cout << "p5(x, y) = (" << p5.getX() << "\t," << p5.getY() << ")" << std::endl;

    return 0;
}