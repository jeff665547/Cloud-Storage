# include <iostream>

class linkedlist_node{
    friend class linkedlist;
  private:
    int data;
    class linkedlist_node* next;
};
typedef class linkedlist_node node;

class linkedlist{
  public:
    linkedlist();
    node* find_node(int value);
    void print_list();
    void insert_last(int value);
    void delete_value(int value);

  protected:
    void insert_node(node* ptr, int value);
    void delete_node(node* ptr);
    node* head;
    node* tail;
};

linkedlist::linkedlist(){
    head = NULL;
    tail = NULL;
}

void linkedlist::insert_node(node* ptr, int value){
    node* new_node;
    new_node = new node;
    if(new_node==NULL){
        std::cout << "Run out of memory." << std::endl;
        return;
    }
    new_node->data = value;
    new_node->next = NULL;

    if(head == NULL){
        head = new_node;
        tail = new_node;
        return;
    }

    if(ptr == NULL){
        new_node->next = head;
        head = new_node;
    }else{
        if(ptr->next == NULL){
            tail->next = new_node;
            tail = new_node;
        }else{
            new_node->next = ptr->next;
            ptr->next = new_node;
        }
    }

    return;
}

void linkedlist::delete_node(node* ptr){
    node *parent, *cur;

    if(head == NULL){
        std::cout << "cannot delete" << std::endl;
        return;
    }

    cur = head;
    while(cur!=NULL){
        if(cur == ptr){
            break;
        }
        parent = cur;
        cur = cur->next;
    }

    if(ptr == head){
        head = head->next;
        if(head == NULL){
            tail = NULL;
        }
        delete ptr;
    }else{
        if(ptr->next == NULL){
            parent->next = ptr->next;
            tail = parent;
            delete ptr;
        }else{
            parent->next = ptr->next;
            delete ptr;
        }
    }
}

node* linkedlist::find_node(int value){
    node* ptr;
    ptr = head;
    while(ptr!=NULL){
        if(ptr->data == value){
            return ptr;
        }
        ptr = ptr->next;
    }
    return NULL;
}

void linkedlist::print_list(){
    node* ptr;
    ptr = head;
    while(ptr!=NULL){
        std::cout << ptr->data << std::endl;
        ptr = ptr->next;
    }
    return;
}

void linkedlist::insert_last(int value){
    insert_node(tail, value);
}

void linkedlist::delete_value(int value){
    node* res;
    res = find_node(value);
    delete_node(res);
}

int main(){

    linkedlist l1;
    l1.insert_last(1);
    l1.insert_last(3);
    l1.insert_last(5);
    l1.insert_last(7);

    l1.print_list();

    l1.delete_value(5);
    l1.print_list();
    l1.delete_value(1);
    l1.print_list();
    l1.delete_value(7);
    l1.print_list();

    return 0;
}