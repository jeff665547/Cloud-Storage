# include <stdio.h>
# include <stdlib.h>

struct node{
    int data;
    char prime;
    struct node* next;
    struct node* prev;
};
typedef struct node node;

node* insert_node(node* root, node* ptr, node* new){
    if(root == NULL){
        root = new;
        ptr = root;
    }else{
        if(ptr->next!=NULL){

            new->prev = ptr; 
            ptr->next->prev = new;
            new->next = ptr->next;
            ptr->next = new;
            ptr = ptr->next;
        }else{

            new->prev = ptr;
            ptr->next = new;
            ptr = ptr->next;
        }
    }
    return ptr;
}

void normal_print_list(node* ptr){
    while(ptr!=NULL){
        printf("%d %c\n", ptr->data, ptr->prime);
        ptr = ptr->next;
    }
}

void inverse_print_list(node* ptr){
    while(ptr!=NULL){
        printf("%d %c\n", ptr->data, ptr->prime);
        ptr = ptr->prev;
    }
}

node* get_tail(node* ptr){
    while(ptr->next!=NULL){
        ptr = ptr->next;
    }
    return ptr;
}

char is_prime(int num){
    int i;

    if(num == 0 || num == 1){
        return 'N';
    }else if(num == 2){
        return 'P';
    }else{
        for(i = 2; i < num/2; i++){
            if(num%i == 0){
                return 'N';
            }
        }
    }
    return 'P';
}

node* print_factors(int num){

    int i;
    int ct = 0;
    node* root = NULL;
    node* ptr = root;
    node* new_node;

    for(i = 1; i <= num; i++){

        if((num%i)==0){
            ct += 1;
            printf("%d ", i);

            new_node = (node*)malloc(sizeof(node));
            new_node->data = i;
            new_node->next = NULL;
            new_node->prev = NULL;
            new_node->prime = is_prime(i);

            ptr = insert_node(root, ptr, new_node);
            if(ct==1){
                root = ptr;
            }
        }
    }
    printf("\n");
    printf("\n");

    return root;
}

int main(){

    int op, input;
    node* root;
    
    printf("n: ");
    scanf("%d", &input);
    printf("factors: ");
    root = print_factors(input);
    node* tail = get_tail(root);

    while(1){
        printf("Operation: ");
        scanf("%d", &op);
        switch(op){
            case 1:
            normal_print_list(root);
            printf("\n");
            break;

            case 2:
            inverse_print_list(tail);
            printf("\n");
            break;

            case 3:
            printf("Program exit.\n");
            return 0;
        }

    }
    

    return 0;
}