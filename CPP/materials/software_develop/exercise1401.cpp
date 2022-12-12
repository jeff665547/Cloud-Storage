#include <iostream>

int main(){

    int a[10];

    for(int i = 0; i < 10; i++){
        a[i] = i;
        std::cout << a[i] << std::endl;
    }

    return 0;
}