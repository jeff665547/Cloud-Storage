# include <iostream>
# include <stdlib.h>  // malloc() function

int main(){

    /* Introduction about the pointer */
    // When to use the pointer:
    // 1. 動態記憶體配置
    // 2. 函式的設計
    
    /* An example */
    int *p;
    int a = 70, b;
    p = &a;
    b = *p + 1;  // a = 71, b = 71, *p = 71
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;
    *p = 80;  // a = 80, b = 71, *p = 80
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;

    /* Array and pointer */
    int A[3] = {1, 2, 3};
    
    std::cout << A << std::endl; // The address of the first element of A. 陣列名稱為記憶體位置
    std::cout << &A[0] << std::endl;  // The address of the first element of A.
    std::cout << *A << std::endl;  // The dereference (value) of the address of the first element of A.
    std::cout << A[0] << std::endl;  // The value of the first value of A.

    std::cout << "=====================" << std::endl;

    /* Print an array with a pointer */
    int AA[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *Q, *P, i;

    P = AA; //or P=&AA: 陣列名稱為記憶體位置
    Q = AA;
    for(i = 0; i < 10; i++){
        std::cout << *P << std::endl;
        P++;

        std::cout << "======start========" << std::endl;
        std::cout << Q[i] << std::endl;
        std::cout << *(Q + i) << std::endl;
        std::cout << "=======end=========" << std::endl;
    }

    std::cout << "================================" << std::endl;

    /*Difference between array and pointer*/
    int BB[2][3] = {{1, 2 ,3}, {4, 5, 6}};
    int CC[2][3] = {{7, 8, 9}, {0, 1, 2}};
    int C = 3;
    int *PP = &C;
    int D = 5;

    // Pointer
    std::cout << PP[0] << std::endl;
    std::cout << *(PP+0) << std::endl;
    std::cout << *PP << std::endl;
    std::cout << "Original, PP[1] is " << PP[1] << "." << std::endl;
    PP[1] = D; // PP is 5.
    std::cout << "PP[1] is " << *(PP+1) << " now." << std::endl;
    std::cout << "PP[1] is " << PP[1] << " now." << std::endl;  
    // *(PP+1) is equivalent to PP[1].

    std::cout << "Original, PP is " << PP << "." << std::endl;
    std::cout << "And its value is " << *PP << std::endl;
    PP = &D; // PP is 5.
    std::cout << "PP's value is " << *PP << "," << std::endl;
    std::cout << "and PP is " << PP << " now." << std::endl;  
    
    // Array
    BB[2][2] = 10;
    std::cout << BB[2][2] << std::endl; // Array cannot be assigned a value without index.
    // Its name cannot be use to store some value directly.

    /* Dynamical Memory Allocation */
    // 當程式執行到一半，發現它需要一塊記憶體空間來存放資料，才向系統索取一塊記憶體空間。
    // 當此記憶體空間用不到時，也可隨時將之釋放供其它程式使用。
    // 由於寫程式時無法預知使用者需要多少資料，
    // 因此可設計成在使用者輸入數字個數後，
    // 再動態配置所需的記憶體空間來存放數值。
    // Concept:
    // 先準備好一個指標
    // 跟系統要求空間, 用指標間接操作
    // 使用完畢後, 將配置的記憶體釋放


    // In C:
    int *ptr1 = (int*)malloc(sizeof(int)*3);
    // 先準備好一個指標
    // sizeof(int) 取得記憶體中一個整數變數的大小，假設為4 Bytes。
    // sizeof(int)*3 取得記憶體中三個整數變數的大小，假設為12 Bytes。
    // malloc(sizeof(int)*3)系統配置連續12個記憶體位址給這3個整數變數使用，
    // 並且回傳一個void pointer，且該pointer指向此12個連續記憶體的起始位址。
    // (int*)malloc(sizeof(int)*3) 利用(int*)將malloc()函式回傳的void指標
    // 轉換成int型別的整數指標，最後在指定給ptr整數指標。

    free(ptr1);
    // 釋放記憶體


    // In C++:
    int *ptr2 = new int[3];
    // ptr2是指向整數的指標
    // 向作業系統要3個整數空間並把這位址交給ptr2

    delete ptr2;
    // 釋放記憶體
    

    /* Dynamical Memory Allocation (Pointer and Array, Multiple-Dim Array)*/
    // 用多個指標配置出不同行數之二維陣列。
    // In C:
    int *new_a[3];  // 宣告3個可以指向整數的指標變數。

    new_a[0] = (int *)malloc(sizeof(int));
    new_a[1] = (int *)malloc(sizeof(int)*2);
    new_a[2] = (int *)malloc(sizeof(int)*3);

    new_a[0][0] = 10;
    new_a[1][0] = 20;
    new_a[1][1] = 30;
    new_a[2][0] = 40;
    new_a[2][1] = 50;
    new_a[2][2] = 60;

    // new_a is:
    //
    // 10
    // 20 30
    // 40 50 60
    //


    // In C++:
    int *new_b[3];  // 宣告3個可以指向整數的指標變數。

    new_b[0] = new int;
    new_b[1] = new int[2];
    new_b[2] = new int[3];

    new_b[0][0] = 10;
    new_b[1][0] = 20;
    new_b[1][1] = 30;
    new_b[2][0] = 40;
    new_b[2][1] = 50;
    new_b[2][2] = 60;

    // new_b is:
    // 
    // 10
    // 20 30
    // 40 50 60
    //

    std::cout << "==============================" << std::endl;

    /* Dynamical Memory Allocation (Data Structure: Linked list 鏈結串列) */
    // 指標再指向另一個指標 => 鏈結串列
    int KKK = 10;
    int *ptr11 = &KKK;
    int **ptr22 = &ptr11;
    std::cout << "The value of **ptr22 is: " << **ptr22 << std::endl;


    // 指標的指標 => 多重指標
    // 應用: 配置列數不固定，行數也不固定的二維陣列
    // Pointer can’t be initialized at definition
    // Pointer is dynamic in nature. 
    // The memory allocation can be resized or freed later. 
    // e.g. 動態配置m班，每班n人，輸入成績後計算平均分數
    int mat_i, mat_j;
    double sum = 0, aver;
    int **student;
    int class_m, peo_n;

    std::cout << "Class Number: " << std::endl;
    std::cin >> class_m;
    std::cout << "People in the class: " << std::endl;
    std::cin >> peo_n;

    // 動態配置m班各n人之記憶體
    // In C:
    student = (int**)malloc(sizeof(int*)*class_m);  // 系統配置連續記憶體位址給這class_m個整數指標變數使用
    for(mat_j = 0; mat_j < class_m; mat_j++){
        student[mat_j] = (int*)malloc(sizeof(int)*peo_n);
    }

    // In C++:
    student = new int*[class_m];  // 系統配置連續記憶體位址給這class_m個整數指標變數使用
    for(mat_j = 0; mat_j < class_m; mat_j++){
        student[mat_j] = new int[peo_n];
    }


    // 分別讀入m班, 各n個同學成績
    for(mat_j = 0; mat_j < class_m; mat_j++){
        std::cout << "Class: " << mat_j + 1 << std::endl;
        for(mat_i = 0; mat_i < peo_n; mat_i++){
            std::cout << "Student: " << mat_i + 1 << std::endl;
            std::cin >> student[mat_j][mat_i];
        }
    }

    // 計算總和
    for(mat_j = 0; mat_j < class_m; mat_j++){
        for(mat_i = 0; mat_i < peo_n; mat_i++){
            sum += student[mat_j][mat_i];
        }
    }

    // 求平均值
    aver = sum/(class_m*peo_n);
    std::cout << "The overall average is " << aver << std::endl;

    return 0;
}
