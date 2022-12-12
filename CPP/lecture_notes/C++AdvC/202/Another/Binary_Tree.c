# include <stdio.h>
# include <stdlib.h>

struct Binary_tree_node{
    int data;
    struct Binary_tree_node* left;
    struct Binary_tree_node* right;
};
typedef struct Binary_tree_node node;

void print_inorder(node* ptr){
    if(ptr != NULL){
        print_inorder(ptr->left);
        printf("[%2d]\n", ptr->data);
        print_inorder(ptr->right);
    }
}

void print_preorder(node* ptr){
    if(ptr != NULL){
        printf("[%2d]\n", ptr->data);
        print_preorder(ptr->left);
        print_preorder(ptr->right);
    }
}

void print_postorder(node* ptr){
    if(ptr != NULL){
        print_postorder(ptr->left);
        print_postorder(ptr->right);
        printf("[%2d]\n", ptr->data);
    }
}

int main(){

    // Level 1
    node* root;
    root = (node*)malloc(sizeof(node));
    root->data = 5;
    root->left = NULL;
    root->right = NULL;


    // Level 2
    root->left = (node*)malloc(sizeof(node));
    root->left->data = 4;
    root->left->left = NULL;
    root->left->right = NULL;

    root->right = (node*)malloc(sizeof(node));
    root->right->data = 6;
    root->right->left = NULL;
    root->right->right = NULL;

    print_inorder(root);
    printf("\n");
    print_preorder(root);
    printf("\n");
    print_postorder(root);

    return 0;
}