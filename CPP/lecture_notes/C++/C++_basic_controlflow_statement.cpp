# include <iostream>
#include <conio.h>

int main(){

    // if-else control flow
    int guess;
    std::cin >> guess;

    if(guess == 2){
        std::cout << "The ans is 2!" << std::endl;
    }else if(guess == 3){
        std::cout << "The ans is 3!" << std::endl;
    }else{
        std::cout << "Wrong Answer!" << std::endl;
    }

    // switch control flow
    double a, b, ans;
    char key;

    std::cout << "Input two number:" << std::endl;
    std::cin >> a >> b;
    std::cout << "Press +, -, *, /:" << std::endl;
    std::cin >> key;

    switch(key){
        case '+':
            ans = a + b;
            break;
        
        case '-':
            ans = a - b;
            break;

        case '*':
            ans = a * b;
            break;

        case '/':
            ans = a / b;
            break;
        
        default:
            std::cout << "Undefined key!" << std::endl;
            return 0;
    }

    std::cout << a << key << b << '=' << ans << std::endl;

    // for loop
    int i;
    for(i = 0; i < 10; i++){
        // 在上方的條件當中 i = 0 為初始運算式
        // i < 10 為條件運算式
        // i++ 為控制運算式
        // 執行順序: 初始運算式 => 重複執行的程式碼 
        //           => 初始運算式 => 條件運算式
        //           => (重複執行的程式碼 => 初始運算式 
        //               => 條件運算式 ...) => 跳出迴圈
        std::cout << "Hello World!" 
        << i << std::endl;
    }

    std::cout << "==========================" << std::endl;

    for(i = 0; i < 10; ++i){
        // Difference between ++i and i++ in the for loop.
        std::cout << "Hello World!" 
        << i << std::endl;
    }

    // While loop 
    // (Test the condition before executing the code below.)
    char keyin_while = '0';

    while(keyin_while != 'q'){
        std::cout << "Please key in a value to leave here: (q)" << std::endl;
        std::cin >> keyin_while;
        std::cout << keyin_while << std::endl;
    }

    std::cout << "==========================" << std::endl;

    // Do while loop
    // (Test the condition after executing the code below.
    //  Execute the code at least one time.)
    char keyin_dowhile = '0';

    do{
        std::cout << "Please key in a value to iterate the code in this section: (0)" << std::endl;
        std::cin >> keyin_dowhile;
        std::cout << keyin_dowhile << std::endl;
    }while(keyin_dowhile == '0');


    // break and continue
    char keyin_break;

    while(1){
        // Detect the keypad in C #include <conio.h>
        std::cout << "Please key in a value to leave here: (q)" << std::endl;
        keyin_break = getche();
        if(keyin_break == 'q'){
            std::cout << std::endl;
            break;
        }
        std::cout << std::endl;
    }

    int j;
    for(j = 1; j <= 10; j++){
        if(j == 4){
            continue;
        }
        std::cout << "Floor: " << j << std::endl;
    }

    return 0;
}