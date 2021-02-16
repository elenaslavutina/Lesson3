def sum_two_max(arg1, arg2, arg3):
    min=arg1
    if arg2 < arg1:
        min = arg2
    elif arg3 < min:
            min = arg3

    return min
str = input("Введите три числа через пробел  ")
print(str)

spisok = str.split()
print(spisok)

print(sum_two_max(int(spisok[0]), int(spisok[1]), int(spisok[2])))
