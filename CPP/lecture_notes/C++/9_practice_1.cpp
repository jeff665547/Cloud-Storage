# include <iostream>
# include "9_practice_1.h"

Square::Square(){
    len = 0;
}

Square::Square(int ll){
    len = ll;
}

int Square::area(){
 
    int area  = len*len;
 
    return area;
}

void Square::setLen(int n){
    len = n;
}

int Square::getLen(){
    return len;
}

