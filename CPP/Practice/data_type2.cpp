#include <iostream>
// 1 Byte (位元組, B)
// 1 Bit (位元, b)
// 1 個位元組代表 8 個位元 (1 Byte = 8 Bits)
// MB = Megabyte, Mb = Megabit

int main(){
    
    std::cout << "The size of int is " << sizeof(int) << " bytes" << std::endl;
    std::cout << "The size of double is " << sizeof(double) << " bytes" << std::endl;

    return 0;
}
