from itertools import count
from itertools import cycle
for e in count(8,3):
    if e > 25:
        break
    else:
        print(e)

spisok = "учитьсяоченьполезно"
с = 0
for e in cycle(spisok):
    if с > 50:
        break
    print(e)
    с += 1
