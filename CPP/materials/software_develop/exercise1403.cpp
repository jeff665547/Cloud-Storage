#include <iostream>
#include <string>

int main(){

    std::string ans = "1234"; // not replication
    std::string guess;
    std::cin >> guess;

    int ct_A = 0;
    int ct_B = 0;
    
    for(int i = 0; i < guess.length(); i++){
        if(guess.find(ans[i]) != 18446744073709551615){
            if(guess[i] == ans[i]){
                ct_A += 1;
            }else{
                ct_B += 1;
            }
        }
    }

    std::cout << ct_A << 'A' << ct_B << 'B' << std::endl;
    
    return 0;
}