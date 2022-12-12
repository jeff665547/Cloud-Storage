# include <iostream>
/* 自訂函數擺放位置 */
// 使用者自定函式是無中生有的，因此必須在使用前先定義該函式，
// 此即為該函式的主體。
// 函式主體的位置通常撰寫在#include和main()主函式的之間，
// 即main()主函式的前面

// 自訂函式也允許放在main()主函式的後面，
// 若放在main()主函式的後面就必須在main()主函式前面先宣告函式的原型，
// 以告知編譯器此自定函式在程式中有定義。
// e.g.
void hello(); // hello函式的宣告

/*Arguments and Parameters*/
// Parameter is variable in the declaration of function.
// Argument is the actual value of this variable that gets passed to function.
void buy(int x){
    std::cout << "The car is " << x << " dollars." << std::endl;
}

/* 傳值呼叫 Call by value (只傳入值，而非傳入變數的整個記憶體位置)*/
void func(int i){
    int a = 2;
    int b = 3;
    i = 5;
    std::cout << "func a, b, i are " << a << " "
    << b << " " << i << std::endl;
}

/* 強制結束某函式 exit(0) */
void exit_func(){
    std::cout << "Call the exit function." << std::endl;
    exit(0);
}

/* 全域變數與區域變數 */
// 區域變數 local variable
void local_func(){
    int xx = 2;
    xx = xx + 1;
    std::cout << xx << std::endl;
}

// 全域變數 global variable
int xx = 1;
int num1 = 5;
int num2 = 10;

/* 傳址呼叫 Call by address */
void swap1(int *pX, int *pY){
    int temp;

    temp = *pX;
    *pX = *pY;
    *pY = temp;

}

/* 傳值呼叫2 Call by value 2*/
void swap2(int pX, int pY){
    int temp;

    temp = pX;
    pX = pY;
    pY = temp;

}

/* 傳遞陣列參數 */
void output(int n, int *p){
    int i;

    for(i = 0; i < n; i++){
        std::cout << p[i] << std::endl;
    }

    std::cout << std::endl;
}

/* 傳遞陣列參數(Input a two-dimensional array to a function) */
double average(int I, int J, int **score){

    double ct = 0;
    double sum = 0;
    double aver;

    for(int i = 0; i < I; i++){
        for(int j = 0; j < J; j++){
            sum += score[i][j];
            ct += 1;
        }
    }
    
    aver = sum/ct;

    return aver;
}

/* 傳遞陣列參數(字串處理) */
void upper(char *a){

    int i = 0;

    while(1){
        if(a[i] >= 'a' && a[i] <= 'z'){
            a[i] -= 32;
        }else if(a[i] == '\0'){
            break;
        }
        i++;
    }

}


