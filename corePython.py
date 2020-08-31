"""
Author: James Miles
Purpose: Pluralsight 
"""
from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
storyWords = []
for line in story:
	line_words = line.decode('utf8').split()    # The HTTP response comes back in bytes format so we need to decode it to 'utf8'. 
	for word in line_words:                     # You decode each word received by running decode agains the line value in the loop
		storyWords.append(word)
story.close()

for word in storyWords:
    print(word)

