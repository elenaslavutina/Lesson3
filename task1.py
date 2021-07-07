def divition():
    delimoe = float(input("Введите делимое: "))
    delitel = float(input("Введите делитель: "))
    if delitel != 0:
        result = delimoe/delitel
        return result
    else:
        return
chastnoe = divition()
print(chastnoe)
