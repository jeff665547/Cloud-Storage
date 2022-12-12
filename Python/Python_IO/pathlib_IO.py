# Python pathlib
# The pathlib is a Python module which provides an object API for working with 
# files and directories. The pathlib is a standard module.

from pathlib import Path
import os

#%%
# f-Strings: A New and Improved War to Format Strings in Python (start from Py 3.6)
# get the current working directory with cwd() and the home directory with home()
print(f"Current directory: {Path.cwd()}")
print("Current directory: {}".format(Path.cwd())) 
# equivalent with above example but above example (f-Strings) runs faster.
print(f"Home directory: {Path.home()}")

#%%
# Change directory
path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO")
os.chdir(path)
print(f"Current directory: {Path.cwd()}")
os.chdir("..")
print(f"Current directory: {Path.cwd()}")

#%%
# Create a new directory
path = Path(r"C:\Users\jeff\Desktop")
os.chdir(path)
print(f"Current directory: {Path.cwd()}")
path = Path.cwd() / "pathlib"
path.mkdir(exist_ok = True)
# exist_ok = True  
# => Error and exceptions (FileExistsError) will be ignored if the target directory already exists.
os.chdir(path)
print(f"Current directory: {Path.cwd()}")

path1 = Path(r"C:\Users\jeff\Desktop") / "layer1" / "layer2"
path1.mkdir(parents = True, exist_ok = True)
# parents = True
# => Any missing parents of this path are created as needed. 
# (with the default permissions.)

#%%
# Copy a file
from shutil import copyfile

# Suppose that there is a file called words.txt in the current working directory.
source = Path("words.txt")
destination = Path("words_bck.txt")
copyfile(source, destination)

#%%
# Join paths
path = Path.home()

docs = path / "Documents"   # / is used to create child paths and mimics the behavior of os.path.join.
pictures = path / "Pictures"

print(docs)
print(pictures)

#%%
# Path touch (Equivalent to the Linux touch command.)
print(f"Current directory: {Path.cwd()}")
# create a new empty file at the current working directory.
Path("myfile.txt").touch()

#%%
# Path rename
print(f"Current directory: {Path.cwd()}")
path = Path("names.txt")
path.touch() # create a file names.txt in the current working directory.
path.rename("mynames.txt") # rename the file to mynames.txt

path = Path(r"C:\Users\jeff\Desktop\pathlib\new")
path.rename(r"C:\Users\jeff\Desktop\pathlib\rename")

#%%
# Path representations
path = Path("C:/Users/Jano/Downloads/wordpress-5.1.tar.gz")

print(path)  # Windows file path.
print(path.as_uri())  # URI style file path.
print(path.as_posix())  # POSIX style file path.

#%%
# Relative path 
path = Path(r"C:\Users\jeff\Desktop\pathlib")
home = Path.home()
relative = path.relative_to(home)

print(relative)

#%%
# Parents of a path
path = Path(r"C:\Users\jeff\Desktop\pathlib")
print(f"The parent directory of {path} is {path.parent}")
print(f"The parent of the parent of {path} is {path.parent.parent}")
print(f"All the parents of {path.parent}: ")
print(list(path.parents))

#%% 
# Path components
path = Path(r"C:\Users\jeff\Desktop\pathlib")

print(path.parts)  # The parts gives access to the path's various components.
print(path.drive)  # The drive gives a string representing the drive letter or name, if any.
print(path.root)   # The root gives a string representing the (local or global) root, if any

path = Path(r"C:\Users\jeff\Desktop\pathlib\wordpress-5.1.tar.gz")
print(f"The stem is: {path.stem}")        # The final path component without its suffix.
print(f"The name is: {path.name}")        # The entire filename (includes file extension).
                                          # (The path component without any directory)
print(f"The suffix is: {path.suffix}")    # The suffix of the file (final component) (or file extension)
print(f"The anchor is: {path.anchor}")    # The part of a path before the directory.
print(f"File name: {os.path.splitext(path.stem)[0]}")  # The filename (excludes the file extension).
print("The suffixes: ")
print(path.suffixes)   # print all the suffixes of the final component.

#%%
# Subdirectories of the specified directory.
path = Path(r"C:\Users\jeff\Desktop\pathlib")
new_path = Path("rename")
new_path.mkdir()

# list all directories (check if the path object is a directory by using is_dir())
dirs = [e for e in path.iterdir() if e.is_dir()]
print(dirs)

# list all files (check if the path object is a directory by using is_file())
files = [e for e in path.iterdir() if e.is_file()]
print(files)

