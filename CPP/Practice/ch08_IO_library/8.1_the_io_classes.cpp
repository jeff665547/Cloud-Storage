# include <iostream>
# include <sstream>
# include <fstream>

// * We would like to use >> to read data regardless of whether we are reading a console window, a disk file, or a string.
// * Similarily, we would like to use that operator regardless of whether the characters we read fit in a char or require a wchar_t.
// * The library lets us ignore the differences among these different kinds of streams by using inheritance.
// * As with templates, we can use classes related by inheritance without understanding the details of how inheritance works.
// 
// IO Library Types and Headers 
// * iostream => reads/writes from a stream.
// * fstream => reads/writes from a file.
// * sstream => reads/writes from a string.
// 

int main(){

    /* No copy or assign for IO objects */
    std::ofstream out1, out2;
    // out1 = out2;  // error: cannot assign stream objects.
    std::ofstream print(std::ofstream);  // error: cannot initialize the ofstream parameter.
    // out2 = print(out2);  // error: cannot copy stream objects.
    // * Since we cannot copy the IO types, we cannot have a parameter or return type that is one of 
    //   the stream types.
    // * Functions that do IO typically pass and return the stream through references. 
    // * Reading or writing an IO object changes its state, so the reference must not be const.

    /* Condition States of a Stream */
    // * The easiest way to determine the state of a stream object is to use that object as a condition.
    // while(std::cin >> word){
    //    // if the state is ok (read operation is successful, .... ), then start to do something ...
    // }
    // 
    // * The IO library defines a machine-dependent integral type named iostate that it uses to 
    //   convey information about the state of a stream. 
    // * This type is used as a collection of bits.
    // * The IO classes define four constexpr values of type iostate that represent particular bit patterns:
    //   1. badbit: Indicate that a stream is corrupted. The badbit indicates a system-level failure, e.g. an unrecoverable read or write error.
    //      It's usually not possible to use a stream once badbit has been set.
    //   2. failbit: Indicate that an IO operation failed. The failbit is set after a recoverable error, e.g. reading a character when numeric data was expected.
    //      It's often possible to correct such problems and continue using the stream.
    //   3. eofbit: Indicate that a stream hit end-of-file. Reaching end-of-file sets both eofbit and failbit.
    //   4. goodbit: Indicate that a stream is not in an error state. It is guaranteed to have the value 0, indicates no failures on the stream.
    //   * If any of badbit, failbit, or eofbit are set, then a condition that evaluates that stream will fail.
    // * The library also defines a set of functions to interrogate the state of these flags.
    //   1. The good operation returns true if none of the error bits is set.
    //   2. The bad, fail, and eof operations return true when the corresponding bit is on.
    //   3. Moreover, fail operations returns true if bad operation is set.
    //   4. By implication, the right way to determine the overall state of a stream is to use either good or fail.
    //   5. The follow-up executed code that is executed when we use a stream as a condition is equivalent to calling !fail().
    std::stringstream s;
    bool eoftrue = s.eof();  // true if eofbit in the stream s is set.
    bool failtrue = s.fail();  // true if failbit or badbit in the stream s is set.
    bool badtrue = s.bad();   // true if badbit in the stream s is set.
    bool goodtrue = s.good();  // true if the stream s is in a valid state.
    s.clear();  // reset all the consition values in the stream s to valid state. Returns void. (turns off all the failure bits.)
    // s.clear(flags); // reset the condition of s to flags. Type of flags is strm::iostate. Returns void.
    // s.setstate(flags);  // Adds specified condition(s) (given condition bit(s)) to s. Type of flags is strm::iostate. Returns void.
    s.rdstate(); // Returns current condition of s as a strm::iostate value.

    auto old_state = std::cin.rdstate();  // remember the current state of std::cin
    std::cin.clear();   // make std::cin valid.
    int gg;
    std::cin >> gg;                 // use std::cin.
    std::cin.setstate(old_state);   // now reset std::cin to its old state.
    std::cin.clear(std::cin.rdstate() & ~std::cin.failbit & ~std::cin.badbit);
    // turns off failbit and badbit but all other bits are unchanged. (leaves eofbit untouched.)

    /* Managing the Output Buffer */
    // * Buffers are not flushed if the program crashes
    // * Each output stream manages a buffer, which it uses to hold the data that the program reads and
    //   writes. e.g. os << "please enter a value: "; 
    // * The literal string might be printed immediately, or the operating system might store the data in
    //   a buffer to be printed later.
    // * Using a buffer allows the operating system to combine serval output operations from our program into a 
    //   single system-level write.
    // * Since writing to a device can be time-consumimg, letting the operating system combine several
    //   output operations into a single write can provide an important performance boost.
    // * There are several conditions that cause the buffer to be flushed -- that is, to be written -- to the actual
    //   output device or file:
    //   1. The program completes normally. All output buffers are flushed as part of the return from main.
    //   2. At some indeterminate time, the buffer can become full, in which case it will be flused before writing the next value.
    //   3. We can flush the buffer explicitly using a manipulator such as endl.
    //   4. We can use the unitbuf manipulator to set the stream's internal state to empty the buffer after each output operation.
    //      By default, unitbuf is set for cerr, so that writes to cerr are flushed immediately.
    //   5. An output stream might be tied to another stream. In this case, the buffer of the tied stream is flushed whenever the 
    //      tied stream is read or written. By default, cin and cerr are both tied to cout. Hence, reading cin or writing to cerr
    //      flushes the buffer in cout.
    // * endl manipulator ends the current line and flushes the buffer.
    // * flush and ends are two other similar manipulators:
    //   1. flush: flush flushes the stream but adds no characters to the output;
    //   2. ends: ends inserts a null character into the buffer and then flushes it.
    //   * examples:
    std::cout << "hi!" << std::endl;  // writes hi and a newline, then flushes the buffer.
    std::cout << "hi!" << std::flush; // writes hi, then flushes the buffer; adds no data.
    std::cout << "hi!" << std::ends;  // writes hi and a null, then flushes the buffer.
    std::cout << "finished!!" << std::endl;

    // * unitbuf manipulator flush after every output. This manipulator tells the stream to do a flush
    //   after every subsequent write.
    // * nounitbuf manipulator restores the stream to use normal, system-managed buffer flushing:
    std::cout << std::unitbuf;  // all writies will be flushed immediately
                                // any output is flushed immediately, no buffering
    std::cout << std::nounitbuf; // returns to normal buffering
    
    // The library ties cout to cin (概念為cin要進來buffer以前會先將cout所使用的buffer給往外清空(意即print到screen)), so the statement:
    int ival;
    std::cin >> ival;
    // causes the buffer associated with cout to be flushed.
    
    
    /* .tie() */
    // There are two overloaded versions of tie: 
    // 1. Takes no argument and returns a pointer to the output stream, if any, to which this object is currently tied.
    //    The function returns the null pointer if the stream is not tied.
    // 2. Takes a pointer to an ostream and ties itself to that ostream. That is, x.tie(&o) ties the stream x to the output stream o.
    // * To tie a given stream to a new output stream, we pass tie a pointer to the new stream.
    // * To untie the stream completely, we pass a null pointer.
    // * Each stream can be tied to at most one stream at a time.
    // * However, multiple streams can tie themselves to the same ostream.
    // Example: We can tie either an istream or an ostream object to another ostream:
    // std::cin.tie(&std::cout);   // illustration only: the library ties cin and cout for us.

    // old_tie points to the stream (if any) currently tied to cin.
    std::ostream *old_tie = std::cin.tie(nullptr);  // cin is no longer tied.
    
    // ties cin and cerr; not a good idea because cin should be tied to cout.
    std::cin.tie(&std::cerr); // reading std::cin flushes std::cerr, not std::cout
    std::cin.tie(old_tie);  // reestablish normal tie between cin and cout

    

    return 0;
}