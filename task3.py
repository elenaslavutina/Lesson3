def sum_two_max(stroka):
    s = stroka.split()
    minimum = int(s[0])
    summ = int(s[0])
    for i in range(1,len(s)):
        if int(s[i])<minimum:
            minimum = int(s[i])
        summ = summ + int(s[i])
    summ = summ - minimum

    return summ
stroka = input("Введите три числа через пробел  ")
print(stroka)

spisok = stroka.split()
print(spisok)
print(f"Сумма чисел без минимального = {sum_two_max(stroka)}")