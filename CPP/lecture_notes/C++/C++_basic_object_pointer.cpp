#include <iostream>
#include "SafeArray.h"
using namespace std;

int main() {
    SafeArray *safeArray = new SafeArray(10);
 
    for(int i = 0; i < safeArray->length; i++) {
        safeArray->set(i, (i + 1) * 10);
    }
 
    for(int i = 0; i < safeArray->length; i++) {
        cout << safeArray->get(i) << " ";
    }
    cout << endl;
 
    delete safeArray;
 
    return 0; 
}
