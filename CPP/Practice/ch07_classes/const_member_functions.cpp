#include <iostream>
// A constant (const) member function can be declared by using const keyword, 
// it is used when we want a function that should not be used to change the value of the data members 
// i.e. any type of modification is not allowed with the constant member function.

// Here, we have a class named "Numbers" with two private data members a and b and 
// 4 member functions two are used as setter functions to set the value of a and b 
// and 2 are constant members functions which are using as getter functions to get 
// the value of a and b.
// The object called by these constant functions cannot be modified.

// A const member function that returns *this as a reference should have a return type that is a reference to const.

class Numbers
{
    private:
        int a;
        int b;
    public:
        Numbers() {a = 0; b = 0;}
        
        //setter functions to set a and b
        void set_a(int num1)
        {
            a = num1;
        }
        void set_b(int num2)
        {
            b = num2;
        }
        
        //getter functions to get value of a and b
        int get_a(void) const
        {
            return a;
        }
        int get_b(void) const
        {
            // b = 33; This will cause a compile error, every objects call by this function are read-only.
            return b;
        }
};

//Main function
int main()
{
    //declaring object to the class
    Numbers Num;
    //set values
    Num.set_a(100);
    Num.set_b(100);
    
    //printing values
    std::cout << "Value of a: " << Num.get_a() << std::endl;
    std::cout << "Value of b: " << Num.get_b() << std::endl;
    
    return 0;
}

