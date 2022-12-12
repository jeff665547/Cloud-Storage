/* 把程式拆成多個檔案 */
// header (.h) <- 用來宣告函式名稱 (用來被include)
// 程式檔, 實做檔 (.c) <- 用來寫函式程式碼 (放到專案一起編譯與連結)
// 此程式包含3個檔，首先是這個檔，第2個是hello.h，第3個則是hello.c
# include <iostream>

# include "hello.h"
// hello() 的宣告在這裏面
// 注意是用" "而非< >

int main(){

    std::cout << "Ready to call hello()" << std::endl;
    hello();
    std::cout << "hello() is called." << std::endl;

    return 0;
}
