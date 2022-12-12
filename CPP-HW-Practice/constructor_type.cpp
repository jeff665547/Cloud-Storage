# include <iostream>
// Default Constructor:
// It is a constructor that can be invoked with no arguments.
// There can be at most one default constructor per class.

// Destructor 
// A class's destructor is called implicitly when an object is destoryed.
// A destructor must be public, and cannot be overloaded.
// If we do not explicitly provide a destructor, the compiler creates an "empty" destructor, 
// and that performs an important operation on objects that are through composition and inheritance. 
// It is useful in dynamically allocate and deallocate memory (dynamically allocated memory).

// copy constructor using time:
// 1. 物件作為函式引數
// 2. 物件作為函式返回值
// 3. 用一個物件初始化另一個物件

// move constructor using time:
// 1. 用右值初始化物件。
// 2. std::move(物件)只將物件轉為右值，讓物件成為被搬移的候選人

class A{
    public:
        int a;
        int b;

        // One-argument constructor: (converting constructor)
        A(int i);

        // Destructor
        ~A();

        // Copy constructor
        A(const A &v);

        // Moving Constructor
        A(A &&v);

        // Copy and assignment operator
        A& operator =  (const A &v);

        // Moving and assignment operator
        A& operator = (A &&v);
};

class test{
    public: 
        int num;
};

A::A(int i): a(i){
    printf("construct is called! %d \n",i); 
}

A::~A(){
    printf("destructer is called! \n");
}

// Copying constructor
A::A(const A &v){
    this -> a = v.a;  // 這裡使用this的寫法怕搞混a
    printf("copy construct is called %d\n", a);
}

// Moving Constructor
A::A(A &&v){
    this -> a = v.a;
    printf("move construct is called %d\n", a);
}

// Copy and assignment operator
A& A::operator = (const A &v){
    printf("copy = is called \n");
    if(this == &v){   // this 指的是當前A類物件的指標
        return *this;   
    }
    a = v.a;
    return *this;  // 凡事只要return給自己身上的寫法都是這樣，然後一開始的回傳類別是type &，有加reference (&)
}

// Moving and assignment operator
A& A::operator = (A &&v){
    printf("move = is called \n");
    if (this == &v){
        return *this;
    }
    a = v.a;
    return *this;
}

//  上述的reference相當於
//  int abc = 33; // 在上述function裡面的this 相當於此處的abc;
//  int &CC = abc; // CC為外部的reference
//  只不過在copy assignment中abc和CC都是同一件事，同一個物件(同一個記憶體位置)

int test2(int a, int b){
    return a + b; 
    // copy the return value and assign to the object, 
    // not the concept of the reference.
}

int main ()
{
    std::cout << "========section 1=========" << std::endl;
    A a(1);    // 呼叫 Default Constructor
    std::cout << "========section 2=========" << std::endl;
    A b(a);    // 呼叫 Copying Constructor
    std::cout << "========section 3=========" << std::endl;
    A c = a;   // 呼叫 Copying Constructor
    std::cout << "========section 4=========" << std::endl;
    A tt(std::move(A(100)));  // 呼叫 Moving Constructor
    std::cout << "========section 5=========" << std::endl;

    A d(2);    // 呼叫 Default Constructor
    std::cout << d.a << std::endl;
    std::cout << "========section 6=========" << std::endl;

    d = a;     //呼叫 Copying and assignment operator
    std::cout << d.a << std::endl;

    std::cout << "========section 7=========" << std::endl;
    
    A e = std::move(A(3));   // 呼叫 Moving constructor
    std::cout << "========section 8=========" << std::endl;

    A g(9);   // 呼叫 Default Constructor
    std::cout << "========section 9=========" << std::endl;
    
    g = std::move(A(8)); // 呼叫 Moving and assignment operator
    std::cout << "========section 10========" << std::endl;

    g = A(7); // 呼叫 Moving and assignment operator
    std::cout << g.a << std::endl;
    std::cout << "========section 11========" << std::endl;

    A f(4);  // 呼叫 Default Constructor
    std::cout << "========section 12========" << std::endl;

    f = std::move(A(5));   //呼叫 Moving and assignment operator
    std::cout << "========section 13========" << std::endl;

    test AA;
    AA.num = 5;
    test BB = AA;
    test CC;
    CC = AA;
    std::cout << CC.num << std::endl;
    std::cout << "========section ends======" << std::endl;

    return 0;
}
