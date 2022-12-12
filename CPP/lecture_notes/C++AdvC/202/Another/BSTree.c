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
        printf("%d", ptr->data);
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
        printf("%d", ptr->data);
    }
}

node* insert_node(node* root, int value){
    node *new_node, *current, *parent;
    new_node = (node*)malloc(sizeof(node));
    new_node->data = value;
    new_node->left = NULL;
    new_node->right = NULL;

    if(root == NULL){
        root = new_node;
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

node* find_node(node* ptr, int value){
    if(ptr!=NULL){
        printf("%d ", ptr->data);
        if(ptr->data == value){
            return ptr;
        }else{
            if(ptr->data > value){
                ptr = ptr->left;
                return find_node(ptr, value);
            }else{
                ptr = ptr->right;
                return find_node(ptr, value);
            }
        }
    }
    printf("Not found.\n");
    return NULL;
}

int main(){

    node *root, *ptr;
    root = NULL;
    char op;
    int input;

    while(1){
        scanf("%c", &op);
        switch(op){
            case 'i':
                scanf("%d", &input);
                root = insert_node(root, input);
                break;

            case 'f':
                scanf("%d", &input);
                ptr = find_node(root, input);
                if(ptr!=NULL){
                    printf("found: %d\n", ptr->data);
                }
                break;

            case 'l':
                print_inorder(root);
                printf("\n");
                break;

            case 'q':
                return 0;
        }
    }

    return 0;
}
