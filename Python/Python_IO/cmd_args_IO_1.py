# command line arguments in Python
import getopt
import sys

def usage():
    print("Addition: python get_opt.py -a <number1> -b <number2>")
    print("Subtraction: python get_opt.py -a <number1> -b <number2> --subtract")
    print("Example: python get_opt.py -a 10 -b 3\n")
    
# return sum of two numbers
def add(a, b):
    return a + b

# return difference of two numbers
def subtract(a, b):
    return a - b

def main():
    try:
        #                     getopt(args, shortopts, longopts=[])
        (opts, args) = getopt.getopt(sys.argv[1:], "ha:b:s", ["help", "num1=", "num2=", "subtract"])
        # sys.argv holds the unformatted list of all the arguments passed to this python script.
        # Specify shortopts as a colon(:) separated single letter characters.
        # Specify longopts as a comma separated list of words with the suffix =
        # `longopts` without the suffix = are considered as a flag and they should be passed without any value.
        
        # We’re using two variables (`opts`, `args`) because getopt.getopt function returns two elements. 
        # One containing a <list> of options and another has a <list> of arguments which are not specified 
        # in our getopt initialisation.
        
    # raised whenever an option (which requires a value) is passed without a value.
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
        
    num1 = num2 = None
    sub = False
    
    # check if any options were passed.
    if len(opts) != 0:
        # loop over opts: Ex, [(a, 10), (b, 20)] => <list>
        
        # `o` will hold our option name and 
        # `a` will have any value assigned to the option.
        # --subtract is being used as a flag it will not have any value.
        for (o, a) in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-a", "--num1"):
                num1 = int(a)
            elif o in ("-b", "--num2"):
                num2 = int(a)
            elif o in "--subtract":
                sub = True
            else:
                # none of the acceptable options were passed
                usage()
                sys.exit(2)
                
    else:
        # no options were passed
        usage()
        sys.exit(2)
     
    # check if num1 and num2 not None
    if num1 and num2:
        if sub:
            print("\n Difference in two numbers is:", subtract(num1, num2), "\n")

        else:
            print("\n Sum of two numbers is:", add(num1, num2), "\n")    
            
    else:
        usage()
        sys.exit(2)
        
if __name__ == "__main__":
    main()