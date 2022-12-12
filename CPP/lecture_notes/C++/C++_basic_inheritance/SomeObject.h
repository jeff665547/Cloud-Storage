#ifndef SOMEOBJECT
#define SOMEOBJECT

#include <iostream>
using namespace std;

class SomeObject{
    public:
        virtual void someFunction(){
            std::cout << "do something" << std::endl;
        }
    
    private:
        void otherFunction(){
            std::cout << "do other" << std::endl;
        }
};

#endif