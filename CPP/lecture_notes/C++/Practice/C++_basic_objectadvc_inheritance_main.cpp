# include <iostream>
# include "C++_basic_objectadvc_inheritance_more.h"

int main(){

    // Inheritance: public member
    Point3D p1(1, 3, 4);
    Point3D p2;

    std::cout << "p1: (" << p1.x() << ", "
    << p1.y() << ", " << p1.z() << ")" << std::endl;

    p2.x(5);
    p2.y(7);
    p2.z(8);

    std::cout << "p2: (" << p2.x() << ", " 
    << p2.y() << ", " << p2.z() << ")" << std::endl;


    // Inheritance: private member
    Cubic c1(0, 0, 0, 10, 20, 30);

    std::cout << "c1 volumn: " << c1.volumn() << std::endl;

    // Redifinition of the member function
    Fool f1;
    Fool2 f2;

    f1.show();
    f2.show();

    // 繼承後的建構函式與解構函式
    class Foo1{
        public:
            Foo1(){
                std::cout << "Foo1's constructor" << std::endl;
            }

            ~Foo1(){
                std::cout << "Foo1's destructor" << std::endl;
            }
    };

    class Foo2 : public Foo1 {
        public:
            Foo2(){
                std::cout << "Foo2's constructor" << std::endl;
            }
            ~Foo2(){
                std::cout << "Foo2's destructor" << std::endl;
            }
    };

    Foo2 f;
    std::cout << std::endl;

    return 0;
}