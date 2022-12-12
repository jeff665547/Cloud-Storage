/* 多重繼承(advc)) */
// 多重繼承時通常其中一個基底類別作為private實作體，而其它的用以表現完全的抽象介面。
//
// 介面: 指API，為了容納各種不同情況的input，所設立的虛擬類別。
// 虛擬類別: 為了把大家共同的部份給抽取出來所設立的虛擬類別，是給程式開發者使用的。
// 
// 考慮您有一個方法doRequest()，您事先並無法知道什麼型態的物件會被傳進來，
// 或者是這個方法可以接受任何類型的物件，您想要操作物件上的某個特定方法，
// 例如doSomething()方法，問題是傳進來的物件是任意的，
// 除非您定義一個抽象類別並宣告doSomething()抽象方法，
// 然後讓所有的類別都繼承這個抽象類別，
// 否則的話您的doRequest()方法似乎無法實作出來，實際上這麼做也沒有價值。
// 您可以藉由多重繼承來解決這個問題，例如先定義一個抽象類別:
#include <iostream>
#include "IRequest.h"
#include "Welcome.h"
#include "Hello.h"
using namespace std;

void doRequest(IRequest *request){
    request -> execute();
}

int main(){
    Welcome welcome;
    Hello hello;

    IRequest *tt;

    tt = &welcome;
    doRequest(tt);

    tt = &hello;
    doRequest(tt);

    return 0;
}

// 假設您設計了一個doRequest()方法，雖然不知道Hello與Welcome是什麼型態，
// 但它們都繼承了IRequest，所以doRequest()只要知道IRequest定義了什麼公開(public)介面，
// 就可以操作Hello與Welcome的實例，而不用知道傳入的物件到底是什麼類別的實例。

/* 虛擬繼承 (Virtual Inheritance) */
// 多重繼承時，會有一種模擬兩可的情況，就是當兩個類別都繼承同一個基底類別，
// 而這兩個類別又同時被另一個類別，以平行多重繼承的方式同時繼承，
// 在上述中，C類別將會擁有兩個A類別的複本，一個來自B1所繼承下來的，
// 一個來自B2所繼承下來的，那麼C類別到底要用B1所繼承下來的？還是B2所繼承下來的？
// 您可以使用「虛擬繼承」(Virtual Inheritance)來解決這個問題。
// 虛擬繼承是在繼承基底類別時使用"virtual"關鍵字
// 
// e.g.
// class A { 
//     // 實作 
// }; 

// class B1 : virtual public A {  // 虛擬繼承 
//     // 實作 
// }; 

// class B2 : virtual public A {  // 虛擬繼承 
//     // 實作 
// }; 

// class C : public B1, public B2 { 
//     // 實作 
// };
// 
// 在上例中，B1與B2以虛擬繼承的方式繼承了A類別，
// 這個好處是當有類別多重繼承了某個基底類別時，在該類別中將會只有一個基底類別存在，
// 而不會有多個複本，例如在上例中，類別C中將只會有一個基底類別A的存在。