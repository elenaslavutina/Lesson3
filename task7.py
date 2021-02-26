import json
try:
    with open("my_file_7.txt","r",encoding='UTF-8') as f:

        summ = 0
        dict = {}
        dict2 = {}
        number = 0
        list = []
        for line in f:
            line_s = line.rsplit()

            number = number + 1

            clue = line_s[0]

            a1 = int(line_s[2])
            a2 = int(line_s[3])


            pribul = a1 - a2

            if pribul > 0:
                summ = summ + pribul




            dict[clue] = pribul
        srednaa_prib = summ /number
        list.append(dict)
        dict2["Средняя прибыль"] = srednaa_prib

        list.append(dict2)
        with open("task7_result.json", 'w', encoding="utf-8") as outfile:
            json.dump(list, outfile, ensure_ascii=False)
        print(list)


except IOError:
    print("Произошла ошибка ввода-вывода!")
