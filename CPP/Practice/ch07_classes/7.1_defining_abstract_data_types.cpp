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
    // * defines the default constructor since it takes no arguments.
    // * An empty parameter list (i.e., the default constructor) 
    //   which as we've just seen we must define because we have defined other constructors below.
    // * This is the synthesized default constructor. (Using in-class initialization below (under "===="))
    // * In practice, it is almost always right to provide a default constructor is other constructors are being defined.

    Sales_data(const std::string &s) : bookNo(s) { }
    // * A const strings& representing an ISBN. This constructor will use default values for the other members.
    // * Constructor initializer list: bookNo, its initial value: s (inside the curly braces or parentheses). 
    // * This constructor does not initialize the units_sold and revenue members. When a member is omitted from the 
    //   constructor initializer list, it is implicitly initialized using the same process as is used by the synthesized default constructor.
    // * In this case, this is equivalent to "Sales_data(const std::string &s): bookNo(s), units_sold(0), revenue(0){ }".
    // * If there is no further work (except initialization), then the function body is empty ({ }).
    // * The default constructor above can be rewritten into Sales_data(std::string s = "") : bookNo(s) { } 
    //   => this written style uses default argument.

    Sales_data(const std::string &s, unsigned n, double p) : bookNo(s), units_sold(n), revenue(p*n) { }
    // * A const string& representing an ISBN, an unsigned representing the count of how many books were sold, 
    //   and a double representing the price at which the books sold.
    // * Constructor initializer list: bookNo, its initial value: s; units_sold, its initial value: n; revenue, its initial value: p*n.
    // * Elements in the constructor initializer list are separated by a comma ",".
    // * It's a good idea to write constructor initializers in the same order as the members are declared. If possible, avoid using members
    //   to initialize other members. (such as revenue(p*units_sold))

    Sales_data(std::istream &);
    // * An istream& from which to read a transaction.
    // * Unlike other constructors, it does have work to do.


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
    std::string bookNo;
    unsigned units_sold;
    double revenue;
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

// Defining the read and print Functions (the IO classes are types that cannot be copied, 
// so we may only pass them by reference. Moreover, reading or writing to a stream changes that stream, so both functions
// take ordinary references, not references to const.)
// input transactions contain ISBN, number of copies sold, and sales price
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


int main(){

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

    std::cout << "==============================================" << std::endl;
    Sales_data test(std::cin);
    std::cout << test.revenue << std::endl;

    return 0;
}