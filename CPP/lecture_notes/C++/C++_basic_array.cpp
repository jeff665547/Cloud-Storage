#include <iostream>
#include <string.h>
#define class 2
#define student 5

int main(){

    int i;
    int score[student];

    for(int i = 0; i < student; i++){
        std::cin >> score[i];
        std::cout << score[i] << std::endl;
    }

    /*Initialize an one-dim Array*/
    // setting a[0] = 1, a[1] = 2, a[2] = 3, a[3] = 4, a[4] = 5
    int a[5] = {1, 2, 3, 4, 5};

    // 沒指定size ，且只有3個值。因此，會自動設定成b[3]。
    int b[] = {1, 2 ,3};

    // 所有值都設為0
    int c[5] = {0};
    
    // 初始化值不足，多的位置會設成0
    int d[5] = {80, 60, 22};

    // Copy an array.
    int *e = a;

    // Copy to a declared array. Function in C.
    int f[5];
    memcpy(f, a, sizeof(int)*5);
    // memcpy(目標陣列; 來源陣列; sizeof(型態)*陣列元素個數)

    std::cout << "===================================" << std::endl;

    /*Array Application - Caculate Avergae*/
    int j;
    double sum = 0;
    double aver = 0;

    for (int k = 0; k < student; k++){
        std::cin >> score[k];
        sum += score[k];
    }
    aver = sum/student;
    std::cout << aver;

    /*Sorting Problem*/
    // Swap two variables.
    int g = 10, h = 5, temp;
    
    std::cout << "g = " << g << std::endl;
    std::cout << "h = " << h << std::endl;

    temp = g;
    g = h;
    h = temp;

    std::cout << "g = " << g << std::endl;
    std::cout << "h = " << h << std::endl;

    // Sort an array
    int data[5] = {34, 12, 5, 66, 1};
    int temp2;
    int m, n;

    for(int t = 0; t < 5; t++){
        std::cout << data[t] << " ";
    }
    std::cout << std::endl;

    for(m = 5; m > 1; m--){  // 需要找4次最大值
        for(n = 0; n < m-1; n++){  // 每次要比對m-1次
            if(data[n] > data[n + 1]){  // 若比後面的數值大就往後交換
                temp2 = data[n];
                data[n] = data[n+1];
                data[n+1] = temp2;
            }
            for(int t = 0; t < 5; t++){
                std::cout << data[t] << " ";
            }
            std::cout << std::endl;
        }
        std::cout << "=======" << std::endl;
    }

    for(int t = 0; t < 5; t++){
        std::cout << data[t] << " ";
    }
    std::cout << std::endl;

    std::cout << "===================================" << std::endl;

    /*Two Dimensional Array*/
    // 二維陣列在記憶體中的排列方式: 利用連續的記憶體空間，製作行列的效果
    // 意即第二列的值在記憶體的位置為緊接地儲存在第一列後方。
    // Initialize an two-dims Array
    int aa[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int bb[2][2] = {1, 2, 3, 4};
    int cc[2][2] = {0};  // 所有資料都設為0
    
    // Initialize a declared array
    int dd[2][2];
    dd[0][0] = 1;
    dd[0][1] = 2;
    dd[1][0] = 3;
    dd[1][1] = 4;

    // Print a two-dim array
    int ee[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int ii, jj;
    for(jj = 0; jj < 3; jj++){
        for(ii = 0; ii < 3; ii++){
            std::cout << ee[jj][ii] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}