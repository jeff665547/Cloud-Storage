// Access Function: It can read or display data, 
// a commin use is to test the truth or falsity of conditions.
// Utility function: it is a private member function that 
// supports the operation of the class's public member functions.
// It's also called helper function. Utility functions are not intended 
// to be used by clients of a class (but can be used by friends of a class.)

// Example below declares an array of 12 monthly sales figures and the prototypes 
// for the class's constructor and member fuctons that manuplate the array.
# include <iostream>
# include <iomanip>

class SalesPerson{
    public:
        static const int monthsPerYear = 12; // months in one year
        SalesPerson(); // constructor
        void getSalesFromUser(); // input sales from keyboard
        void setSales(int, double); // set sales for a specific month
        void printAnnualSales(); // summarize and print sales

    private:
        double totalAnnualSales(); // prototype for utility function
        double sales[ monthsPerYear ]; // 12 monthly sales figures

};

// initialize elements of array sales to 0.0
SalesPerson::SalesPerson(){
    for(int i = 0; i < monthsPerYear; i++){
        sales[ i ] = 0.0;
    }
}

// gets 12 sales figures from the user at the keyboard
void SalesPerson::getSalesFromUser(){
    double salesFigure;

    for(int i = 1; i <= monthsPerYear; i++){
        std::cout << "Enter sales amount for month " << i << ": ";
        std::cin >> salesFigure;
        setSales( i, salesFigure);
    }
}

// set one of the 12 monthly sales figures; function substracts
// one from month value for proper subscript in sales array.
void SalesPerson::setSales( int month, double amount){
    // test for valid month and amount values
    if( month >= 1 && month <= monthsPerYear && amount > 0 ){
        sales[ month - 1 ] = amount; // adjust for subscripts 0-11
    }else{
        std::cout << "Invalid month or sales figure" << std::endl;
    }
}

// print total annual sales (with the help of the utility function)
void SalesPerson::printAnnualSales(){
    std::cout << std::setprecision( 2 ) << std::fixed
    << "\nThe total annual sales are: $" << totalAnnualSales() << std::endl;
    // totalAnnualSales() (utility function) supports the operation of the class's public member functions printAnnualSales().
}

// private utility function to total annual sales
double SalesPerson::totalAnnualSales(){
    double total  = 0.0; // initialize total

    for(int i = 0; i < monthsPerYear; i++){ // summarize sales results
        total += sales[i];  // add month i sales to total 
    }

    return total;
}

int main(){
    SalesPerson s; // create SalesPerson object s

    s.getSalesFromUser(); // note simple sequential code; there are
    s.printAnnualSales(); // no control statements in main
}