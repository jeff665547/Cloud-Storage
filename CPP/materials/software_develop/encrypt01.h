// 類別 (class) 為 C++ 開發軟體 (software) 的要角，
// 因為類別用來設計物件，軟體的實際運作則是藉由物件與物件的互動。

#include <string>

class Encrypt {
  public:
    // declare the construct function
    Encrypt();

    // declare the setter and getter member function 
    void set_code_array();
    std::string get_code_array();
    // declare encoding and decoding member function
    std::string to_encode(std::string);
    std::string to_decode(std::string);

  private:
    // 密碼表字串符
    std::string code_array;
};

