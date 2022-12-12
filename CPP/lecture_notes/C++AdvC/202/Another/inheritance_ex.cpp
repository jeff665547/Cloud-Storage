// C++ program to demonstrate the working of friend class

#include <iostream>
using namespace std;

// forward declaration
class ClassB;

class ClassA {
    private:
        int numA;

        // friend class declaration
        // friend class ClassB;

    public:
        int AA;
        // constructor to initialize numA to 12
        ClassA(){
            numA = 12;
            AA = 10000;
        }
};

class ClassB {
    private:
        int numB;

    public:
        // constructor to initialize numB to 1
        ClassB(){
            numB = 1;
        }
    
    // member function to add numA
    // from ClassA and numB from ClassB
    // int add() {
    //     ClassA objectA;
    //     return objectA.numA + numB;
    // }

    int add2(){
        ClassA obA;
        return obA.AA;
    }
};

int main() {
    ClassB objectB;
    cout << "Sum: " << objectB.add2();
    return 0;
}