#%%
# Path globbing 
# "glob" means global, global pattern
# Glob patterns specify setsof filenames with wildcard characters. 
# For example, the * character of the *.txt is a wildcard standing for any 
# string of characters. The *.txt represents all files with ending in .txt. 
# The other common wildcard is the question mark (?), which stands for one character.
path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib")
file = path / "rename" / "test.txt"
file.touch()

# rglob: recursive globbing. 
# Find the corresponding file under the given directories and all its subdirectories.
for e in path.rglob("test.txt"):
    print(e)

# **/ is equivalent to rglob.
# Find the corresponding file (test.txt) under the given directories and all its subdirectories.
for e in path.glob("**/test.txt"):
    print(e)
    
# Find the corresponding file (*.txt) under the given directories and all its subdirectories.
for e in path.glob("**/*.txt"):
    print(e)

# Find the corresponding file (*.txt) under the given directories.
for e in path.glob("*.txt"):
    print(e)

# Find the corresponding file (tes?.txt) under the given directories and all its subdirectories.
for e in path.rglob("tes?.txt"):
    print(e)
    
#%% 
# Path tree
# A pratical program which outputs the contents of the specified directory in a 
# hierachical tree structure.
def tree(directory):
    
    print(f"+ {directory}")
    
    for path in sorted(directory.rglob("*")): # * represents all files.
        
        depth = len(path.relative_to(directory).parts)
        spacer = "    " * depth
        
        # print(f"{spacer} + {path.name}")
        
        if path.is_file():
            print(f"{spacer}f {path.name}")
        else:
            print(f"{spacer}d {path.name}")
            
path = Path.home() / "Downloads" 
tree(path)

#%%
# Counting files by extension
# In the following example, we count all files by their extension.
# We use the collections's Counter for the task.
import collections

docs = Path.home() / "Documents"

# counts files grouped by their extension in the "Documents" directory.
files = [path.suffix for path in docs.iterdir() if path.is_file() and path.suffix]
data = collections.Counter(files)

print(data)

for key, val in data.items():
    print(f"{key}: {val}")

#%%
# Path read_text
path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib\words.txt")

# The optional parameters have the same meaning as in open().
content = path.read_text()
print(content)

#%%
# Path read file with open()
path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib\words.txt")

with path.open() as f:
    lines = f.readlines()
    print(lines)

for line in lines:
    print(line.rstrip())

# Original open(): with open(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib\words.txt", r) as f:
#                      lines = f.readlines()

#%%
# Path read binary file
import binascii
from more_itertools import sliced

# The example reads a PNG picture and prints it to 
# the terminal in hexadecimal representation.
path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib\scan.png")

# Binary files, such as images, can be read with read_bytes().
hexed = binascii.hexlify(path.read_bytes())
mybytes = list(sliced(hexed, 2))

i = 0

for b in mybytes:
    
    print(b.decode("utf-8"), end = " ")
    i += 1
    
    if (i % 30 == 0):
        print()

#%%
# Path write_text
path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib")
os.chdir(path)

file = Path("myfile.txt")
file.touch()

file.write_text("This is myfile.txt.")

#%%
# New article
import datetime

# Content management systems often put their newly created articles in directory
# structure based on the current year and month.
# This example demonstrates this.

# The program ask an input from the users. 
# It then creates a new text file based on the current year and month.

now = datetime.datetime.now()
year = now.year
month = now.month

name = input("Enter article name:")

path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib")
os.chdir(path)

path1 = Path("articles") / str(year) / str(month)
path1.mkdir(parents = True, exist_ok = True)


path2 = path1 / f"{name}.txt"

path2.touch()

print(f"Article created at: {path2}")


#%%
# PrettyTable example
# When we work with files and directories, we can use PrettyTable module for
# nicer output.
# The example displays all text files inside Documents in a nice table. 
# The table contains three columns: file name, size, and created date.
import datetime
from prettytable import PrettyTable
path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_IO\pathlib")

pt = PrettyTable()
pt.field_names = ["File name", "Size", "Created"]

pt.align["File name"] = "l"
pt.align["Size"] = "r"
pt.align["Created"] = "l"

# Path.stat() contains information about this path. (like os.stat())
for e in path.glob("**/*.txt"):
    
    created = datetime.datetime.fromtimestamp(e.stat().st_ctime)
    print(e.stat())
    size = e.stat().st_size  # file/path size
    pt.add_row([e.name, size, f"{created:%Y-%m-%d}"])
    
print(pt)

#%%
# Jump from the current working directory.
path = Path(r"C:\Users\jeff\Desktop")
os.chdir(path)
