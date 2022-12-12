# include <iostream>
# include <array>
# include <string>
# include <list>
# include <deque>
# include <vector>
# include <forward_list>

struct ob{
    int value;
};

int main(){

    /* 9.1 Overview of the Sequential Containers */

    /* array */
    // * fixed-size container. (does not support operations to add and remove elements or to resize the container).
    // * a safer, easier-to-use alternative to built-in arrays.
    // * Like built-in arrays, library arrays have fixed size.

    /* string and vector */
    // * elements are contiguous.
    // * fast to compute the address of an element from its index.
    // * adding or removing elements in the middle of one of these containters takes time. 
    //   (All the elements after the one inserted or removed have to be moved to maintain contiguity.)
    
    /* list (Doublely linked list) and forward_list (Singly linked list) */
    // * fast to add or remove an element any where in the container.
    // * These types do not support random access to elements.
    // * we can only by iterating through the container to access the elements.
    // * the forward_list does not have the size operation since storing or computing its size
    //   would entail overhead compared to a handwritten list.

    /* deque */
    // * deque supports fast random access.
    // * adding elements in the middle of a deque is a expensive operation.
    // * adding or removing elements at either end of the deque (雙端) is a fast operation (comparable to adding an element to a list or forward_list).

    // * Morden C++ programs should use the library containers rather than more primitive structures like arrays.
    // * Ordinaily, it is best to use vector unless there is a good reason to prefer another container.
    // * If you are not sure which container to use, write the code do that it uses only operations common to both vectors and lists: 
    //   (iterators, not subscripts, and avoid random access to elements.) Convenience for changing different containers to use.


    // Few rules of thumb that apply to selecting which container to use:
    // 1. it is best to use vector unless there is a good reason to prefer another container.
    // 2. if your program has lots of small elements and space overhead matters, don't use list or forward_list.
    // 3. if the program requires random access to elements, use a vector or a deque.
    // 4. if the program needs to insert or delete elements in the middle of the container, use a list or forward_list.
    // 5. if the program needs to insert or delete elements at the front and the back, but not in the middle, use a deque.
    // 6. if the program needs to insert elements in the middle of the container only while reading input, and subsequently
    //    needs random access to the elements:
    //    * First, decide whether you actually need to add elements in the middle of a container. It is often easier to append
    //      to a vector and then call the library sort function to reorder the container when you are done with input.
    //    * Second, if you must insert into the middle, consider using a list for the input phase. Once, the input is complete,
    //      copy the list into a vector.







    /* 9.2 Container Library Overview */
    // * The containers are class templates. As with vectors, we must supply additional information to generate a particular container type.
    // * For most, but not all of the containers, the information we must supply is the element type:
    std::list<int> l = {7, 5, 16, 8};  // # include <list>
    // std::list<ob>;  // # include <list>
    // std::deque<double>;  // # include <deque>


    // * we can define a container whose element type is itself another container.
    // * we define such container exactly as we do any other container type
    // * we specify the element type (which in this case is a container type) inside angle brackets:
    std::vector<std::vector<std::string>> lines;     // definition, vector of vectors
    // * Here, lines is a vector whose elements are vectors of strings.
    // * Older compliers may require a space between the angle brackets, for example, std::vector<std::vector<std::string> >.

    // * Some classes do not have a default constructor. We can define a container that holds objects of such types, 
    //   but we cannot construct such containers using only an element count:
    std::vector<int> v1(10);  // ten elements, each initialized to 0.
    // std::vector<noDefault> v1(10, init);  // ok: element initializer supplied.
    // std::vector<int> v2(10);  // error: must supply an element initializer.


    // Standard Container Iterator Operation
    // *iter  Dereference
    // iter->mem  dereferences iter and fetches the member
    // ++iter  refer to the next element in the container.
    // --iter  refer to the previous element in the container. (the forward_list iterators do not support the decrement(--) operator.)
    // iter == iter2  Compares two iterators for equality (inequality). Two iterators are equal if they denote the same element.
    // iter != iter2  

    // Operations Supported by vector, string, deque, and array Iterators.
    // iter + n   Adding (subtracting) an integral value n to (from) an iterator yields 
    // iter - n   an iterator that many elements forward (backward) within the container.
    // iter += n  Compound-assignment for iterator addition and subtraction
    // iter -= n
    // iter1 - iter2  yields the number that when added to the right-hand iterator yields the left-hand iterator.
    // >, >=, <, <=   One iterator is less than another if it refers to an element that appears in the container before the one referred to
    //                by the other iterator.


    // Iterator Ranges (begin and end)
    // * Left-inclusive interval
    // * Mathematical notation for this range is [begin, end). => indicating that the range begins with begin and ends with, but does not include, end.
    // * The iterators begin and end must refer to the same iterator. 
    // * The iterator end may be equal to begin but must not refer to an element before the one denoted by begin. (end must not precede begin.)
    // * If begin equals end, the range is empty.
    // * If begin is not equal to end, there is at least one element in the range, and begin refers to the first element in that range.
    // * We can increment begin some number of times until begin == end.
    // e.g. while(begin != end){  // if begin == end, then the range is empty. If the range is not empty, begin refers to an element in this nonempty range.
    //          *begin = val;  // ok: range is not empty so begin denots an element. 
    //          ++begin;   // advance the iterator to get the next element.
    //      }


    // Container Type Members
    // * type aliases
    std::string st;
    std::getline(std::cin, st);
    auto len = st.size();  // len has type string::size_type

    // To use the following types, we must name the class of which they are a member.
    std::vector<int>::iterator it;  // it can read and write vector<int> elements 
    std::string::iterator it2;    // it2 can read and write characters in a string
    std::vector<int>::const_iterator it3; // it3 can read but not write elements
    std::string::const_iterator it4;  // it4 can read but not write characters.

    std::list<std::string>::iterator iter;  // iter is the iterator type defined by std::list<std::string>.
    std::vector<int>::difference_type count;  // count is the difference_type type defined by std::vector<int>.


    // begin and end Members
    std::list<std::string> a = {"Milton", "Shakespeare", "Austen"};
    auto itt1 = a.begin();  // list<string>::iterator
    auto itt2 = a.rbegin();  // list<string>::reverse_iterator
    auto itt3 = a.cbegin();  // list<string>::const_iterator
    auto itt4 = a.crbegin();  // list<string>::const_reverse_iterator
    // The functions that do not begin with a c are overloaded.
    // That is, there are actually two members named begin. One is a const member that returns the container's const_iterator type.
    // The other is nonconst and returns the container's iterator type.
    // Similarly for rbegin, end, and rend.
    // * When we call one of these members on a nonconst object, we get a version that returns iterator.
    // * We get a const version of the iterators only when we call these function on a const object.
    // * In the past, we had to say which type of iterator we want, but now the c versions (const) were introduced by the new standard to 
    //   support using auto with begin and end functions.
    // * When write access is not needed, use cbegin and cend.
    // type is explicitly specified
    std::list<std::string>::iterator it5 = a.begin();
    std::list<std::string>::const_iterator it6 = a.begin();
    // iterator or const_iterator depending on a's type of a.
    auto it7 = a.begin();   // const_iterator only if a is const.
    auto it8 = a.cbegin();  // it8 is const_iterator.


    // Defining and Initializing a Container
    // * With the exception of array, the default constructor creates an empty container of the specified type.
    // * The other constructors take arguments that specify the size of the container and initial values for the elements.
    // * Two ways for initailizing a Container as a Copy of Another Container:
    //   1. Directly copy the container.
    //   2. Copy a range of elements denoted by a pair of iterators.
    // * To create a container as a copy of another container, the container and element types must match.
    // * The element types in the new and original containers can differ as long as it is possible to convert the elements
    //   we are copying to the element type of the container we are initializing.
    // * When we initialize a container as a copy of another container, the container type and element type of both containers must be identical.
    // * When we pass iterators, there is no requirement that the container types be identical.
    // * The following shows defining and initializing containers:
    // C c;  // Default constructor. If C is array, then the elements in c are default-initialized; otherwise c is empty.
    // C c1(c2);   // c1 is a copy of c2. c1 and c2 must have the same type 
    // C c1 = c2;  // (i.e., they must be the same container type and hold the same element type; for array must also have the same size.)
    // 
    // C c{a, b, c};        // c is a copy of the elements in the initializer list. 
    // C c = {a, b, c};     // Type of elements in the list must be compatible with the element type of C.
    //                      // For array, the list must have same number or fewer elements than the size of the array.
    // C c(b, e);           // c is a copy of the elements in the range denoted by iterators b and e.
    //                      // Type of the elements must be compatible with the element type of C. (Not valid for array.)
    // * Constructors that take a size are valid for sequential containers only.
    // C seq(n)             // seq has n value-initialized elements; this constructor is explicit (Not valid for string)
    // C seq(n, t)          // seq has n elements with value t.

    // each container has three elements, initialized from the given initializers
    std::list<std::string> authors = {"Milton", "Shakespeare", "Austen"};
    std::vector<const char*> articles = {"a", "an", "the"};
    
    std::list<std::string> list2(authors);  // ok: types match.
    // std::deque<std::string> authList(authors);  // error: container types don't match.
    // std::vector<std::string> words(articles);  // error: element types must match.

    // The following case is passing iterators.
    // The constructor that takes two iterators uses them to denote a range of elements that we want to copy.
    std::forward_list<std::string> words(articles.begin(), articles.end());    // ok: converts const char* elements to string.
    // Copy a subsequence of a container to construct and initialize a container.
    // e.g. copies up to but not including the element denoted by it. (Assume it is an iterator denoting an element in authors.)
    std::list<std::string>::iterator it_authors = authors.end();
    --it_authors;
    std::deque<std::string> authList(authors.begin(), it_authors);
    

    // List Initialization
    // * For types other than array, the initializer list also implicitly specifies the size of the container.
    // std::list<std::string> authors = {"Milton", "Shakespeare", "Austen"};
    // std::vector<const char*> articles = {"a", "an", "the"};

    // Sequential Container Size-Related Constructors
    // * Initialize the sequential containers (other than array) from a size and an (optional) element initializer.
    // * If we do not supply an element initializer, the library creates a value-initialized one for us. 
    //   (Only valid for the built-in type or a class type that has a default constructor.)
    // * If the element type does not have a default constructor, then we must specify an explicit element initializer along with the size.
    std::vector<int> ivec(10, -1);   // ten int elements, each initialized to -1.
    std::list<std::string> svec(10, "hi!");   // ten strings; each element is "hi!"
    std::forward_list<int> ivec2(10);   // ten elements, each initialized to 0.
    std::deque<std::string> svec3(10);    // ten elements, each an empty string.
    // * The constructor that takes a size are valid only for sequential containers; they are not supported for the associative containers.

    // Library arrays Have Fixed Size
    // * Since the size of a library array is part of its type, when we define an array, in addition to specifying the element type,
    //   we also need to specify the container size.
    std::array<int, 42> AA; // type is: array that holds 42 ints.
    std::array<std::string, 10> BB; // type is: array that holds 10 strings.
    std::array<int, 10>::size_type i;  // array type includes element type and size.
    // std::array<int>::size_type j;      // error: array<int> is not a type.

    // 


    
    


    return 0;
}