// 您可以使用static_cast（甚至是傳統的C轉型方式）將基底類別指標轉換為衍生類別指標，
// 這種轉型方式是強制轉型，在執行時期使用強制轉型有危險性，
// 因為編譯器無法得知轉型是否正確，執行時期真正指向的物件型態是未知的，
// 透過簡單的檢查是避免錯誤的一種方式。
// e.g. RTTI.cpp 中的 typeid(*base) == typeid(Derived1)

// 使用dynamic_cast
#include <iostream>
#include <typeinfo>
using namespace std;

class Base{
    public:
        virtual void foo() = 0;
};

class Derived1 : public Base{
    public:
        void foo(){
            std::cout << "Derived1" << std::endl;
        }

        void showOne(){
            std::cout << "Yes! It's Derived1." << std::endl;
        }
};

class Derived2: public Base{
    public:
        void foo(){
            std::cout << "Derived2" << std::endl;
        }

        void showTwo(){
            std::cout << "Yes! It's Derived2." << std::endl;
        }
};

void showWho(Base &base){  // arguments 使用 reference, 
                           // dynamic_cast在轉換失敗之後會丟出bad_cast例外，
                           // 所以必須使用try...catch來處理例外
    try{
        Derived1 derived1 = dynamic_cast<Derived1&>(base);
        derived1.showOne();
    }
    catch(bad_cast){
        std::cout << "bad_cast convert fails!" << std::endl;
    }
}

int main(){
    Derived1 derived1;
    Derived2 derived2;

    showWho(derived1);
    showWho(derived2);

    return 0;
}
