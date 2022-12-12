# include <iostream>
# include "9_hw_1.h"

int main(){

    eCash p1;


    char in;
    int str;

    while(true){
        std::cout << std::endl;
        std::cout << "Please choose a service: " << std::endl;
        std::cout << "s : saving money." << std::endl;
        std::cout << "p : purchase." << std::endl;
        std::cout << "d : query." << std::endl;
        std::cout << "q : exit this program." << std::endl;


        std::cin >> in;

        if(in == 's'){
            std::cout << "Please enter the dollar:" << std::endl;
            std::cin >> str;
            p1.store(str); 
            continue;
        }else if(in == 'p'){
            std::cout << "Please enter the dollar:" << std::endl;
            std::cin >> str;
            p1.pay(str);
            continue;
        }else if(in == 'd'){
            p1.display();
            continue;
        }else if(in == 'q'){
            std::cout << "End the program." << std::endl;
            break;
        }else{
            std::cout << "Try again!" << std::endl;
            continue;
        }
    }

    return 0;
}