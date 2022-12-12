# include <stdio.h>
# include <stdlib.h>
# include <string.h>

struct BSTree_node{
    char name[32];
    int phone;
    int no;
    struct BSTree_node* left;
    struct BSTree_node* right;
};
typedef struct BSTree_node node;

void print_preorder(node* ptr){
    if(ptr!=NULL){
        printf("Name: %s\n", ptr->name);
        printf("Phone: %d\n", ptr->phone);
        printf("NO: %d\n", ptr->no);
        printf("\n");
        print_preorder(ptr->left);
        print_preorder(ptr->right);
    }
}

void print_postorder(node* ptr){
    if(ptr!=NULL){
        print_postorder(ptr->left);
        print_postorder(ptr->right);
        printf("Name: %s\n", ptr->name);
        printf("Phone: %d\n", ptr->phone);
        printf("NO: %d\n", ptr->no);
        printf("\n");
    }
}

void print_inorder(node* ptr){
    if(ptr!=NULL){
        print_inorder(ptr->left);
        printf("Name: %s\n", ptr->name);
        printf("Phone: %d\n", ptr->phone);
        printf("NO: %d\n", ptr->no);
        printf("\n");
        print_inorder(ptr->right);
    }
}

node* insert_node(node* root, char name[], int phone, int no){
    node* new_node, *current, *parent;
    new_node = (node*)malloc(sizeof(node));
    strcpy(new_node->name, name);
    new_node->phone = phone;
    new_node->no = no;
    new_node->left = NULL;
    new_node->right = NULL;

    if(root == NULL){
        root = new_node;
    }else{
        current = root;
        while(current != NULL){
            parent = current;
            if(strcmp(current->name, name) > 0){
                current = current->left;
            }else{
                current = current->right;
            }
        }
        if(strcmp(parent->name, name) > 0){
            parent->left = new_node;
        }else{
            parent->right = new_node;
        }
    }

    return root;
}

node* find_node(node* ptr, char name[]){
    if(ptr!=NULL){
        if(strcmp(ptr->name, name) == 0){
            return ptr;
        }else{
            if(strcmp(ptr->name, name) > 0){
                return find_node(ptr->left, name);
            }else{
                return find_node(ptr->right, name);
            }
        }
    }
    return NULL;
}

// 找某值之父節點
node *find_parent(node *ptr, char name[], int *pos)
{
	node *parent;

	parent = ptr;	// 從ptr開始找
	*pos = 0;
	while(ptr != NULL)	
	{
		if(strcmp(ptr->name, name) == 0)	// 找到目標
			return parent;		// 回傳此節點之父節點
		else
		{
			parent = ptr;
			if(strcmp(ptr->name, name) > 0)
			{
				*pos = -1;			// ptr在parent左子樹
				ptr = ptr->left;	// 往左找
			}
			else
			{
				*pos = 1;			// ptr在parent右子樹
				ptr = ptr->right;	// 往右找
			}
		}
	}
	return NULL;	// 找不到
}

// 刪除節點
node *delete_node(node *root, char name[])
{
	node *parent;
	node *ptr;
	node *next;
	int pos;

	parent = find_parent(root, name, &pos);	// 從root開始,找value之父節點
	if(parent != NULL)	// 有找到, 準備刪除
	{
		switch(pos)	// 判斷目前節點再父節點左邊或右邊
		{
			case -1:
				ptr = parent->left;
				break;
			case 1:
				ptr = parent->right;
				break;
			case 0:
				ptr = parent;
				break;
		}
		if(ptr->left == NULL)		// 情況1: 節點沒有左子樹 如果要刪的是根節點
		{
			if(parent == ptr)	// 如果要刪的是根節點
				root = root->right;
			else				// 其他
			{
				if( pos == 1 )
				{
					//要刪除的節點在父節點右方,所以將父節點的右節點指向刪除節點的右節點
					parent->right = ptr->right;
				}
				else
				{
					//要刪除的節點在父節點左方,所以將父節點的左節點指向刪除節點的右節點
					parent->left = ptr->right;
				}
			}
			free(ptr);
		}
		else if(ptr->right == NULL)	// 情況2: 節點沒有右子樹
		{
			if(parent != ptr)
			{
				if( pos == 1 )
				{
					//要刪除的節點在父節點右方,所以將父節點的右節點指向刪除節點的左節點
					parent->right = ptr->left;
				}
				else
				{
					//要刪除的節點在父節點左方,所以將父節點的左節點指向刪除節點的左節點
					parent->left = ptr->left;
				}
			}
			else
				root = root->left;
			free(ptr);
		}
		else						// 情況3: 節點有左右子樹
		{
			parent = ptr;
			next = ptr->left;	// 找取代點next, 從ptr左邊開始找
            if(next->right!=NULL){
                while(next->right!=NULL){  // 往左子節點之右子樹找最大值當取代點
                    parent = next;   // parent為next之父節點
                    next = next->right;
                }
                parent->right = next->left;
            }else{
                parent->left = next->left;
            }
			strcpy(ptr->name, next->name);		// 取代!!
            ptr->phone = next->phone;
            ptr->no = next->no;
			free(next);	// 刪除next (注意: 不是刪除ptr)
		}
	}else{
        return NULL;
    }
	return root;	// 回傳此樹
}

