# 5.4.2 Python's String Class

import random
from time import time

Random = 'abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_-+=[]{}|\/?<>,.`~` '
document = str()
document = ''.join(random.choice(Random) for i in range(1000000))

# first time
letters = ''
begin = time()
for c in document:
    if c.isalpha():
        letters += c
end = time()
print('1:',end - begin)

# second time
letters = ''
temp = []
begin = time()
for c in document:
    if c.isalpha():
        temp.append(c)
letters = ''.join(temp)
end = time()
print('2:',end - begin)

# third time
letters = ''
begin = time()
letters = ''.join(c for c in document if c.isalpha())
end = time()
print('3:',end - begin)

# forth time
letters = ''
begin = time()
letters = ''.join([c for c in document if c.isalpha()])
end = time()
print('4:',end - begin)