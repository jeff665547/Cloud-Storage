# include <stdio.h>
# include <stdlib.h>

struct linked_node node{
    int data1;
    int data2;
    struct linked_node_next;
};
typedef struct linked_node node;

node* stack = NULL;
node* top = NULL;

void push(node* input){
    node* new_node = (node*)malloc(sizeof(node));
    if(new_node == NULL){
        printf("Run out of memory.\n");
    }
    new_node = input;
    if(top == NULL){
        stack = new_node;
        top = new_node;

    }else{

    }
}

void pop(){

}

int main(){


    
    return 0;
}