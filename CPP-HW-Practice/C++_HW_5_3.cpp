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

class Car; // 凡是只要在前面寫的class需要用到後面寫的class資訊，就必須要先宣告，
// 如同此例，Engine class 在 friend void function 中的 argument 用到了Car class，
// 因此在此先宣告class Car。

class Engine{
    public:
        Engine();  // default constructor
        Engine(int cc, int weight, std::string type); // non-default constructor.
        Engine(const Engine &item); // copying constructor.
        Engine(Engine &&item); // moving constructor.
        Engine& operator=(const Engine &item); // copying and assignment operator.
        Engine& operator=(Engine &&item); // moving and assignment operator.
        friend void check_engine(Car &car);  // for void check_engine(Car &car) function.
        friend class Car; // for 

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

class Car{
    public:
        Car();
        void check_my_engine(void);
        friend void check_engine(Car &car);

    private:
        Engine my_engine;
};

Car::Car(){
    Engine temp(0, 0, "none");
    my_engine = temp;
};

void Car::check_my_engine(void){

    std::cout << "CC is " << my_engine.Cc << "." << std::endl;
    std::cout << "Weight is " << my_engine.Weight << "." << std::endl;
    std::cout << "Type is " << my_engine.Type << "." << std::endl;

}

void check_engine(Car &car){

    std::cout << "CC is " << car.my_engine.Cc << std::endl;
    std::cout << "Weight is " << car.my_engine.Weight << std::endl;
    std::cout << "Type is " << car.my_engine.Type << std::endl;

};

class Police{
    public:
        static void check_car(Car& temp);
};

void Police::check_car(Car& temp){
    temp.check_my_engine();
};


int main() {

    std::cout << "=======================Chapter 1=======================" << std::endl;
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

    std::cout << "=======================Chapter 2=======================" << std::endl;
    Car Escape;
    check_engine(Escape);
    std::cout << "=======================================================" << std::endl;
    Escape.check_my_engine();
    std::cout << "=======================section end=======================" << std::endl;

    std::cout << "=======================Chapter 3=======================" << std::endl;
    Police::check_car(Escape);
    std::cout << "=======================section end=======================" << std::endl;


    return 0;
}