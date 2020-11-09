# READING & WRITING
# -----------------

# To write a file in python on the IDE you need to do the following:

# >>> fout = open('output.txt', 'w')

# open = open a file
# 'output.txt' = name of file
# 'w' = write file

# The above is important to note as the IDE command will open a file called 'output.txt' and write to it
# This is significant as if there is no 'output.txt' file it will create a new one
# If there IS a file named 'output.txt' and you use the 'w' argument you will OVERWRITE the contents of that file
# Use 'a' if you want to append to a file that already exists!

# >>> line1 = '1, 2, 3, 4, 5 once I caught a fish alive'
# >>> fout.write(line1)

# We are assigning a value (a famous British nursery rhyme) to line1
# We then proceed to write 'line1' to the variable 'fout', which is 'output.txt'
# The number printed out shows how many characters were written to the file

# When you are finished writing to a file, remember to close it oterhwise it closes when the program ends

# >>> fout.close()

# FORMAT OPERATOR
# ---------------

# When writing to a file there is a caveat to be aware of - anything being written to a file MUST be a string
# Therefore when trying to write other types into a file we need to convert them to a string
# The quickest way to achieve this is with the str() function

# >>> x = 52
# >>> fout.write(str(x))

# This does not scale fantastically well so an alternative is to use the FORMAT OPERATOR %
# The FORMAT OPERATOR shares the same symbol as MODULUS but when applied to STRINGS it is FORMAT OPERATOR
# There are unique FORMATS for the variable types that need to be adhered to for successful use

# '%d' = second operand should be formatted as a DECIMAL integer
# '%g' = second operand should be formatted as a FLOATING-POINT number
# '%s' = second operand should be formatted as a STRING

# >>> camels = 42
# >>> 'I have spotted %d camels.' % camels

# If you have more than ONE FORMAT SEQUENCE in the string, the second argument has to be a TUPLE

# >>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels') 

# NOTE - the number of elements in the tuple has to match the number of FORMAT SEQUENCES otherwise you will get an error
# Furthermore, the TYPE of elements in the tuple MUST match the FORMAT SEQUENCES

# Check out the 'string format' method though, it is more powerful than the above

# FILENAMES AND PATHS
# -------------------

# When considering files you need to be aware that a filename of, 'memo.txt' is a RELATIVE PATH NAME
# This means that it is the path name relative to the directory you are currently in
# If you want to find the absolute path of a file you can use the os.path.abspath() function

# >>> import os
# >>> os.path.abspath('memo.txt')

# If you wanted to know what your current working directory is then you can use the following:
# >>> cwd = os.getcwd()
# >>> cwd

# You can also check to see if a file exists already:
# >>> os.path.exists('memo.txt')

# If the file or directory exists you can check if it's a dir with the following:
# >>> os.path.isdir('memo.txt')

# Similarly you can check if it is actually a file:
# >>> os.path.isfile('memo.txt')

# If you were intrigued about the contents of a directory you can run the following:
# >>> os.listdir(cwd)

# That will show you a list of the files and other directories in the specified directory

# EXERCISE
# --------
"""
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        
        else:
            walk(path)

os.path.join takes a directory & filename and joins them together to make a full path
In Python the 'os' module provides a 'walk' function similar to this but more powerful

As an exercise, read the documentation and use it to print the names of the filesin a given directory and its subdirectories
"""

# CATCHING EXCEPTIONS
# -------------------

# Errors happen when working and moreso when reading & writing files
# A classic error would be opening a file that does not already exist!

# When that happens you will get an IOError stating the file does not exist
# >>> fin = open('bad_file')

# You will also experience issues when trying to access a file you do not have permissions to access:
# >>> fin = open('/etc/passwd', 'w')

# If you get confused and try to read a DIRECTORY when you meant a FILE, you might see the following:
# >>> fin = open('/home')

# You could avoid these errors by checking every file/dir exists and if the target is a file
# That doesn't scale too well so a compromise is to use a try...except approach

# try:
#     fin = open('bad_file')
# except:
#     print('Something went wrong')

# Python will start be executing the 'try' clause and if there's no issues it skips the 'except' clause
# Should an exception occur Python leaves the 'try' clause and runs the 'except' clause
# CATCHING EXCEPTIONS is advised - but use a better error message to aid troubleshooting!!