#include <iostream>
#include <string>

class Encrypt:{
  public:
    // declare the constructor
    Encrypt();
    // declare setter and getter member function
    void set_code_array();
    std::string get_code_array();
    // declare encode and decode member function
    std::string to_encode(std::string);
    std::string to_decode(std::string);
  
  private:
    // secret code string
    std::string code_array;
};