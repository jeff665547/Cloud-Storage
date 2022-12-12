# include <iostream>
# include <string>

struct Sales_data{
    
    // Sales_data() = default;   

    // Sales_data(const std::string &s) : bookNo(s) { }

    // Sales_data(const std::string &s, unsigned n, double p) : bookNo(s), units_sold(n), revenue(p*n) { }

    // Sales_data(std::istream &);
    std::string isbn(double) const { return this->bookNo; }
    Sales_data& combine(const Sales_data&);
    double avg_price() const;

    std::string bookNo;
    unsigned units_sold;
    double revenue;
};

double Sales_data::avg_price() const {
    if (this->units_sold){
        return this->revenue/this->units_sold;
    }
}

Sales_data& Sales_data::combine(const Sales_data &rhs){
    this->units_sold += rhs.units_sold;  
    this->revenue += rhs.revenue;        
    return *this;
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

Sales_data add(const Sales_data &lhs, const Sales_data &rhs){
    Sales_data sum = lhs;   
    sum.combine(rhs);       
    return sum;             
}

// Sales_data::Sales_data(std::istream &is){
    // read(is, *this);
// }

class Screen {
public:
    // bkground refers to the static member
    // declared later in the class definition
    void clear(void){ std::cout << bkground + 1.0 << std::endl; };
    int tempp(){ return bkground/2; }
private:
    double bkground;
};

int main(){

    Sales_data total; 

    int price;
    /*
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
    */

    std::cout << "==============================================" << std::endl;
    // Sales_data test(std::cin);
    Sales_data test;
    std::cout << test.revenue << std::endl;

    return 0;
}