# include <iostream>

int main(){

    // 1. const 修飾普通變數
    // 含義一樣，即value只不可變
    const int AA = 5;
    int const BB = 6;

    // AA = 7;
    // BB = 8;

    // 2. const 修飾指標
    int CC = 10;
    const int DD = 11;
    int *HH = &CC;
    
    const int * pContent = &CC;    // pointer to const int, equivalent to const (int) *pContent;  (A)
    int * const pContent;          // const pointer to int, equivalent to (int*) const pContent;   (B)
    int const * pContent;          // pointer to const int, equivalent to (int) const *PContent;  (C) A, C 等價
    const int* const pContent;     // const pointer to const int.

    // 3. const 修飾函數參數
    void function(const int Var);    // Var is a const int in the function.
    void function(const char* Var);  // Var is a pointer to const char in the function.
    void function(char* const Var);  // Var is a const pointer to char in the function.

    // 參數為引用，為了增加效率同時防止修改。
    void function(const Class& Var);  // Var is a reference to const Class in the function.
    void function(const Type& Var);   // Var is a reference to const Type in the function.

    // 4. const 修飾函數返回值
    // const修飾函數返回值其實用的並不是很多，它的含義和const修飾普通變數以及指標的含義基本相同。
    // 說明函數的返回值是不能被修改的。
    const int fun1(); // 這個其實無意義，因為參數返回本身就是賦值。 (return a const int.)
    int back = fun1();
    const int const_back = fun1();

    const int *fun2(); // return a pointer to const int.
    const int *ptrValue = fun2(); // return a pointer to const int.

    int* const fun3(); // return a const pointer to int.
    int* const ptrValue = fun3(); // return a const pointer to int.



        




    return 0;
}