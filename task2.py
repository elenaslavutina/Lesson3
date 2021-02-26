try:
    with open("my_file_2.txt","r",encoding = 'UTF-8') as f:
        count = 0
        for line in f:
            count += 1
            print(f"Количество строк в {count} строке = {len(line)-1}")

        print(count)
except IOError:
    print("Произошла ошибка ввода-вывода!")

