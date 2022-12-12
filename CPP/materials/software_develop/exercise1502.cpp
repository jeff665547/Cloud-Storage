#include <iostream>

int main(){

    std::string input_str;
    int input[4];
    int i;
    int j;
    int ct_A = 0;
    int ct_B = 0;

    std::cout << "Please enter a number with four non-repeated digits: " ;

    std::cin >> input_str;

    for(i = 0; i < input_str.length(); i++){
        input[i] = (int) input_str[i] - 48;
    }

    int ans[4] = {3, 4, 5, 6};
    
    for(i = 0; i < (std::end(ans) - std::begin(ans)); i++){
        for(j = 0; j < (std::end(input) - std::begin(input)); j++){
            if(input[j] == ans[i]){
                if(ans[i] == input[i]){
                    ct_A += 1;
                }else{
                    ct_B += 1;
                }
            }
        }
    }

    std::cout << std::endl << ct_A << "A" << ct_B << "B" << std::endl;

    if(ct_A == 4 && ct_B == 0){
        std::cout << "Congratulations!! Your answer is correct!" << std::endl;
        std::cout << "The answer is " << input_str << std::endl;
    }else{
        std::cout << "Go! GO! Keep Guessing!!" <<std::endl;
    }

    return 0;
}