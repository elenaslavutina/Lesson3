def sum_numbers(stroka):

    sum = 0
    for number in stroka:
        if number.isdigit():
           sum = sum + int(number)
        else:
            break


    return sum
stroka = []
stroka.append(input("Введите числа, разделенные пробелом. Чтобы выйти нажмите любую букву  "))
stroka1 = stroka[0].split()
summ = sum_numbers(stroka1)
print(summ)

