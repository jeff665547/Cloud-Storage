# include <iostream>

class linkedlistnode{
    friend class linkedList;
    friend class stack;
  private:
    int data;
    class linkedlistnode* next;
};
typedef class linkedlistnode node;

class linkedList{
  public:
    linkedList();
    void insert_last(int value);
    void delete_node(int value);
    node* find_node(int value);
    void print_list();

  protected:
    node* head;
    node* tail;
    void insert_node(node* ptr, int value);
};

linkedList::linkedList(){
    head = NULL;
    tail = NULL;
}

void linkedList::insert_node(node* ptr, int value){
    node* new_node;
    new_node = new node;
    if(new_node == NULL){
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
    }else if(ptr->next == NULL){
        ptr->next = new_node;
        tail = new_node;
    }else{
        new_node->next = ptr->next;
    }
    return;
}

void linkedList::insert_last(int value){
    insert_node(tail, value);
}

void linkedList::delete_node(int value){
    node* parent, *ptr;
    ptr = head;
    parent = ptr;
    
    if(ptr==NULL){
        std::cout << "cannot delete" << std::endl;
        return;
    }

    while(ptr!=NULL){
        if(ptr->data == value){
            break;
        }
        parent = ptr;
        ptr = ptr->next;
    }

    if(ptr == head){
        head = ptr->next;
        if(head == NULL){
            tail = NULL;
        }
        delete ptr;
    }else{
        if(ptr == tail){
            tail = parent;
            parent->next = ptr->next;
            delete ptr;
        }else{
            parent->next = ptr->next;
            delete ptr;
        }
    }
    return;
}

node* linkedList::find_node(int value){
    node* ptr;
    ptr = head;
    while(ptr!=NULL){
        if(ptr->data == value){
            return ptr;
        }else{
            ptr = ptr->next;
        }
    }
    return NULL;
}

void linkedList::print_list(){
    node* ptr;
    ptr = head;
    while(ptr!=NULL){
        std::cout << ptr->data << std::endl;
        ptr = ptr->next;
    }
    return;
}

class stack : public linkedList{
  public:
    void push(int value);
    int pop();
};

void stack::push(int value){
    insert_node(NULL, value);
    return;
}

int stack::pop(){
    if(head!=NULL){
        int tmp;
        tmp = head->data;
        delete_node(tmp);
        return tmp;
    }
    return -1;
}

int main(){

    stack st;
    
    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);

    st.print_list();
        
    std::cout << st.pop() <<" ";
    std::cout << st.pop() <<" ";
    std::cout << st.pop() <<" ";
    std::cout << st.pop() <<" ";    

    return 0;
}