node *find_parent_no(node *ptr, int no, int *pos, node *out_parent)
{
	node *parent, *res;

	parent = ptr;	// 從ptr開始找
	*pos = 0;

    if(ptr!=NULL){
        if(ptr->no == no){
            return ptr;
        }else{
            parent = ptr;
            ptr = ptr->left;
            res = find_parent_no(ptr, no, pos, out_parent);
            if(res!=NULL && out_parent==NULL){
                *pos = -1;
                return parent;
            }
            ptr = parent->right;
            res = find_parent_no(ptr, no, pos, out_parent);
            if(res!=NULL && out_parent == NULL){
                *pos = 1;
                return parent;
            }
        }
    }

	return NULL;	// 找不到
}

// 刪除節點
node *delete_node_no(node *root, int no)
{
	node *parent = NULL;
	node *ptr;
	node *next;
	int pos = 0;

	parent = find_parent_no(root, no, &pos, parent);	// 從root開始,找value之父節點
	if(parent != NULL)	// 有找到, 準備刪除
	{
		switch(pos)	// 判斷目前節點再父節點左邊或右邊
		{
			case -1:
				ptr = parent->left;
				break;
			case 1:
				ptr = parent->right;
				break;
			case 0:
				ptr = parent;
				break;
		}
		if(ptr->left == NULL)		// 情況1: 節點沒有左子樹 如果要刪的是根節點
		{
			if(parent == ptr)	// 如果要刪的是根節點
				root = root->right;
			else				// 其他
			{
				if( pos == 1 )
				{
					//要刪除的節點在父節點右方,所以將父節點的右節點指向刪除節點的右節點
					parent->right = ptr->right;
				}
				else
				{
					//要刪除的節點在父節點左方,所以將父節點的左節點指向刪除節點的右節點
					parent->left = ptr->right;
				}
			}
			free(ptr);
		}
		else if(ptr->right == NULL)	// 情況2: 節點沒有右子樹
		{
			if(parent != ptr)
			{
				if( pos == 1 )
				{
					//要刪除的節點在父節點右方,所以將父節點的右節點指向刪除節點的左節點
					parent->right = ptr->left;
				}
				else
				{
					//要刪除的節點在父節點左方,所以將父節點的左節點指向刪除節點的左節點
					parent->left = ptr->left;
				}
			}
			else
				root = root->left;
			free(ptr);
		}
		else						// 情況3: 節點有左右子樹
		{
			parent = ptr;
			next = ptr->left;	// 找取代點next, 從ptr左邊開始找
            if(next->right!=NULL){
                while(next->right!=NULL){  // 往左子節點之右子樹找最大值當取代點
                    parent = next;   // parent為next之父節點
                    next = next->right;
                }
                parent->right = next->left;
            }else{
                parent->left = next->left;
            }
			strcpy(ptr->name, next->name);		// 取代!!
            ptr->phone = next->phone;
            ptr->no = next->no;
			free(next);	// 刪除next (注意: 不是刪除ptr)
		}
	}else{
        return NULL;
    }
	return root;	// 回傳此樹
}

int main(){

    node* root, *res;
    root = NULL;
    char op;
    char input_name[32];
    int input_phone;
    int input_no;
    int ct = 0;


    while(1){
        scanf("%c", &op);
        switch(op){
            case 'i':
                scanf("%s", input_name);
                scanf("%d", &input_phone);
                root = insert_node(root, input_name, input_phone, ct);
                ct++;
                break;

            case 'd':
                scanf("%s", input_name);
                res = delete_node(root, input_name);
                if(res!=NULL){
                    root = res;
                    printf("delete %s ok\n", input_name);
                    printf("\n");
                }else{
                    printf("cannot delete\n");
                }
                break;

            case 'r':
                scanf("%d", &input_no);
                res = delete_node_no(root, input_no);
                if(res!=NULL){
                    root = res;
                    printf("delete %d ok\n", input_no);
                    printf("\n");
                }else{
                    printf("cannot delete\n");
                }
                break;
            
            case 'm':
                print_preorder(root);
                break;

            case 'l':
                print_inorder(root);
                break;

            case 'n':
                print_postorder(root);
                break;

            case 'f':
                scanf("%s", input_name);
                res = find_node(root, input_name);
                if(res == NULL){
                    printf("not found\n");
                }else{
                    printf("found:\n");
                    printf("Name: %s\n", res->name);
                    printf("Phone: %d\n", res->phone);
                    printf("\n");
                }
                break;

            case 'q':
                return 0;

        }
    }

    return 0;
}