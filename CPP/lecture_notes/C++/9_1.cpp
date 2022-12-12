# include <iostream>
# include "9_1_1.h"

int main(){

    Pokemon Pikachu;

    Pikachu.ShowInfo();
    Pikachu.Attack("Lapras");
    Pikachu.Defence("Lapras");
    Pikachu.Cure();

    std::cout << std::endl;

    Pokemon Lapras("Lapras", 382, 76, 76);

    Lapras.ShowInfo();
    Lapras.Attack("Pikachu");
    Lapras.Defence("Pikachu");
    Lapras.Cure();

    return 0;
}