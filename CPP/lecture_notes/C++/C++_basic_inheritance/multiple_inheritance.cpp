/* 多重繼承 */
// C++允許讓衍生類別同時直接繼承兩個以上的父類別，
// 例如有A、B兩個類別，您可以使用下面的方式來讓C類別直接繼承這兩個類別:
// class C : public A, public B { 
// public: 
//     C(int x) : A(x), B(x) {  // 多重繼承下的建構函式呼叫 
//         // 實作 
//     }    

//     // 實作 
// };
// 上面也同時示範了在繼承之後的的建構函式呼叫，
// 沒有參數的預設建構函式不用使用這種方式執行，它會自動被呼叫，
// 而解構函式也是會自動執行。 
// 多重繼承之後的建構函式執行順序，是依您撰寫程式時的順序由左而右決定，
// 最後才是繼承後衍生類別。
// 例如上面的例子中，會先執行A類別定義的建構函式，然後再執行B類別的建構函式，
// 最後執行C類別的建構函式，而解構函式的執行則正好相反，先執行衍生類別的解構函式，
// 然後再由右向左執行。

# include <iostream>

class FooA{
    public:
        FooA(){
            std::cout << "FooA's Constructor." << std::endl;
        }

        ~FooA(){
            std::cout << "FooA's Destructor." << std::endl;
        }
};

class FooB{
    public:
        FooB(){
            std::cout << "FooB's Constructor." << std::endl;
        }

        ~FooB(){
            std::cout << "FooB's Destructor." << std::endl;
        }
};

class FooC : public FooA, public FooB {
    public:
        FooC(){
            std::cout << "FooC's Constructor." << std::endl;
        }

        ~FooC(){
            std::cout << "FooC's Destructor." << std::endl;
        }
};

int main(){
    FooC c; // 二個父類別對一個子類別

    std::cout << std::endl;

    return 0;
}
