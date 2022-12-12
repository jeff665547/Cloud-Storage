#include "IRequest.h"
#include "SomeObject.h"
#include <iostream>
using namespace std;

class Welcome : public SomeObject, public IRequest{
    public:
        void execute(){
            std::cout << "Welcome!!" << std::endl;
        }
};
