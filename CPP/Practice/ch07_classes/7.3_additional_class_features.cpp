# include <iostream>
# include <vector>

class Screen{
    public:

        // Friendship between classes
        // * Window_mgr members can access the private parts of class Screen.
        // * this kind of friendship is not transitive. That is if class Window_mgr has its own friends,
        //   those friends have no special access to Screen.
        // * Simplify to say, each class controls which classes or functions are its friends.
        friend class Window_mgr;

        // Making a member function a friend
        // * Making the entire Window_mgr class a friend, Screen can instead specify that only the clear member is allowed access.
        // friend void Window_mgr::clear(ScreenIndex);
        // * Using this format requires carefully structuring the program, we must order the program as follows:
        // 1. define the "Window_mgr" class, which declares "clear", but cannot define "clear".
        //    "Screen" class must be declared before "clear" can use the members of "Screen" class.
        // 2. define class Screen, including a friend declaration for clear.
        // 3. define clear, which can now refer to the members in "Screen" class
        // * A friend declaration cannot be considered to be a general formal declaration of that function, 
        //   it only affects the access right (declaration for access).
        //   we still need to provide a declaration outside of the class itself to make that function visible.
        // * In this example "void Window Window_mgr::clear(ScreenIndex);" is not the 
        //   declaration (definition) for the function (clear(ScreenIndex)), it just 
        //   declare the access right (friendship) between that function and the "Screen" class.
        // * Another example:
        //   struct X{
        //        friend void f() { /* friend function can be defined in the class body */} // => this only declare the friendship.
        //        X() { f(); }            // error: no declaration for f.
        //        void g();
        //        void h();
        //   };
        //   void X::g() { return f(); }  // error: f hasn't been declared.
        //   void f();                    // declares the function defined inside X.
        //   void X::h() { return f(); }  // ok: declaration for f is now in the scope.



        // Define a type member.
        typedef std::string::size_type pos;
        // type alias: using pos = std::string::size_type;
        // type members usually appear at the beginning of the class.

        Screen() = default;  // It is needed since Screen has another constructor.
        
        // cursor initialized to 0 by its in-class initializer.
        Screen(pos ht, pos wd, char c) : height(ht), width(wd), contents(ht * wd, c) { }
        
        char get() const { return contents[cursor]; }  // implicitly inline. 
                                                       // (inline by defaults: member functions defined inside the class are automatically inline.)
        // overloading member fucntion
        inline char get(pos ht, pos wd) const;         // explicitly inline.
        Screen &move(pos r, pos c);                    // can be made inline later.
        // A const member function that returns *this as a reference should have a return type that is a reference to const.
        // * Because a class is not defined until its class body is complete, a class cannot
        //   have data members of its own type. However, a class is considered declared (but not
        //   yet defined) as soon as its class name has been seen. Therefore, a class can have
        // data members that are pointers or references to its own type. (Like this example.)


        // Mutable Data Members: member which can always be changed; even if the object is const type (i.e. is never const).
        // It is just opposite to “const”. Sometime we required to use only one or two data member as a variable and other as a constant. 
        // In that situation, mutable is very helpful to manage classes
        // Despite the fact that some_member is a const member function, it can change the value of access_ctr.
        // that member is a mutable member, so any member function, including const functions, can chage its value.
        void some_member() const;

        // Functions to set the character at the cursor or at a given location
        Screen &set(char);
        Screen &set(pos, pos, char);

        // Display overloaded on whether the object is const or not
        Screen &display(std::ostream &os){
            do_display(os); // Its own this pointer is implicitly passed to do_display. 
            // "this" pointer is implictly converted from a pointer to nonconst to a pointer to const.
            return *this;  // return a nonconst reference
        }
        const Screen &display(std::ostream &os) const {
            do_display(os); // Its own this pointer is implicitly passed to do_display.
            return *this;   // return a const reference.
        }
        // A const member function that returns *this as a reference should have a return type that is a reference to const.

    private:
        pos cursor = 0;
        pos height = 0, width = 0;
        std::string contents;

        mutable size_t access_ctr;  // may change even in a const object

        // Overloading based on const
        // function to do the work of displaying a Screen.
        void do_display(std::ostream &os) const {os << contents;}
};


// Initializers for Data Members of class type
class Window_mgr{
  public:
    // location ID for each screen on the window. (Define a type member.)
    using ScreenIndex = std::vector<Screen>::size_type;
    // reset the Screen at the given position to all blanks. (Use the private members in the Screen class.)
    void clear(ScreenIndex);

  private:
    // Screens this Window_mgr is tracking by default, a Window_mgr has one standard sized blank Screen
    std::vector<Screen> screens{Screen(24, 80, ' ')};
    // in-class initializers must use either the = form of initializaiton (which we used when we initialized the data membrs of Screen class.) 
    // or the direct form of initialization using curly braces ({}, as we do for screens). 
};

// specifying inline only on the definition outside the class can make the class easier to read.
inline Screen &Screen::move(pos r, pos c){
    pos row = r * width;  // compute the row location
    cursor = row + c;     // move cursor to the column within that row
    return *this;
}

char Screen::get(pos r, pos c) const // declared as inline in the class
{
    pos row = r * width; // compute the row location
    return contents[row + c];  // return character at the given column.
}

// Mutable data member can be changed even though it is called by the const member function.
void Screen::some_member() const {
    ++access_ctr; // keep a count of the calls to any member function.
}

inline Screen &Screen::set(char c){
    contents[cursor] = c;  // set the new vlaue at the current cursor location
    return *this;          // return this object as an lvalue.
}                          // change the value of the object and return the object reference at the same time.

inline Screen &Screen::set(pos r, pos col, char ch){
    contents[r*width + col] = ch;   // set specified location to given value 
    return *this;                   // return this object as an lvalue.
}                                   // change the value of the object and return the object reference at the same time.

void Window_mgr::clear(ScreenIndex i){
    // s is a reference to the Screen we want to clear.
    Screen &s = screens[i];
    // reset the contents of that Screen to all blanks.
    s.contents = std::string(s.height * s.width, ' ');
}

int main(){

    Screen myscreen;
    char ch = myscreen.get(); // calls Screen::get()
    ch = myscreen.get(0, 0);  // calls Screen::get(pos, pos)

    myscreen.move(4, 0);
    myscreen.set('#');

    std::cout << myscreen.get() << std::endl;

    const Screen blank(5, 3, ' ');
    myscreen.set('#').display(std::cout);  // calls nonconst version
    blank.display(std::cout);         // calls const version

    return 0;
}