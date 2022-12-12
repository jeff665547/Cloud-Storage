# include <stdio.h>

void print(int n){
    if(n <= 1){
        printf("%d\n", n);
    }else{
        print(n - 1);
        printf("%d\n", n);
    }
}

int Fib(int n){
    // 0, 1, 1, 2, 3, 5, 8, ...
    if(n == 1){
        return 0;
    }else if(n <= 3){
        return 1;
    }else{
        return(Fib(n-1) + Fib(n-2));
    }
}

int main(){

    // print(10);
    printf("%d", Fib(1));
    printf("%d", Fib(2));
    printf("%d", Fib(3));
    printf("%d", Fib(4));
    printf("%d", Fib(5));
    printf("%d", Fib(6));
    

    return 0;
}