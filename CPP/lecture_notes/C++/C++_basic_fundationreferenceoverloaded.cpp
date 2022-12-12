// C++包含C語言的所有功能，
// 另外提供完整物件導向程式設計
// (Object-Oriented Programmin: OOP)功能
//
// C++特色:
//
// 1. 高階的程式描述方式
// 更利於用來開發大型專案，
// 讓程式設計師在分工時更能快速的開發程式，
// 並減少錯誤的產生。
//
// 2. 物件導向程式設計
// 讓開發程式者簡單的使用物件所提供的功能，
// 來達到所需要的效果
//
// 注意: 新式標頭寫法
// C++逐漸取代傳統的C語言，
// 在C++程式中，
// 若有使用到這些C語言所提供的標頭檔時，
// 建議使用新式標頭寫法。
// 其做法就是在標頭檔名稱最前面加上小寫的c
// 和省略副檔名*.h即可
// 如: #include <cstdio>
// 
// e.g. 一個正確的C++程式


// Program: gretting.cpp  // => 由註解開頭
#include <iostream>  // 程式中使用IO
#include <string> // 程式中使用string物件
#include <string.h> // 程式使用strcpy()


/* C++ reference */
void increment(int &n){
    n += 1;
}

/* C++ overload */
void show(int x){
    std::cout << "I'm an integer, int: " << x << std::endl;
}
void show(double x){
    std::cout << "I'm a float, int: " << x << std::endl;
}

