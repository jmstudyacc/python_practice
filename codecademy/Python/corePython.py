"""
Author: James Miles
Purpose: Pluralsight Core Python Course 

Retrieve and print words from a URL

Usage:

    python3 corePython.py <URL>
"""

import sys
from urllib.request import urlopen


def getWords(url):
    """ Fetch a list of words from a URL.
    
        Args:
            url: The URL of a UTF-8 text document.
    
        Returns:
            A list of strings containing the words
            from the document.
    """
    story = urlopen(url)
    storyWords = []
    for line in story:
        line_words = line.decode('utf8').split()    # The HTTP response comes back in bytes format so we need to decode it to 'utf8'. 
        for word in line_words:                     # You decode each word received by running decode agains the line value in the loop
            storyWords.append(word)
    story.close()
    return storyWords


def printItems(items):
    """ Prints items one per line.
    
        Args:
            items: An interable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    """ Print each word from a text document from a URL.

        Args:
            url: URL passed by user of a UTF-8 text document.

    """
    words = getWords(url)   # When run the program assigns the result of getWords to 'words' 
    printItems(words)       # It then calls the printItems function to run against 'words', which is running against the storyWords list


if __name__ == '__main__':  # This tests the value of dunder name, if the value of dunder name is dunder main that means the module is being executed
    main(sys.argv[1])       # Refers to the list of command line arguments passed to the Python scrip
                            # In this instance the command line argument is the URL
                            # sys.argv[0] references the script itself
