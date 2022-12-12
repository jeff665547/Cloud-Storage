// 1. Relationships between reference and pointer.
// 2. Implicit/Explicit Class-Type Conversions
// 3. Aggregrate Classes
// 4. constexpr and Constant Expressions
// 5. Literal Classes and constexpr Constructors
// 
// Input:
// 0-201-78345-X 3 20.00
// 0-201-78345-X 2 25.00

# include <iostream>
# include <string>

// * Member functions may be defined inside the class itself or outside the class body. 
// * Nonmember functions that are part of the interface, such as add, read, and print, are declared
//   and defined outside the class.
// * The only difference between class keyword ans struct keyword is the default access level (存取權限).
// * The default access level of the member in the "class" is private, 
//   and the default access level of the member in the "struct" is public.

struct Sales_data{
    // * if our class does not explicitly define any constructor, the compiler will implicitly define the default constructor for us.
    
    Sales_data() = default;   
    
    Sales_data(const std::string &s) : bookNo(s) { }
    
    // * The explicit keyword is meaningful only on constructors that can be called with a single argument.
    //   Constructor that require more arguments are not used to perform an impicit conversion, so there is no need
    //   to designate such constructors as explicit.
    // * The explicit keyword is used only on the constructor declaration inside the class.
    // * It is not repeated on a definition made outside the class body.
    explicit Sales_data(const std::string &s, unsigned n, double p) : bookNo(s), units_sold(n), revenue(p*n) { }
    
    explicit Sales_data(std::istream &);
    

    // Delegating Constructors Version
    // * nondelegating constructor initializes members from corresponding arguments
    // Sales_data(std::string s, unsigned cnt, double price):
    //            bookNo(s), units_sold(cnt), revenue(cnt*price) { }  // the three-argument constructor.
    // * remaining constructors all delegate to another constructor
    // Sales_data(): Sales_data("", 0, 0){ }  // delegates to the three-argument constructor.
    // Sales_data(std::string s): Sales_data(s, 0, 0) { }  // delegates to the three-argument version constructor.
    // Sales_data(std::istream &is): Sales_data() { read(is, *this); }  // delegates to the default constructor.

    // ================================================================================================
    // new members: operation on Sales_data objects
    std::string isbn() const { return this->bookNo; }  // this is a constant pointer.
    Sales_data& combine(const Sales_data&);
    double avg_price() const;

    // data members are unchanged from p72
    // These are in-class initializers.
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
};

// Defining a member function outside the class
double Sales_data::avg_price() const { // :: is the scope operator.
    if (this->units_sold){
        return this->revenue/this->units_sold;
    }
}

// Defining a function to return "this" object
Sales_data& Sales_data::combine(const Sales_data &rhs){
    this->units_sold += rhs.units_sold;  // add the members of rhs into
    this->revenue += rhs.revenue;        // the members of "this" object.
    return *this;   // return the object on which the function was called.  // "this" is a pointer to the address of the object on which the function was invoked.
                    // this 是一個指向類別物件(實體)位址的指標，*this 代表此處回傳的是該類別物件的實體。
}

std::istream &read(std::istream &is, Sales_data &item){
    double price = 0;
    is >> item.bookNo >> item.units_sold >> price;
    item.revenue = price * item.units_sold;
    return is;
}
std::ostream &print(std::ostream &os, const Sales_data &item){
    os << item.isbn() << " " << item.units_sold << " "
       << item.revenue << " " << item.avg_price();
    return os;
}

// Define the add Function
Sales_data add(const Sales_data &lhs, const Sales_data &rhs){
    Sales_data sum = lhs;   // initialize sum as a copy. copy data members from lhs into sum.
    sum.combine(rhs);       // add data members from rhs into sum.
    return sum;             // return a copy of sum.
}


// Define a Constructor outside the Class Body.
Sales_data::Sales_data(std::istream &is){
    read(is, *this); // read will read a transaction from is into this object.
}

// Aggragrate Classes
// 1. all of the data members are public.
// 2. it does not define any constructors.
// 3. it has no in-class initializers
// 4. it has no base classes or virtual functions, which are class-related features.
struct Data{
    int ival;
    std::string s;
};

int get_size(int aa){
    return aa*aa;
};

// Literal Classes and constexpr Constructors
class Debug{
public:
    constexpr Debug(bool b = true): hw(b), io(b), other(b) { }
    constexpr Debug(bool h, bool i, bool o): hw(h), io(i), other(o) { }
    constexpr bool any() { return hw || io || other; }
    void set_io(bool b) { io = b; }
    void set_hw(bool b) { hw = b; }
    void set_other(bool b){ hw = b; }

private:
    bool hw;     // hardware errors other than IO errors.
    bool io;     // IO errors.
    bool other;  // other errors.
};

