#include <iostream>
#include <string>

int main(){

    std::string input;
    int i;
    int ct_A = 0;
    int ct_B = 0;

    std::cout << "Please enter a number with four non-repeated digits: " ;
    std::cin >> input;

    std::string ans = "3456";

    for(i = 0; i < ans.length(); i++){
        std::cout << ans[i];
        if(input.find(ans[i]) <= 3){
            if(ans[i] == input[i]){
                ct_A += 1;
            }else{
                ct_B += 1;
            }
        }
    }

    std::cout << std::endl << ct_A << "A" << ct_B << "B" << std::endl;

    if(ct_A == 4 && ct_B == 0){
        std::cout << "Congratulations!! Your answer is correct!" << std::endl;
        std::cout << "The answer is " << ans << std::endl;
    }else{
        std::cout << "Go! GO! Keep Guessing!!" <<std::endl;
    }

    return 0;
}