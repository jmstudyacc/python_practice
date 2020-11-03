"""
Implement a function word_count(s) that, given a string consisting of words separated by spaces, returns how many distinct words it has. 

For example, the result of 
print(word_count("Such a day is a bad day"))
must be
5

"""

def word_count(s):
    usr_ipt = s.split()
    usr_set = set(usr_ipt)
    
    print(len(usr_set))

word_count(input())

"""
def word_count(s):
  word_list = s.split()
  
  S = set()
  for el in word_list:
    S.add(el)
    
  return len(S)
"""