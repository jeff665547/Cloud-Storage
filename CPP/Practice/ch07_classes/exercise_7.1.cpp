// 0-201-78345-X 3 20.00
// 0-201-78345-X 2 25.00

# include <iostream>
# include <string>

struct Sales_data{
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
};

int main(){
    Sales_data total;
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

    return 0;
}