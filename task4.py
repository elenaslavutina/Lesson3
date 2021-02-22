from functools import reduce
l = [e for e in range(100,1001) if ( e%2 == 0)]
m = [e for e in range(1,11) if ( e%2 == 0)]
print(l)

def multiplai(one, two):

    return one * two

print(reduce(multiplai, l))
print(m)
print(reduce(multiplai, m))
