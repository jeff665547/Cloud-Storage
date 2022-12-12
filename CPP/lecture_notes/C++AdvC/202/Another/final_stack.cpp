# include <stdio.h>
# include <stdlib.h>

struct stack_node{
    int data1;
    int data2;
    struct stack_node* next;
};
typedef struct stack_node node;

node* stack = NULL;

void push(int input1, int input2){
    node* new_node;
    new_node = (node*)malloc(sizeof(node));
    if(new_node == NULL){
        printf("run out of memory.\n");
        return;
    }
    
}

int main(){



    return 0;
}