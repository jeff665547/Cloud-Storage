// Access Control and Encapsulation
// Use access specifiers to enforce encapsulation.
// * Members defined after a public specifier are accessible to all parts of the program. 
//   The public members define the interface to the class.
// * Members defined after a private specifier are accessible to the member functions of the class, but are
//   not accessible to code that uses the class. The private sections encapsulate (i.e. hide) the implementation.
// * Benefits of the encapsulation (using private):
//   1. User code cannot inadvertently corrupt the state of an encapsulated object. (The debug area for the class auther is limited.)
//   2. The implementation of an encapsulated class can change over time without requiring changes in user-level code. 
//      (when the implementatioin of the class chages, only the class code (implementation) needs to be examined to face changes.)
 
# include <iostream>
// Declaration for the friend function in the Sales_data class.
Sales_data add(const Sales_data&, const Sales_data&);
std::istream &read(std::istream&, Sales_data&);
std::ostream &print(std::ostream&, const Sales_data&);

class Sales_data {
    // * A class can allow another class or function to access its nonpublic members by making that class or function a friend.
    // * friend declarations for nonmember Sales_data operations added.
    // * friend declarations may appear only inside a class difinition; they may appear anywhere in the class.
    // * frineds are not members of the class and are not affected by the access control of the section where they are declared.
    // * A friend declararion only specifies access. It's not a general declaration of the function.
    friend Sales_data add(const Sales_data&, const Sales_data&);
    friend std::istream &read(std::istream&, Sales_data&);
    friend std::ostream &print(std::ostream&, const Sales_data&);

  public: // access specifier added  // part of the interface.
    Sales_data() = default;
    Sales_data(const std::string &s, unsigned n, double p) : bookNo(s), units_sold(n), revenue(p*n) { }
    Sales_data(const std::string &s): bookNo(s) { }
    Sales_data(std::istream&);
    std::string isbn() const { return bookNo; }
    Sales_data &combine(const Sales_data&);
  private: // access specifier added  // part of the implementation.
    double avg_price() const { return units_sold ? revenue/units_sold : 0; }
    std::string bookNo = "default";
    unsigned units_sold = 0;
    double revenue = 0.0;
};

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


int main(){

    // 
    std::cout << "" << std::endl;

    return 0;
}