# include <iostream>
# include <vector>

class Screen{
    public:

        // Member function definitions are processed after the compiler processed all of the declarations in the class.
        // In other words, member function bodies are not processed until the entire class is seen.
        friend class Window_mgr;

        // Define a type member.
        typedef std::string::size_type pos;

        Screen() = default;  // It is needed since Screen has another constructor.
        
        // cursor initialized to 0 by its in-class initializer.
        Screen(pos ht, pos wd, char c) : height(ht), width(wd), contents(ht * wd, c) { }
        
        char get() const { return contents[cursor]; }  // implicitly inline. 
                                                       // (inline by defaults: member functions defined inside the class are automatically inline.)
        inline char get(pos ht, pos wd) const;         // explicitly inline.
        Screen &move(pos r, pos c);                    // can be made inline later.

        void some_member() const;

        // Functions to set the character at the cursor or at a given location
        Screen &set(char);
        Screen &set(pos, pos, char);

        // Display overloaded on whether the object is const or not
        Screen &display(std::ostream &os){
            do_display(os); // Its own this pointer is implicitly passed to do_display. 
            return *this;  // return a nonconst reference
        }
        const Screen &display(std::ostream &os) const {
            do_display(os); // Its own this pointer is implicitly passed to do_display.
            return *this;   // return a const reference.
        }

    private:
        pos cursor = 0;
        pos height = 0, width = 0;
        std::string contents;

        mutable size_t access_ctr;  // may change even in a const object

        // Overloading based on const
        // function to do the work of displaying a Screen.
        void do_display(std::ostream &os) const {os << contents;}
};

class Window_mgr{
  public:
    // location ID for each screen on the window. (Define a type member.)
    using ScreenIndex = std::vector<Screen>::size_type;
    void clear(ScreenIndex);

    // Add a Screen to the window and returns its index.
    ScreenIndex addScreen(const Screen&);

  private:
    // Screens this Window_mgr is tracking by default, a Window_mgr has one standard sized blank Screen
    std::vector<Screen> screens{Screen(24, 80, ' ')};
};

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

// Since the complier sees the parameter list after noting that we are in the scope
// of class WindowMgr, there is no need to specify that we want the ScreenIndex that is defined
// by Window_mgr.
void Window_mgr::clear(ScreenIndex i){
    // s is a reference to the Screen we want to clear.
    Screen &s = screens[i];
    // reset the contents of that Screen to all blanks.
    s.contents = std::string(s.height * s.width, ' ');
}

Window_mgr::ScreenIndex // this line is the return type of the function below 
// (the return type is seen before we're in the scope (start from the next line) of Window_mgr).
Window_mgr::addScreen(const Screen &s){
    screens.push_back(s);
    return screens.size() - 1;
}

// Names are resolved where they appear within a file.
int height;
class Screen2{
  public:
    typedef std::string::size_type pos;
    void setHeight(pos);
    pos height = 0;     // this line hides the declaration of height in the outer scope.
};
Screen2::pos verify(Screen2::pos);
void Screen2::setHeight(pos var){
    height = verify(var); 
    // Here,
    // var: refers to the parameter, 
    // height: refers to the class member,
    // verify: refers to the golbal function
}


int main(){
    Screen::pos ht = 24, wd = 80;  // use the pos type defined by Screen.
    Screen scr(ht, wd, ' ');
    Screen *p = &scr;
    char c = scr.get();  // fetches the get member from the object scr
    c = p->get();        // fetches the get member from the object to which p points.
    return 0;
}