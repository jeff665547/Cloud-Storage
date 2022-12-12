// C++中用來取得指標或參考所實際代表的物件，
// 您可以使用typeid()來取得物件於執行時期的資訊。
// 要使用typeid()，您必須包括<typeinfo>標頭檔。
// typeid()使用時傳入一個物件，
// 接著typeid()會回傳一個type_info物件，
// 其擁有幾個成員可以描述或進行物件的比較。
// 用範例來說明typeid()與其成員的使用方法與應用，
// 下面這個程式只是使用name()取得物件的型態名稱:

#include <iostream>
#include <typeinfo>
using namespace std;

class Base {
public: 
    virtual void foo() {
        cout << "Base" << endl;
    }
};

class Derived1 : public Base { 
public: 
    void foo() {
        cout << "Derived1" << endl;
    }
};

class Derived2 : public Base { 
public: 
    void foo() { 
        cout << "Derived2" << endl; 
    } 
}; 


// RTTI的使用時機
// RTTI的使用時機之一，就是當您將物件以參考方式傳遞給函式時，
// 函式的參數使用共同的基底類別指標或參考，
// 但在函式中有必須操作衍生類別中的某個方法，
// 由於函式事先並不知道您傳入的物件型態名稱，
// 所以您必須利用RTTI來進行判斷。
// e.g.
class Base2{
    public:
        virtual void foo() = 0;
};

class Derived21 : public Base2{
    public:
        void foo(){
            cout << "Derived21" << std::endl;
        }

        void showOne(){
            std::cout << "Yes! It's Derived21." << std::endl;
        }
};

class Derived22 : public Base2{
    public:
        void foo(){
            std::cout << "Derived22" << std::endl;
        }
        void showTwo(){
            std::cout << "Yes! It's Derived22." << std::endl;
        }
};

void showWho(Base2 *base){
    base->foo();

    if(typeid(*base) == typeid(Derived21)){ // 比較物件型態是否相同
        Derived21 *derived21 = static_cast<Derived21*>(base);  
        // C++ 強制轉型，也可以使用傳統C語言的強制轉型法，如: Derived21 *derived21 = (Derived21*) base;
        derived21 -> showOne();
    }
    else if(typeid(*base) == typeid(Derived2)){ // 比較物件型態是否相同
        Derived22 *derived22 = static_cast<Derived22*>(base);
        // C++ 強制轉型，也可以使用傳統C語言的強制轉型法，如: Derived21 *derived21 = (Derived21*) base;
        derived22 -> showTwo();
    }
}

int main() {

    // Section 1
    Base *ptr; // 基底類別指標
    Base base; 
    Derived1 derived1;
    Derived2 derived2;

    ptr = &base;
    cout << "ptr points to " 
         << typeid(*ptr).name()  // 取得物件的型態名稱
         << endl;

    ptr = &derived1;
    cout << "ptr points to "
         << typeid(*ptr).name()
         << endl;

    ptr = &derived2;
    cout << "ptr points to " 
         << typeid(*ptr).name() 
         << endl;

    // Section 2
    Derived21 derived21;
    Derived22 derived22;

    showWho(&derived21);
    showWho(&derived22);

    return 0;
}
