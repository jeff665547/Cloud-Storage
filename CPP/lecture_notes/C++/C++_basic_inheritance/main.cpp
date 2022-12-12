// Virtual function 虛擬函式
//
// * 之前曾經介紹過函式與運算子的重載(Overload)，
//   重載可以使用一個函式名稱來執行不同的實作，
//   這是一種「編譯時期」就需決定的方式，這是「早期繫結」(Early binding)、
//   「靜態繫結」(Static binding)，因為在編譯時就可以決定函式的呼叫對象，
//   它們的呼叫位址在編譯時就可以得知。
//
// * 「虛擬函式」(Virtual function)可以實現「執行時期」的多型支援，
//   是一個「晚期繫結」(Late binding)、「動態繫結」(Dynamic binding)，
//   也就是指必須在執行時期才會得知所要調用的物件或其上的公開介面。
//
// * 在談虛擬函式之前必須先知道，一個基底類別的物件指標，
//   可以用來指向其衍生類別物件而不會發生錯誤，例如若基底類別是Foo1，
//   而衍生類別是Foo2，則下面這個指定是可以接受的:
//   Foo1 *fptr; 
//   Foo2 f2; 
//   fptr = &f2;
//
// * 多型與動態繫結的基礎從這開始，它們只有在使用指標或參考時才得以發揮它們的特性，
//   然而由於fptr仍是Foo1類型的指標，它只能存取Foo1中有定義的成員，目前來說也只能操作Foo1中的成員。
//
// * 注意將衍生類別型態的指標指向基底類別的物件基本是不可行的（雖然可以使用型態轉換的方式來勉強達成，但並不鼓勵），
//   衍生類別的指標並不能存取基底類別的成員。
// 
// * 虛擬函式是一種成員函式，它在基底類別中使用關鍵字"virtual"宣告（定義），
//   並在衍生類別中重新定義虛擬函式，這將成員函式的操作決議 （Resolution）推遲至執行時期再決定。
// 
// * 虛擬函式可以實現執行時期的「多型」，也就是「一個介面，多種函式」，
//   一個含有虛擬函式的類別被稱為「多型的類別」（Polymorphic class），
//   當一個基底類別型態的指標指向一個含有虛擬函式的衍生類別，
//   您就可以使用這個指標來存取衍生類別中的虛擬函式，下面這個例子是個簡單的示範
# include <iostream>

class Foo1{
    public:
        virtual void show(){ //  虛擬函式
            std::cout << "Foo1's show" << std::endl;
        }
};

class Foo2 : public Foo1{
    public:
        virtual void show(){
            std::cout << "Foo2's show" << std::endl;
        }
};

void showFooByPtr(Foo1 *foo) {
    foo -> show();
}

void showFooByRef(Foo1 &foo){
    foo.show();
}

int main(){
    Foo1 f1;
    Foo2 f2;

    // 動態繫結
    showFooByRef(f1);
    showFooByRef(f2);
    std::cout << std::endl;
    
    // 動態繫結
    showFooByRef(f1);
    showFooByRef(f2);
    std::cout << std::endl;

    // 靜態繫結
    f1.show();
    f2.show();

    return 0;
}

// showFooByPtr()與showFooByRef()函式並無法事先知道要操作的是哪一個物件的哪一個公開介面，
// 最後的操作要在執行時期才能決定。
// 衍生類別中重新定義虛擬函式時，virtual可以根據需求加上，
// 如果再接下來的衍生類別仍想進行多型操作，
// 則加上virtual，如果不打算進行多型操作，則可以不加上。

