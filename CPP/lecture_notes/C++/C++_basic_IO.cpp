#include <iostream>
#include <stdio.h>

int main(){

    // Baisic I/O for C++
    int K;
    std::cin >> K;
    std::cout << K << std::endl;

    // Basic I/O for C
    int L;
    scanf("%d", &L); // The input from the keypad stores in the variable L.
    printf("%d\n", L); // The output of the variable K is printed to the monitor.

    // Print with format for C
    printf("%c is a character.\n", 'A');
    printf("%d is an integral.\n", 33);
    printf("%f is a float.\n", 5678.5678);
    printf("|%12f is a float.\n", 5678.5678); // 12 代表總位數(小數點也算一位)
    printf("|%012f is a float.\n", 5678.5678); // 0 代表小數點前多餘的空白位數補0
    printf("|%-12f is a float.\n", 5678.5678); // - 代表向左對齊
    printf("|%.2f is a float.\n", 5678.5678); // .2 代表顯示到小數點後面第幾位(四捨五入)
    std::cout << "===========================" << std::endl;
    
    // Scan format for C
    int num1;
    int num2;
    scanf("%d%d", &num1, &num2);
    printf("The first number is %d.\nThe second number is %d.\n", num1, num2);
    std::cout << "===========================" << std::endl;
    
    // Basic data transformation
    int a1 = 46, a2 = 5;
    double b1 = 46, b2 = 5;
    double x, y;
    x = a1/a2;  // x = 9
    y = b1/b2;  // y = 9.2
    std::cout << 46/5 << std::endl;
    std::cout << a1/a2 << std::endl;
    std::cout << x << std::endl;
    std::cout << y << std::endl;

    x = (double) a1/a2; // x = 9.2
    std::cout << x << std::endl;
    std::cout << "===========================" << std::endl;
    
    // Basic operation
    int a = 0;
    std::cout << a << std::endl;
    a += 5;  // a = 5
    std::cout << a << std::endl;
    a++;     // a = a + 1, a = 6
    std::cout << a << std::endl;
    a /= 3;  // a = a / 3, a = 2
    std::cout << a << std::endl;
    a *= 5;  // a = a * 5, a = 10
    std::cout << a << std::endl;
    a -= 4;  // a = a - 4, a = 6
    std::cout << a << std::endl;
    a %= 3;  // a = a % 3, a = 0
    std::cout << a << std::endl;

    std::cout << "===========================" << std::endl;
    int b = 0, c;

    b = 10;
    b += 10;  // b = 20, c
    std::cout << b << std::endl << std::endl;
    
    b = 10;    
    c = b++;  // b = 11, c = 10
    std::cout << b << std::endl << c << std::endl;

    b = 10;    
    c = ++b;  // b = 11, c = 11
    std::cout << b << std::endl << c << std::endl;

    b = 10;
    c = b--;  // b = 9, c = 10
    std::cout << b << std::endl << c << std::endl;

    b = 10;
    c = --b;  // b = 9, c = 9
    std::cout << b << std::endl << c << std::endl;

    return 0;
}