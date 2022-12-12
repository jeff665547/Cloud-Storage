# include <stdio.h>
# include <stdlib.h>
struct BSTree_node{
    int data;
    struct BSTree_node* left;
    struct BSTree_node* right;
};
typedef struct BSTree_node node;

void print_preorder(node* ptr){
    if(ptr!=NULL){
        printf("%d ", ptr->data);
        print_preorder(ptr->left);
        print_preorder(ptr->right);
    }
}

void print_inorder(node* ptr){
    if(ptr!=NULL){
        print_inorder(ptr->left);
        printf("%d ", ptr->data);
        print_inorder(ptr->right);
    }
}

void print_postorder(node* ptr){
    if(ptr!=NULL){
        print_postorder(ptr->left);
        print_postorder(ptr->right);
        printf("%d ", ptr->data);
    }
}

void release_node(node* ptr){
    if(ptr != NULL){
        release_node(ptr->left);
        release_node(ptr->right);
        free(ptr);
    }
}

node* insert_node(node* root, int value){
    node* new_node;
    node* current;
    node* parent;

    new_node = (node*)malloc(sizeof(node));
    new_node->data = value;
    new_node->left = NULL;
    new_node->right = NULL;

    if(root == NULL){
        root = new_node; // 
    }else{
        current = root;
        while(current != NULL){
            parent = current;
            if(current->data > value){
                current = current->left;
            }else{
                current = current->right;
            }
        }
        if(parent->data > value){
            parent->left = new_node;
        }else{
            parent->right = new_node;
        }
    }
    return root;
}

node* find_node(node*ptr, int value){
    while(ptr!=NULL){
        if(ptr->data == value){
            return ptr;
        }else{
            if(ptr->data > value){
                ptr = ptr->left;
            }else{
                ptr = ptr->right;
            }
        }
    }
    return NULL;
}

int main(){

    int value;
    char op;
    node* tree;
    tree = NULL;

    while(1){
        scanf("%c", &op);
        switch(op){
            case 'i':
                scanf("%d", &value);
                tree = insert_node(tree, value);
                break;
            case 'l':
                print_inorder(tree);
                printf("\n");
                break;
            case 'm':
                print_preorder(tree);
                printf("\n");
                break;
            case 'n':
                print_postorder(tree);
                printf("\n");
                break;
            case 'q':
                release_node(tree);
                return 0;
        }
    }

    return 0;
}