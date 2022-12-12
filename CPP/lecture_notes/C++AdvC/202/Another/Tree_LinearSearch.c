# include <stdio.h>
# include <stdlib.h>

struct Binary_tree_node{
    int data;
    struct Binary_tree_node* left;
    struct Binary_tree_node* right;
};
typedef struct Binary_tree_node node;

node* search_node(node* ptr, int value){
    node* tmp = NULL;

    if(ptr!=NULL){
        printf("%d ", ptr->data);
        if(ptr->data == value){
            return ptr;
        }else{
            tmp = search_node(ptr->left, value);
            if(tmp != NULL){
                return tmp;
            }
            tmp = search_node(ptr->right, value);
            if(tmp != NULL){
                return tmp;
            }
        }
    }
    return tmp;
}

void releasenode(node* ptr){
    if(ptr!=NULL){
        releasenode(ptr->left);
        releasenode(ptr->right);
        free(ptr);
    }
}

int main(){

    node* root;
    root = (node*)malloc(sizeof(node));
    root->data = 5;
    root->left = (node*)malloc(sizeof(node));
    root->right = (node*)malloc(sizeof(node));

    root->left->data = 4;
    root->left->left = (node*)malloc(sizeof(node));
    root->left->right = NULL;
    root->left->left->data = 2;
    root->left->left->left = (node*)malloc(sizeof(node));
    root->left->left->left->data = 1;
    root->left->left->left->left = NULL;
    root->left->left->left->right = NULL;
    root->left->left->right = (node*)malloc(sizeof(node));
    root->left->left->right->data = 3;
    root->left->left->right->left = NULL;
    root->left->left->right->right = NULL;

    root->right->data = 6;
    root->right->left = NULL;
    root->right->right = (node*)malloc(sizeof(node));
    root->right->right->data = 8;
    root->right->right->left = (node*)malloc(sizeof(node));
    root->right->right->left->data = 7;
    root->right->right->left->left = NULL;
    root->right->right->left->right = NULL;
    root->right->right->right = (node*)malloc(sizeof(node));
    root->right->right->right->data = 9;
    root->right->right->right->left = NULL;
    root->right->right->right->right = NULL;

    int input;
    scanf("%d", &input);

    node* res;
    res = search_node(root, input);
    if(res!=NULL){
        printf("\nfound %d", res->data);
    }else{
        printf("\nnot found");
    }

    releasenode(root);

    return 0;
}