# include <stdio.h>
# include <stdlib.h>

void Honai(char start, char dst, char tmp, int n, int *ct){
    if(n == 1){
        printf("plate %d from %c -> %c\n", n, start, dst);
        ct[n - 1]++;
    }else{
        Honai(start, tmp, dst, n-1, ct);
        printf("plate %d from %c -> %c\n", n, start, dst);
        ct[n - 1]++;
        Honai(tmp, dst, start, n-1, ct);
    }
}

int main(){

    int num;
    scanf("%d", &num);
    int *plate;
    plate = (int*)malloc(num*sizeof(int));
    for(int i = 0; i < num; i++){
        plate[i] = 0;
    }
    Honai('A', 'C', 'B', num, plate);
    printf("\n");
    for(int i = 0; i < num; i++){
        printf("plate %d = %d\n", i + 1, plate[i]);
    }
    free(plate);

    return 0;
}