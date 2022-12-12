#include <iostream>
#include <string>
#include <cstdio> // fflush()
#include <vector>
#include <cstdlib>

class Data{
    public:
        std::string scientific_name;
        int number;
};

class Animal{
    public:
        Animal();
        void add(Data x);
        void update(Data x);
        void display();

    private:
        Data Animal_list[500]; 
        int type;
        int Endanger_number;
        int index;
};

Animal::Animal(){
    type = 0;
    for (size_t i = 0; i < 500; i++){
        Animal_list[i].number = 0;
        Animal_list[i].scientific_name = " ";
    }
}

void Animal::add(Data x){
    Animal_list[type] = x;
    type += 1;
    std::cout << "Add. Animal: " << x.scientific_name 
              << ".\nNumber: " << x.number << "\nEndanger species: ";
    if(x.number < 1000){
        std::cout << "Yes";
    }else{
        std::cout << "No";
    }
    std::cout << "\n";
}

void Animal::update(Data x){
    for (size_t i = 0; i < type; i++){
        if(Animal_list[i].scientific_name == x.scientific_name){
            Animal_list[i].number = x.number;
            std::cout << "Update. Animal: " << x.scientific_name 
              << ".\nNumber: " << x.number << "\nEndanger species: ";
            if(x.number < 1000){
                std::cout << "Yes";
            }else{
                std::cout << "No";
            }
            std::cout << "\n";
        }
    }
}

void Animal::display(){
    int ct = 0;
    for (size_t i = 0; i < type; i++){
        if(Animal_list[i].number < 1000){
            ct += 1;
        }
    }
    
    std::cout << "There are " << ct << " animals who are endanger species\n"; 
    
    for (size_t i = 0; i < type; i++){
        if(Animal_list[i].number < 1000){
            std::cout << "Animal: "<< Animal_list[i].scientific_name <<
            ".\nNumber: "<< Animal_list[i].number << std::endl;
        }
    }
}

class input{
    public:
        std::string op_animal_name;
        int op_num;
};

int main(){
    Animal all_animal;

    std::vector<std::string> container;

    while(true){
        std::string input;
        fflush(stdin);
        getline(std::cin, input);

        if(input[0] == 'q'){
            container.push_back(input);
            break;
        }else{
            container.push_back(input);
        }
    }

    for (size_t i = 0; i < container.size(); i++)
    {
        if(container[i] == "d"){
            all_animal.display();
        }else if(container[i] == "q"){
            std::cout << "That are the endanger animal list we have now. Bye bye." << std::endl;
        }else{
            std::string input_name;
            input_name = input_name.assign(container[i], 2, container[i].length() - 2);
            int input_number = atoi(container[i + 1].c_str());
            Data tmp;
            tmp.number = input_number;
            tmp.scientific_name = input_name;

            if(container[i][0] == 'a'){
                all_animal.add(tmp);
            }else if(container[i][0] == 'u'){
                all_animal.update(tmp);
            }
            i += 1;
        }
    }

    return 0;
}