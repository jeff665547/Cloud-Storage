while True:
    try:
        AA = eval(input(""))
        BB = int(input(""))
        ans = AA/BB 
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print(AA,"/", BB, " = %.2f"%(AA/BB), sep ="")
        break