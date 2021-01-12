'''
 Python 1 - DAT-119 
 Homework 9
 The initial shell of the Pig Latin program -- gets the text out of prejudice.txt 

'''

import os 
import string


# you do not need to change this function
# (but if you want to, you can)
def get_text(filename):
    """get the text from the specified file, with its path passed in as a string"""
    the_text = ""
    # is the file actually there?
    if os.path.isfile(filename):
        # open it, and read its contents
        file_handler = open(filename, 'r')
        the_text = file_handler.read()
        file_handler.close()
    return the_text


def main():
    # get the text from the file; prejudice is a big, long string
    prejudice = get_text('prejudice.txt')
    
    # prove to ourselves that it worked
    print(prejudice)


# the incantation to make the program go
if __name__ == "__main__":
    main()