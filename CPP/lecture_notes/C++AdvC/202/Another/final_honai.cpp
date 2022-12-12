# include <cstdio>
# include <cstdlib>
# include <iostream>
# include <cstring>

class tower{
  public:
    char name;
    int *stack;
    int max;
    int top = -1;
    int push(int value);
    int pop();
    void print();
};
typedef class tower tower;

int tower::push(int value)
{
	
    if( top == max-1 )
	{
		return -1;
	}
	top++;

	stack[top] = value;
	return 1;
}

int tower::pop()
{
	int temp;

	if( top == -1 ) //判斷堆疊是否為空的
	{
		return -1;
	}
	temp = stack[top];
	stack[top] = 0;
	top--;
	return temp;
}

void tower::print(){
    printf("Tower %c:  ", name);
    int i = 0;
    for(i = 0; i < max; i++){
        printf("%d ", stack[i]);
    }
    printf("\n");
}

void print_order(tower *all, int n){
    int i, j;
    for(i = n; i > 1; i--){
        for(j = 0; j < i-1; j++){
            if(all[j].name > all[j+1].name){
                tower tmp;
                tmp = all[j];
                all[j] = all[j+1];
                all[j+1] = tmp;
            }
        }
    }
    for(i = 0; i < n; i++){
        all[i].print();
    }
    printf("\n");
}

void Honai(tower *start, tower *dst, tower *tmp, int n, int ct){
    
    ct++;
    
    if(n == 1){
        printf("plate %d from tower %c -> tower %c\n", n, start->name, dst->name);
        start->pop();
        dst->push(n);
        tower tmp_all[3] = {*start, *dst, *tmp};
        print_order(tmp_all, 3);

    }else{
        Honai(start, tmp, dst, n-1, ct);
        printf("plate %d from tower %c -> tower %c\n", n, start->name, dst->name);
        start->pop();
        dst->push(n);
        tower tmp_all[3] = {*start, *dst, *tmp};
        print_order(tmp_all, 3);

        Honai(tmp, dst, start, n-1, ct);
    }
}

int main(){


    std::cout << "<< Honai Tower 2.0 >>" << std::endl << std::endl;
    std::cout << "Input the number of plate: ";
    int num;
    scanf("%d", &num);

    tower A;
    tower B;
    tower C;
    A.stack = (int*)malloc(num*sizeof(int));
    B.stack = (int*)malloc(num*sizeof(int));
    C.stack = (int*)malloc(num*sizeof(int));
    A.name = 'A';
    B.name = 'B';
    C.name = 'C';
    A.max = num;
    B.max = num;
    C.max = num;
    A.top = num - 1;
    for(int i = num; i > 0; i--){
        A.stack[num - i] = i;
        B.stack[num - i] = 0;
        C.stack[num - i] = 0;
    }
    A.print();
    B.print();
    C.print();
    printf("\n");

    Honai(&A, &C, &B, num, 0);
    
    return 0;
}