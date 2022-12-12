#include <iostream>
#include "IRequest.h"
#include "SomeObject.h"
using namespace std;

class Hello : public SomeObject, public IRequest {
    public:
        void execute(){
            std::cout << "Hello!!" << std::endl;
        }
};