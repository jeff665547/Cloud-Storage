// const member function in C++ program
#include <iostream>
using namespace std;

class Product
{
      int pId;
      float cost;
      public:
        //constructor
        Product(int pId, float cost)
        {
            this->pId = pId;
            this->cost = cost;
        }

      /*---------------------------------------
      *Gettr and setter of class data members
      */
      //set product id
      void setProductId(int pId)
      {
            this->pId = pId;
      } 

      Product& retrunself(){
        std::cout << "in the class" << std::endl;
        std::cout << this << std::endl;
        return *this;
      }

      //This method cannot modify any
      //data member of this class
      //If we try to modify them then compiler
      //will flash an error l-value specifies
      //const object
      int getProductId()const
      {
            //if try to modify any data member
            // e.g. pId here the compiler will
            //flash error e.g.
            //this->pId = 20;//error

            //Also cannot call non static function
            //of this class in here e.g.
            //setProductId(50); error

            return pId;
      }    

      //Print data
      void print()
      {
             cout<<"Product Id : "<<this->pId;
             cout<<" Cost : "<<this->cost<<endl;
      }

};


int main()
{
      int pId = 1234;
      float cost = 100.00;
      Product a(pId, cost);
      Product p(pId,cost); 
      std::cout << "outside the class" << std::endl;
      std::cout << &p << std::endl;
      std::cout << &p.retrunself() << std::endl;
      std::cout << &a << std::endl;
      p.getProductId();
      p.print();           

      return 0;

}