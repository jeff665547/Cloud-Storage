#include <iostream>

// std::vector<int> ArrayNumber(std::string string){
//     static int input[4];
//     int i;

//     for(i = 0; i < string.length(); i++){
//         input[i] = (int) string[i] - 48;
//     }

//     return input;
// }



auto foo(int i)
{
    return std::tuple(10, 20)
}

int main(){

    auto [a, b] = foo(i);
    int a = 
    // std::string input_str;
    // int i;
    // int j;
    // int ct_A = 0;
    // int ct_B = 0;

    // std::cout << "Please enter a number with four non-repeated digits: " ;

    // std::cin >> input_str;

    // int* int_arr = ArrayNumber(input_str);

    // std::cout << std::begin(int_arr);
    
    int *B = new int[4];
    for (int i = 0; i != 4; ++i)
        B[i] = i;

    std::cout << "...\n";

    std::cout << B[1] << ", " << *(B + 1) << '\n';

    //for(i = 0; i < (std::end(ans) - std::begin(ans)); i++){
    //    for(j = 0; j < (std::end(int_arr) - std::begin(int_arr)); j++){
    //        if(int_arr[j] == ans[i]){
    //            if(ans[i] == int_arr[i]){
    //                ct_A += 1;
    //            }else{
    //                ct_B += 1;
    //            }
    //        }
    //    }
    //}
//
    //std::cout << std::endl << ct_A << "A" << ct_B << "B" << std::endl;
//
    //if(ct_A == 4 && ct_B == 0){
    //    std::cout << "Congratulations!! Your answer is correct!" << std::endl;
    //    std::cout << "The answer is " << input_str << std::endl;
    //}else{
    //    std::cout << "Go! GO! Keep Guessing!!" <<std::endl;
    //}
//
    return 0;
}