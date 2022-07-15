import string
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
a = random.choice(string.ascii_letters)
b = random.randrange(10, 0, -1)
c = random.choice(string.ascii_letters)
d = random.choice(string.ascii_letters)
e = random.randrange(10, 0, -1)
f = random.choice(string.ascii_letters)
g = random.randrange(10, 0, -1)
h = random.choice(string.ascii_letters)
i = random.choice(string.ascii_letters)
j = random.randrange(10, 0, -1)
k = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)
print(k)