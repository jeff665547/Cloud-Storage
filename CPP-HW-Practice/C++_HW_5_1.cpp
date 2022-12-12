#include <string>
#include <iostream>

// Write a class named Engine.
// copy constructor using time:
// 1. 物件作為函式引數
// 2. 物件作為函式返回值
// 3. 用一個物件初始化另一個物件

// copy assignment operator
// T t1;
// T t2;
// t1 = t2; "=" is not assignment here

// move constructor using time:
// 1. 用右值初始化物件。
// 2. std::move(物件)只將物件轉為右值，讓物件成為被搬移的候選人

// move assignemt operator
// T t1;
// t1 = std::move(T());

class Engine{
    public:
        Engine();  // default constructor
        Engine(int cc, int weight, std::string type); // non-default constructor.
        Engine(const Engine &item); // copying constructor.
        Engine(Engine &&item); // moving constructor.
        Engine& operator=(const Engine &item); // copying and assignment operator.
        Engine& operator=(Engine &&item); // moving and assignment operator.

    private:
        int Cc;
        int Weight;
        std::string Type;

};

Engine::Engine(){
    Cc = 0;
    Weight = 0;
    Type = "None";
    std::cout << "Invoke default constructor." << std::endl;
}

Engine::Engine(int cc, int weight, std::string type){
    Cc = cc;
    Weight = weight;
    Type = type;
    std::cout << "Invoke non-default constructor." << std::endl;

}

Engine::Engine(const Engine &item){
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;
    std::cout << "Invoke copying constructor." << std::endl;

}

Engine::Engine(Engine &&item){
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;
    std::cout << "Invoke moving constructor." << std::endl;

}

Engine& Engine::operator=(const Engine &item){
    if(this == &item){
        return *this;
    }
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;
    std::cout << "Invoke copying and assigning operator." << std::endl;

    return *this;
}

Engine& Engine::operator=(Engine &&item){
    if(this == &item){
        return *this;
    }
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;
    std::cout << "Invoke moving and assigning operator." << std::endl;

    return *this;
}

int main() {

    std::cout << "============section start============" << std::endl;
    Engine e0; // Default constructor;
    std::cout << "============section 1============" << std::endl;
    Engine e1 = e0; // Copying constructor;
    std::cout << "============section 2============" << std::endl;
    Engine e2 = std::move(e0);  // Moving constructor;
    std::cout << "============section 3============" << std::endl;
    Engine e3;
    e3 = e0; // Coping and assigning operator;
    std::cout << "============section 4============" << std::endl;
    Engine e4;
    e4 = std::move(Engine()); // Moving and assignment operator, default constructor;
    std::cout << "============section 5============" << std::endl;
    Engine e5;
    e5 = std::move(Engine(2300, 3400, "Altis")); // Moving and assignment operator, non-default constructor.
    std::cout << "============section end==========" << std::endl;


    return 0;
}