#include <iostream>

int main(){

    char table[26];

    for(int i = 0; i < 26 ; i++){
        table[i] = 97 + i;
        std::cout << table[i] << std::endl;
    }

    return 0;
}