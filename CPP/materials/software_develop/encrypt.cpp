// This is the preprocessor, start with "#". (introduce header file, def macro or constant)
// This is macro start with #define
#define DIFF 97
#define N 26
//#define PrintInt(a) std::cout << a << std::endl

#include "encrypt.hpp"
#include <cstdlib>  // srand() (like set seed), rand()
#include <ctime>  // time()

// the constructor of Encrypt (setting the initial value)
Encrypt::Encrypt(){
    set_code_array();
}

std::string Encrypt::to_encode(std::string s){
    // temp character variable from parameter string
    char c;

    // temp encode results 
    std::string r;
    int i, m;

    for(i = 0; i < s.size(); i++){

        // judge if the character is an uppercase
        if((s.at(i) >= DIFF) && (s.at(i) < DIFF + N)){
            c = s.at(i);
            m = c - DIFF;
            r += get_code_array().at(m);
        }else{
            r += s.at(i);
        }
    }

    return r;
}

std::string Encrypt::to_decode(std::string s){

    std::string r;
    int i, j;

    for (i = 0; i < s.size(); i++){
        if (s.at(i) >= DIFF && s.at(i) < DIFF + N){
            
            for (j = 0; j < N; j++){
                if (s.at(i) == get_code_array().at(j)){
                    r += static_cast<char>(j + DIFF);  // type converting. convert int into char.
                    break;
                }
            }
        }else{
            r += s.at(i);
        }
    }
    return r;
}

void Encrypt::set_code_array() {

    srand(time(0)); // initialize the random number generator, 
                    // take the current time as the input parameter of the random seed. 

    int a = 0;
    int b = 0;

    while ((a%2) == 0){
        a = rand() % 10;
        b = rand() % 10;
    }

    std::cout << a << ", ";  // print the value of a
    std::cout << b << ", ";  // print the value of b

    // Use the formula to construct the converting table
    int x, y, m;
    char c = 'a';
    std::string s;
    int i;
    for (i = 0; i < N; i++){

        x = c;
        y = x * a + b;
        m = y%N;
        s += m + DIFF;  // a's ASCII is 97 (DIFF)
        c++;

    }

    // construct the encode and pass to the member variables.
    code_array = s;
}

std::string Encrypt::get_code_array() {
    return code_array;
}
