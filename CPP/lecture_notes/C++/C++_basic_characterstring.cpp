#include <iostream>
# include <string>

int main(){

    /*Character Input Classification*/
    char ch;
    std::cin >> ch;

    if(ch >= '0' && ch <= '9'){
        std::cout << "The input is an integer." << std::endl;
    }else if(ch >= 'A' && ch <= 'Z'){
        std::cout << "The input is a capital english letter." << std::endl;
    }else if(ch >= 'a' && ch <= 'z'){
        std::cout << "The input is a small english letter." << std::endl;
    }else{
        std::cout << "The input cannot be recognized." << std::endl;
    }

    /*Character Conversion*/
    char ch2;
    std::cin >> ch2;

    if(ch2 >= 'A' && ch2 <= 'Z'){
        std::cout << ch2 << std::endl;
    }else if(ch2 >= 'a' && ch2 <= 'z'){
        ch2 -= ('a' - 'A');
        std::cout << ch2 << std::endl;
    }else{
        std::cout << "This input is not a english letter." << std::endl;
    }
    
    /*String*/
    // Initialize a string.
    char a[] = "Hello";  // String initialization by using "".
    
    char b[] = {'H', 'e', 'l', 'l', 'o', '\0'};  // String initialization by using array.
    // \0 是字串結束字元，每個字串結束的最後一個字元。

    // String initialization with declaration.
    char c[6]; // Declare a character array.

    c[0] = 'H';
    c[1] = 'e';
    c[2] = 'l';
    c[3] = 'l';
    c[4] = 'o';
    c[5] = '\0';

    // Print the string;
    std::cout << a << std::endl;
    std::cout << b << std::endl;

    // The string inputted from the keypad cannot include a space.
    char aa[80];

    std::cin >> aa;
    std::cout << aa << std::endl;

    std::cout << "===========================" << std::endl;
    
    // Use a two-dimensional array to store multiple strings.
    int z;
    char name[3][80];

    for(z = 0; z < 3; z++){
        gets(name[z]); // Use "gets" to replace a for loop initialization. (within a string)
        // #include <stdio.h>

        std::cout << name[z] << std::endl;
    }

    /* Some useful string library for C++*/
    // # include <string> 
    // Use string to initialize a string.
    std::string str1; // declaration.
    std::string str2("caterpillar");  
    std::string str3 = "example";
    
    // Define a declared string.
    str1 = "dwcefcefcrc";
    std::string str4 = str1;

    std::cout << str3 << std::endl;
    
    // Combine strings with "+" (std::string).
    std::cout << str1 + " " + str3 << std::endl;

    // Compare strings with "==" (std::string).
    int ans1 = str1 == str4;  
    int ans2 = str1 != str4;
    std::cout << ans1 << std::endl;
    std::cout << ans2 << std::endl;

    // Compute the length of a string. 
    // The ending notation "\0" is not taken into account. 
    // (std::string)
    std::cout << str3.length() << std::endl;
    std::cout << str3.size() << std::endl;
    // Both usages above are equivalent.

    std::cout << "==================" << std::endl;
    
    // Advanced useful string methods.
    // str.assign(): "="
    std::cout << "====str.assign()====" << std::endl;
    str1 = str1.assign(str2, 0, 5);  // start from 0, total: 5 characters in the str2.
    std::cout << "str1: " << str1 << std::endl;
    str1 = str1.assign("caterpillar", 5, 6);  // start from 5, total: 6 characters in the "caterpillar".
    std::cout << "str1: " << str1 << std::endl;

    // str.append(): "+" 
    std::cout << "====str.append()====" << std::endl;
    str1 = " ";
    str1 = str1.append(str2, 0, 5);  // start from 0, total: 5 characters in the str2.
    str1 = str1.append(str3, 5, 6);  // start from 5, total: 6 characters in the str2.
    std::cout << "str1: " << str1 << std::endl;

    // str.find(): 尋找字串位置 
    str1 = "caterpillar";
    std::cout << "====str.find()====" << std::endl;
    std::cout << "find pill from str1: (str1: 'caterpillar') "
              << str1.find("terp", 0) << std::endl;
              // find "pill", "0" means start from the str1[0]

    // str.insert(): 插入字串
    std::cout << "====str.insert()====" << std::endl;
    std::cout << "jinput str1 with ***: " 
              << str1.insert(5, "***") << std::endl;
              // insert "***" at the str1[5]    

    return 0;
}
