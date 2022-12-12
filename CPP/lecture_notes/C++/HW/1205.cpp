# include <iostream>
# include <string>
# include <vector>
# include <cstdlib>
# include <cstdio>

class Data{
    public:
        Data();
        std::string name;
        int price;
        int number;
};

Data::Data(){
    name = "";
    price = 0;
    number = 0;
}

class product{
    public:
        product();
        void add(Data x);
        void update(Data x);
        void sell(Data x);
        void display();
        void quit();

    private:
        Data product_list[500];
        int product_index;
        int profit;
};

product::product(){
    product_index = 0;
    profit = 0;
    for(size_t i = 0; i < 500; i++){
        product_list[i].name = "";
        product_list[i].number = 0;
        product_list[i].price = 0;
    }
}

void product::add(Data x){

    product_list[product_index] = x;
    product_index += 1;
    
    std::cout << "Added. Product: " << x.name << "." << std::endl;
    std::cout << "Sell price: " << x.price << std::endl;
}

void product::update(Data x){

    for (size_t i = 0; i < 500; i++){
        if(product_list[i].name == x.name){
            product_list[i].price = x.price;
        }
    }
    std::cout << "Updated. Product: " << x.name << "." << std::endl;
    std::cout << "Sell Price: " << x.price << std::endl;
}

void product::display(){
    int sum_num = 0;
    for (size_t i = 0; i < product_index; i++){
        std::cout << "Product: " << product_list[i].name << "." << std::endl;
        std::cout << "Total number of sold: " << product_list[i].number << std::endl;
        sum_num += product_list[i].number;
    }
    std::cout << "Total product sold: " << sum_num << std::endl;
    std::cout << "Profit: " << profit << std::endl;
}

void product::sell(Data x){

    for (size_t i = 0; i < 500; i++){
        if(product_list[i].name == x.name){
            profit += product_list[i].price*(x.number - product_list[i].number);
            product_list[i].number += x.number;
            std::cout << "Sold. Product: " << x.name << "." << std::endl;
            std::cout << "Number of sold: " << x.number << std::endl;
        }
    }
}

void product::quit(){
    std::cout << "Thanks for visiting Old Farmer Market. Wish you have a good day. Bye bye." << std::endl;
}

int main(){

    std::vector<std::string> container;
    std::string input;

    while(true){

        fflush(stdin);
        getline(std::cin, input);

        if(input == "q"){
            container.push_back(input);
            break;
        }else{
            container.push_back(input);
        }
    }

    product all;
    std::cout << "Welcome to Old Farmer Market, what can I help you?" << std::endl;
    
    std::string input_name;
    int input_price;
    int input_number;

    for(size_t i = 0; i < container.size(); i++){

        if(container[i][0] == 'a'){
            input_name = input_name.assign(container[i], 2, container[i].size() - 2);
            input_price = atoi(container[i+1].c_str());
            Data tmp;
            tmp.name = input_name;
            tmp.price = input_price;
            all.add(tmp);
            i += 1;
        }else if(container[i][0] == 'u'){
            input_name = input_name.assign(container[i], 2, container[i].size() - 2);
            input_price = atoi(container[i+1].c_str());
            Data tmp;
            tmp.name = input_name;
            tmp.price = input_price; 
            all.update(tmp);
            i += 1;
        }else if(container[i][0] == 's'){
            input_name = input_name.assign(container[i], 2, container[i].size() - 2);
            input_number = atoi(container[i+1].c_str());
            Data tmp;
            tmp.name = input_name;
            tmp.number = input_number;
            all.sell(tmp);
            i += 1;
        }else if(container[i][0] == 'd'){
            all.display();
        }else if(container[i][0] == 'q'){
            all.quit();
        }
    }

    return 0;
}