int main(){
    
    /* 自訂函式的放置位置 */
    // hello函式的宣告與執行
    std::cout << "Ready to call hello().\n";
    hello();  // 呼叫hello函式
    std::cout << "hello() was called.\n";

    /* Arguments and Parameters */
    buy(20); // x is a parameter, but 20 is an argument for buy function.

    /* 傳值呼叫 Call by value (只傳入值，而非傳入變數的整個記憶體位置)*/
    // 呼叫用的參數內容會被copy到函式用來接收參數的變數中，
    // 也就是說，呼叫時要傳入的參數，和函式中接收用的參數，
    // 事實上是兩個不同的變數。
    // 所以函式中改變參數數值時，原來呼叫處的數值並不會改變
    // 可以想像說，函式中的參數會宣告成一個新的變數，
    // 而它的初值會在呼叫時被設定成傳入的數值。
    // 執行程式後可以發現，每個變數的記憶體位址都不一樣，
    // 所以當然每個變數都是各自獨立的
    // e.g.
    int a = 3;
    int b = 2;
    int i = 4;
    func(i);
    std::cout << "original a, b, i are " << a << " "
    << b << " " << i << std::endl;

    /* 全域變數與區域變數 global variable and local variable */
    // 區域變數: 區域變數的有效範圍僅在該函式內，
    // 離開該函式便由記憶體中釋放掉，
    // 下次呼叫該函式時再重新配置記憶體給該函式使用。
    // 全域變數: 的有效時間則一直到程式結束為止。
    // 程式中區域變數與全域變數的名稱相同，
    // 當存取函式內的變數時會以區域變數為優先，
    // 使用時最好注意，
    // 建議全域變數最好不要和區域變數的名稱重複，
    // 以免參用時造成混淆。
    // e.g.
    int xx = 1;
    local_func();
    local_func();
    std::cout << xx << std::endl;

    /* 傳址呼叫 Call by address */
    // 傳址呼叫就是函式在做引數傳遞時，
    // 呼叫函式中的實引數是將自己本身的記憶體位址傳給被呼叫函式內的引數。
    // 使用時機: 希望將回傳一個以上的結果時使用。
    // 設定方式:
    // 定義的函式小括號內的虛引數必須宣告為指標變數。
    // (即在變數前面加上*)
    // 呼叫函式內的引數必須傳送變數的記憶體位址。
    // (即在變數前面加上&)
    // 要是函式傳參數時，傳的是變數的位址，
    // 就可以在函式中去改變主程式中變數的內容了。
    // e.g.
    std::cout << "The address of num1 is " << &num1 << std::endl;
    std::cout << "Its value is " << num1 << std::endl;
    std::cout << "The address of num2 is " << &num2 << std::endl;
    std::cout << "Its value is " << num2 << std::endl;
    swap1(&num1, &num2);
    std::cout << "The address of num1 is " << &num1 << std::endl;
    std::cout << "Its value is " << num1 << std::endl;
    std::cout << "The address of num2 is " << &num2 << std::endl;
    std::cout << "Its value is " << num2 << std::endl;
    // The address of the two global variables (num1, num2) are not changed. 
    // However, their values are exchanged.
    swap2(num1, num2);
    std::cout << "The address of num1 is " << &num1 << std::endl;
    std::cout << "Its value is " << num1 << std::endl;
    std::cout << "The address of num2 is " << &num2 << std::endl;
    std::cout << "Its value is " << num2 << std::endl;

    std::cout << "==============================" << std::endl;

    /* 傳遞陣列參數 */
    // 把陣列當參數來傳遞時，要從記憶體的角度來看，
    // 如果傳遞的只是陣列某欄位中的一個變數，那和傳統普通變數沒有什麼分別。
    // 如果傳的是整個陣列，傳遞的東西會是陣列的位址。
    // e.g. (array 和 pointer 不完全等價, 此例一維array是恰巧為這樣,
    // 若是二維array, 則傳入的argument也必須要是pointer of pointer, 
    // 不能使用陣列來傳入function，意即型別要一致)
    int aa[5] = {1, 2, 3, 4, 5};
    int bb[7] = {1, 2, 3, 4, 5, 6, 7};

    output(5, aa);
    output(7, bb);

    std::cout << "========================================" << std::endl;

    /* 傳遞陣列參數(Input a two-dimensional array to a function) */
    int **score_matrix;
    int nrow, ncol, ii, jj;
    std::cout << "Please enter the row number of the matrix:" << std::endl;
    std::cin >> nrow >> ncol;


    score_matrix = new int*[nrow];
    std::cout << "Please enter the number that you want to calculate the average:" << std::endl;
    for(ii = 0; ii < nrow; ii++){
        score_matrix[ii] = new int[ncol];
    }

    for(ii = 0; ii < nrow; ii++){
        for(jj = 0; jj < ncol; jj++){
            std::cin >> score_matrix[ii][jj];
            std::cout << score_matrix[ii][jj] << std::endl;
        }
    }

    std::cout << "The average is " << average(nrow, ncol, score_matrix) << std::endl;


    /* 傳遞陣列參數(字串處理) */
    char str[80];

    std::cout << "Please input an integer: " << std::endl;
    std::cin >> str;
    upper(str);

    std::cout << str << std::endl;

    /* 函數指標 */
    

    /* 強制結束某函式 exit(0) */
    exit_func();
    std::cout << "The program is terminated." << std::endl;

    return 0;
}

/* 自訂函數擺放位置 */
void hello(){  // void代表不回傳資料

    std::cout << "Hello" << std::endl;
    std::cout << "Hello" << std::endl;
    std::cout << "Hello" << std::endl;

}
