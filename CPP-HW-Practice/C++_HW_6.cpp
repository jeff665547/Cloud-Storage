#include <string>
#include <iostream>
#include <algorithm>  // std::sort()
#include <vector>

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
class comp;

class Engine{
    public:
        Engine();  // default constructor
        Engine(int cc, int weight, std::string type); // non-default constructor.
        Engine(const Engine &item); // copying constructor.
        Engine(Engine &&item); // moving constructor.
        Engine& operator=(const Engine &item); // copying and assignment operator.
        Engine& operator=(Engine &&item); // moving and assignment operator.
        friend void check_engine(Car &car);  // for void check_engine(Car &car) function.
        friend class Car; // for member function in class Car (void check_my_engine(void)).
        friend bool operator<(Car &car1, Car &car2);
        // friend std::ostream;
        friend std::ostream& operator<<(std::ostream &__out, Car car);
        friend class comp;

    private:
        int Cc;
        int Weight;
        std::string Type;

};

Engine::Engine(){
    Cc = 0;
    Weight = 0;
    Type = "None";
}

Engine::Engine(int cc, int weight, std::string type){
    Cc = cc;
    Weight = weight;
    Type = type;

}

Engine::Engine(const Engine &item){
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;

}

Engine::Engine(Engine &&item){
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;

}

Engine& Engine::operator=(const Engine &item){
    if(this == &item){
        return *this;
    }
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;

    return *this;
}

Engine& Engine::operator=(Engine &&item){
    if(this == &item){
        return *this;
    }
    Cc = item.Cc;
    Weight = item.Weight;
    Type = item.Type;

    return *this;
}

class Car{
    public:
        Car();
        void check_my_engine(void);
        void set_my_engine(int cc, int weight, std::string name);
        friend void check_engine(Car &car);
        friend bool operator<(Car &car1, Car &car2);
        // friend std::ostream;
        friend std::ostream& operator<<(std::ostream &__out, Car car);
        friend class comp;

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

void Car::set_my_engine(int cc, int weight, std::string name){

    my_engine.Cc = cc;
    my_engine.Weight = weight;
    my_engine.Type = name;

}

// friend operator 的實作和 overloaded operator 的實作是不同的(operator前方不用加上type name)
// friend operator 和其他friend系統的用法相同(要先去會使用到的class中宣告，
// 如在Engine class中先宣告下方的friend operator)
bool operator<(Car &car1, Car &car2){

    if(car1.my_engine.Cc < car2.my_engine.Cc){
        return true;
    }else{
        return false;
    }
}

std::ostream& operator<<(std::ostream &__out, Car car){
    
    __out << "The cc of the Car is " << car.my_engine.Cc << "." << std::endl;
    __out << "The Weight of the Car is " << car.my_engine.Weight << "." << std::endl;

    return __out;
}

void check_engine(Car &car){

    std::cout << "CC is " << car.my_engine.Cc << std::endl;
    std::cout << "Weight is " << car.my_engine.Weight << std::endl;
    std::cout << "Type is " << car.my_engine.Type << std::endl;

};

// struct default is public, but class default is private.
class comp{
    public:
        bool operator() (Car car1, Car car2){
            return(car1.my_engine.Cc < car2.my_engine.Cc);
        }
};

int main() {

    std::vector <Car> car_list;

    for (int i = 0; i < 5; i++){
        std::cout << i << std::endl;
        Car tmp;
        car_list.push_back(tmp);
        car_list[i].set_my_engine(5-i, 10*(5-i), "ABC");
    }
    
    std::cout << "========================================" << std::endl;

    for (int i = 0; i < 5; i++){
        std::cout << car_list[i] << '\n';
    }

    comp test;
    std::sort(car_list.begin(), car_list.end(), test);

    std::cout << "========================================" << std::endl;

    for (int i = 0; i < 5; i++){
        std::cout << car_list[i] << '\n';
    }

    return 0;
}