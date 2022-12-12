# include <fstream>
# include <iostream>

int main(){

    // The fstream header defines three types to support file IO:
    //  1. ifstream to read a given file.
    //  2. ofstream to write a given file.
    //  3. fstream reads and writes a given file.
    // * The fstream inherit from the iostream types, the types defined in fstream add members to manage the file associated with the stream.
    // * fstream-Specific Operations:
    //   fstream fstrm;     Creates an unbound file stream. fstream is one of the types defined in the fstream header.
    //   fstream fstrm(s);  Creates an fstream and opens the file named s. s can have type string or can be a pointer to a C-style character string.
    //                      These constructors are explicit. The default file mode depends on the type of fstream.
    //   fstream fstrm(s, mode);  Like the previous constructor, but opens s in the given mode.
    //   fstrm.open(s);           Opens the file named by the s and binds that file to fstrm. s
    //   fstrm.open(s, mode);  can be a string or a pointer to a C-style character string. The default file mode depends on the type of fstream. Returns void.
    //   fstrm.close()  Close the file to which fstrm is bound. Returns void.
    //   fstrm.is_open()  Returns a bool indicating whether the file associated with fstrm was successfully opened and has not been closed.

    /* Using File Stream Objects */
    // * Each file stream class defines a member function named "open" that does whatever system-specific operations are 
    //   required to locate the given file and open it for reading or writing as appropriate.
    // * When we create a file stream, we can (optionally) provide a file name. When we supply a file name, "open" is called automatically:
    std::string ifile = "ISO.csv"; // this is just an example.
                                   // In this new standard, file names can be either library strings or C-style character arrays.
    std::ifstream in(ifile); // construct an ifstream and open the given file. 
                             // In this example, "in" is an input stream that is initialized to read from the file named by the string argument ifile.
    std::ofstream out;  // output file stream that is not associated with any file.
                        // In this example, "out" is an output stream that is not yet associated with a file.

    
    
    
    return 0;
}