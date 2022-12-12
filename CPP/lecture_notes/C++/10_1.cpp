# include <iostream>
# include "10_1_1.h"

int main(){

    Point2D p1(5, 5);
    Point2D p2(10, 10);
    Point2D p3;

    p3 = p1 + p2;
    std::cout << "p3(x, y) = (" << p3.getX() << "," << p3.getY() << ")" << std::endl;

    p3 = p2 - p1;
    std::cout << "p3(x, y) = (" << p3.getX() << "," << p3.getY() << ")" << std::endl;

    Point2D p4(11, 22), p5;
    p5 = p4 + 10;
    std::cout << "p5(x, y) = (" << p5.getX() << "," << p5.getY() << ")" << std::endl;

    int aa = 10, bb = 20, cc;
    cc = aa + bb;
    std::cout << cc << std::endl;

    return 0;
}