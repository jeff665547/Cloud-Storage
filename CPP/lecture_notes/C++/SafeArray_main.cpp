#include <iostream>
#include "SafeArray.h"

int main(){
    SafeArray safeArray(10);

    for(int i = 0; i < safeArray.length; i++){
        safeArray.set(i, (i + 1)*10);
    }

    for(int i = 0; i < safeArray.length; i++){
        std::cout << safeArray.get(i) << " ";
    }

    std::cout << std::endl;
    
    return 0;
}