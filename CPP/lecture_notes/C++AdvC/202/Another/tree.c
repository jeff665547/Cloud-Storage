# include <stdio.h>
# include <stdlib.h>

struct binary_tree_node{
    int data;
    struct binary_tree_node* left;
    struct binary_tree_node* right;
};
typedef struct binary_tree_node node;

int main(){

    node* root;
    root = (node*)malloc(sizeof(node));
    root->data = 10;
    root->left = NULL;
    root->right = NULL;    

    return 0;
}