int main(int argc, char *argv[]){

    std::cout << "Hello\n";
    std::cout << "This is the first program of C++" << std::endl;  
    // 輸出雙引號括住的字串常數，並將游標移到下一行的開頭。    

    /* C++ Input */
    char K[80];

    std::cout << "Please enter a string." << std::endl;
    std::cin >> K;
    std::cout << K << std::endl;
    
    // 同時使用cin的 >> 與 getline 會產生衝突, 用cin.ignore()來避免衝突
    std::cin.ignore();

    // 輸入含有空白字元的字串
    // 用法: cin.getline(字元陣列名稱，最大長度)
    std::cout << "Please enter a sentence." << std::endl;
    std::cin.getline(K, 80);
    std::cout << K << std::endl;


    /* C++ Dynamic Memory Allocation */
    // Dynamic Memory Allocation: new
    // 配置一個資料空間，並傳回該空間的位址
    // 用法: 指標 = new 資料型態;
    // 
    // 配置一個給定初始值的空間，並傳回該空間的位址
    // 用法: 指標 = new 資料型態(初始值);
    //
    // 配置多個資料空間，並傳回該空間的位址
    // 用法: 指標 = new 資料型態[個數];
    // 
    // Release Memory: delete
    // 配置一個空間的釋放    
    // 用法: delete 指標;
    // 
    // 配置多個空間的釋放
    // 用法: delete [] 指標;
    //
    // e.g. 

    // 配置一個給定初始值的空間
    int *ptr = new int(100);
    std::cout << "variable address:" << ptr << std::endl;
    std::cout << "variable value:" << *ptr << std::endl;

    *ptr = 200;
    std::cout<< "variable address:" << ptr<< std::endl;
    std::cout << "variable value:" << *ptr << std::endl;

    delete ptr;

    // 配置多個資料空間
    int *ptr2;
    int size, i;

    std::cout << "Please enter a number: " << std::endl;
    std::cin >> size;
    ptr2 = new int[size];
    std::cout << "Please enter the elements: " << std::endl;
    for(i = 0; i < size; i++){
        std::cout << "ptr2[" << i << "] = ";
        std::cin >> ptr2[i];
    }
    for(i = 0; i < size; i++){
        std::cout << "ptr2[" << i << "] = " << ptr2[i] << std::endl;
    }

    delete [] ptr2;


    /* C++ String */
    // declare 用法: string 字串物件名稱
    // 字串物件提供下面語法可以使用:
    //    std::cin.getline(cin, str, '\n'); 可輸入含"空白"的字串
    //    [索引]: 取得索引值代表的字元
    //     =: 字串複製
    //     ==: 字串比對
    //     +=: 字串連結
    //     length(): 計算字串長度
    //     c_str(): 回傳字串位置(常用在字串函式)

    // ex.1 輸入字串後印出長度與所有字元
    std::string str;
    int n;
    std::cout << "Please input a string." << std::endl;
    std::cin >> str;

    n = str.length();
    std::cout << "Input length: " << n << std::endl;
    std::cout << "The character in the string is" << std::endl;
    for(i = 0; i < n; i++){
        std::cout << "[" << i << "]:" << str[i] << std::endl;
    }

    // ex.2 string常用之運算
    std::string aa, bb;
    aa = "Hello!";
    std::cout << "Please input string bb:" << std::endl;
    std::cin >> bb;

    if(aa == bb){
        std::cout << "String aa is same as string bb." << std::endl;
    }else{
        std::cout << "String bb is different from string aa." << std::endl;
    }

    aa += bb;
    std::cout << "The connection result of string aa and bb is " << aa << std::endl;

    // ex.3 輸入a字串內容後儲存b (字元陣列 => 字串)
    char str_a[80];
    std::string str_b;

    std::cout << "Please enter a character string str_a: ";
    std::cin >> str_a;

    str_b = str_a;

    std::cout << "Output the string str_b: " << str_b << std::endl;
    
    // ex.4 輸入b字串內容後儲存a (字串 => 字元陣列)
    std::cout << "Please enter a string str_b: ";
    std::cin >> str_b;

    strcpy(str_a, str_b.c_str());

    std::cout << "Output the characeter array str_a: " << str_a << std::endl;

    std::cout << "=================================" <<std::endl;

    /* C++ Reference */
    // 參考(Reference)型態代表了變數或物件的一個別名(Alias)
    // 參考型態可以直接取得變數或物件的位址，並間接透過參考型態別名來操作物件
    // 作用類似於指標，但卻不必使用指標語法，也就是不必使用*運算子來提取值。
    // 要定義參考型態，在定義型態時於型態關鍵字後加上&運算子
    // 參考型態一定要初始化，因為參考初始化後就不能改變它所代表的物件，
    // 任何指定給參考的值，就相當於指定給原來的物件。
    // 參考型態最常使用於函式的參數列上
    // e.g.
    int var = 10;    // 定義變數
    int *ptr3 = &var; // 定義指標，代表var變數位置
    int &ref = var;  // 定義參考，代表var變數

    std::cout << "var: " << var << std::endl;
    std::cout << "*ptr: " << *ptr3 << std::endl;
    std::cout << "ref: " << ref << std::endl;
    ref = 20;
    std::cout << "var: " << var << std::endl;
    std::cout << "*ptr: " << *ptr3 << std::endl;
    std::cout << "ref: " << ref << std::endl;

    // 參考型態最常使用於函式的參數列上
    int x = 10;

    increment(x);
    std::cout << x << std::endl;

    /* C++ overloaded */
    // 1. 定義多個名稱相同，但引數的型態和數量不同之函數，
    //    就叫作函數的多載（多重定義：function overloading）。
    // 2. 當函數進行多載時，可以依照呼叫時所傳遞的引數，
    //    來呼叫出適當的函數。
    // 3. 要進行多載的函數，其引數的型態或個數都必須不同，
    //    否則將無法判斷要呼叫的函數，
    //    因此也必須避免使用預設引數。
    // 4. C++支援函式「重載」(Overload)，
    //    根據回傳值的不同或參數列個數或型態的不同，
    //    而自動呼叫對應的函式。
    // 5. 從使用函式的角度... 功能一樣，
    //    但參數不同的函式不用取多個名字比較好記!
    // e.g. 
    // 根據參數的型態來決定要呼叫的函式
    show(12);
    show(12.5);

    return 0;
    // 將0傳回給系統表示系統正常結束，若傳回非0值則代表失敗。
}

// C++的cin/cout物件較scanf/printf函式聰明，所以比較容易使用。
// 在聰明的背後... (使用物件很容易，自己設計物件比較困難!)

