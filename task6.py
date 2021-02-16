def upper_case(stroka):
    stroka2 = stroka[0].upper() + stroka[1:]
    return stroka2

def stroka_upper(long_stroka):
    stroka = long_stroka.split()
    stroka2 =[]
    for slovo in stroka:
        stroka2.append(upper_case(slovo))
    result = " ".join(stroka2)
    return result

str = input("Введите слово , все буквы маленькие   ")
print(upper_case(str))
str2 = input("Введите слова через пробел с маленьком регистре   ")
print(stroka_upper(str2))

