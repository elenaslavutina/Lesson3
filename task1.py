try:
    f = open("my_file_1.txt","a",encoding='UTF-8')
    while True:
        l = input("Введите строку. Для окончания введите пустую строку. ")
        if not l:
            break

        f.write(l)
        f.write('\n')
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f.close()







