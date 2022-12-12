#include <iostream>
#include <string>
#include "encrypt.hpp"

int main(){

    std::cout << std::endl;

    Encrypt encryptor;

    std::cout << encryptor.get_code_array() << std::endl << std::endl;

    std::string d = "There is no spoon.";
    std::cout << d << std::endl;

    std::string r1 = encryptor.to_encode(d);
    std::cout << r1 << std::endl << std::endl;

    std::string r2 = encryptor.to_decode(r1);
    std::cout << r2 << std::endl << std::endl;

    return 0;
}
