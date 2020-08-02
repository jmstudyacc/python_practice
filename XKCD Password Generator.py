# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(choice(words) for i in range(4))
    print (password)

# To use this spin up a Linux VM and run.
# Windows doesn't have a dictionary like Linux.
