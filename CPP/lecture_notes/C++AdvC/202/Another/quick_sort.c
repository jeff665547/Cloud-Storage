#include <stdio.h>
#include <stdlib.h>

#define N 6

void swap(int *a, int *b)
{
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;
}
void print(int n, int *p)
{
    int i;

    for(i=0; i<n; i++)
    {
        printf("%d ", p[i]);
    }
    printf("\n");
}

void QuickSort(int *numbers, int low, int high)  // Quick Sort 由小排到大
{   
    int a, b, pivot;
    
    a = low+1;    // a從左邊開始找
    b = high;       // b從右邊開始找
    pivot = numbers[low]; // 基準值預設為第一個
    do{
        while(numbers[a] < pivot && a<high) // a向右找，找到比基準值大的才停下來
            a++;
        while(numbers[b] > pivot && b>=0) // b向左找，找到比基準值小的才停下來 
            b--;
        if(a < b)
            swap(&numbers[a], &numbers[b]);
    }while(a < b);               
    numbers[low] = numbers[b];     // 把基準值擺到中間 
    numbers[b] = pivot;                  // 兩者交換後，把數列切成兩半 
  
    if((b-1) > low)
        QuickSort(numbers, low, b-1);     // 小的那一半繼續做QuickSort 
    if((b+1) < high)
        QuickSort(numbers, b+1, high);   // 大的那一半繼續做QuickSort
}

int main(){

    int ary[] = {5,1,6,4,8,7};
    QuickSort(ary, 0, 6-1);
  
    print(6, ary);

    return 0;
}