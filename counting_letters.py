a = input()

count = 0

for i in a:
	if i == 'f':
		count += 1
		
if count == 0:
	print(-1)
elif count == 1:
	print(a.find('f'), end=' ')
else:
	print(a.find('f'), a.rfind('f'))

"""
s = input()
if s.find('f') == s.rfind('f'):
  print(s.find('f'))
else:
  print(s.find('f'), s.rfind('f'))
  """

# Given a string that may contain a letter p. 
# Print the index of the second occurrence of p. 
# If the letter p occurs only once, then print -1, 
# If the string does not contain the letter p, then print -2.

a = input()

count = 0

for i in a:
	if i == 'p':
		count += 1
		
if count == 0:
	print(-2)
elif count == 1:
	print(-1)
else:
	p1 = a.find('p')
	print(a.find('p', p1+1))

"""
s = input()
if 'p' in s:
  if s.find('p') == s.rfind('p'):
    print(-1)
  else:
    print(s.find('p') + s[s.find('p') + 1:].find('p') + 1)
else:
  print(-2)
"""