from random import randint
spisok = []

def generator(number):
    for i in range(number):
        el = randint(0,1000)
        spisok.append(el)
    return spisok

s = generator(100)
print(s)
t=[]
for i in range(len(s)-1):
    if (s[i]< s[i+1]):
        t.append(s[i+1])
print(t)