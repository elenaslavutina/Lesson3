def square(x,y):
    y = abs(y)
    z = x
    if y == 1:
        res = 1/x
    else:
        i = 2
        while i <= y:
            x = z*x
            i = i + 1
        res = 1/x

    return res
sam = square(3, -1)
print(sam)