int main(){

    // Relationships between reference and pointer.
    int AA = 3;
    int &BB = AA;
    int *CC = &AA;
    std::cout << BB << std::endl;
    std::cout << *CC << std::endl;
    // * BB is equivalent to *CC.
    // * BB in fact is a pointer (stores in somewhere in the memory, and that storage address is different from AA.) 
    //   that always points to its initializd value. (cannot be changed.)
    // * Thus, when we tried to get the address of the reference (i.e. &BB). In fact, we are doing somthing like this &(*CC).
    // * So, the value of &(*CC) is the address of AA. (it is the value in CC.)
    // * From another viewpoint, * operator returns a lvalue. *CC will return the variable AA, so &(*CC) is equivaluent to &AA,
    //   which means the address of the variable AA.

    Sales_data total; 
    // this is the correct way to define an object that uses the default constructor for initialization is to leave off the trailing, 
    // empty parenthess.
    int price;
    if(std::cin >> total.bookNo >> total.units_sold >> price){
        total.revenue = total.units_sold * price;
        Sales_data trans;
        while(std::cin >> trans.bookNo >> trans.units_sold >> price){
            trans.revenue = trans.units_sold * price;
            if(total.bookNo == trans.bookNo){
                total.units_sold += trans.units_sold;
                total.revenue += trans.revenue;
            }else{
                std::cout << total.bookNo << " " << total.units_sold << " " << total.revenue << std::endl;
                total = trans;
            }
        }
        std::cout << total.bookNo << " " << total.units_sold << " " << total.revenue << std::endl;
    }else{
        std::cerr << "No data?!" << std::endl;
        return -1;
    }
    
    // Implicit/Explicit Class-Type Conversions
    // total.combine(std::cin); // error: istream constructor is explicit. 
    // 如果沒有在constructor的地方宣告explicit，則此行可編譯。
    // std::cin會先轉成Sales_data的形式再送到combine function內部。
    Sales_data temp(std::cin);
    total.combine(temp);
    // 若在constructor的地方宣告explicit，則只能使用此種方法進行編譯。

    // Aggregrate Classes
    // Initialize the aggregrate class.
    Data val1 = {0, "Anna"};  // the initializers must appear in declaration order of the data members.
    // val1.ival = 0; val1.s = std::string("Anna");
    // three drawbacks:
    // 1. it requires that all data members of the class be public.
    // 2. it puts the burden on the user of the class to correctly initialize every member of every object. (tedious and error-prone)
    // 3. If a member is added or removed, all initializations have to be updated.

    std::cout << "==============================================" << std::endl;
    Sales_data test(std::cin);
    std::cout << test.revenue << std::endl;

    // constexpr and Constant Expressions
    // * const告訴程式設計師沒人動的了我，放心的把我傳出去吧，或者放心的把變數交給我，我不會去動它。
    // * constexpr告訴編譯器我(some expression)是可以在編譯期間可知的，請盡情的優化我(some expression)吧
    //   (一堆常數可以在編譯時期經過固定確定運算得到確切值的表達式。)
    // * constexpr function 有非常硬的限制。從傳入的參數到中間的運算流程都必須是編譯期確切知道的，不然編譯器根本沒辦幫法幫你算。
    // * 如一開始constexpr function 裡面是不能出現如 if, for 這樣的流程控制的，必須一步到位計算結果，
    //   函式體中間也不得出現 i++ 這類的表達式，也不能宣告變數。
    // * 可以把 constexpr function 整體想成一個包起來的一行的表達式。
    // * constexpr function 可以應用在 enum, switch 上，enum 宣告，switch 邏輯判斷分支都需要吃一堆常數。
    // * constant expression is an expression whose value cannot change and that can be evlauated at compile time.
    // * lieral types: Since a constant expression is one that can be evaluated at compile time, there are limits on
    //   the types that we can use in a constexpr declaration. The types we can use in a constexpr are known as "literal types"
    //   because they are simple enough to have literal values.
    const int max_files = 20;         // max_files is a constant expression
    const int limit = max_files + 1;  // limit is a constant expression
    int staff_size = 27;              // staff_size is not a constant expression
    const int sz = get_size(3);       // sz is not a constant expression if the value of its initializer is not known until run time.
    // Literal Classes and constexpr Constructors
    // * In addition to the arithmetic types, references, and pointers, certain classed are also literal types.
    // * Unlike other classes, classes that are literal types may have function members that are constexpr. Such members must meet
    //   all the requirements of a constexpr function. These member functions are implicitly const (指 const member function). 
    // * An aggregrate class whose data members are all of literal type is a literal class.
    // * A nonaggregrate class, that meets the following restrictions, is also a literal class:
    //   1. the data members all must have literal type.
    //   2. the class must have at least one constexpr constructor.
    //   3. If a dara member has an in-class initializer, the initializer for a member of built-in type must be a constant expression,
    //      or if the member has class type, the initializer must use the member's own constexpr constructor.
    //   4. The class must use default definition for its destructor, which is the member that destroys objects of the class type.
    constexpr Debug io_sub(false, true, false);  // debugging IO
    if (io_sub.any()){ // equivalent to if(true)
        std::cerr  << "print appropriate error messages" << std::endl;
    }
    constexpr Debug prod(false);  // no debugging during production.
    if (prod.any()){ // equivalent to if(false)
        std::cerr << "print an error message" << std::endl;
    }

    return 0;
}