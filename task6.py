
try:
    with open("my_file_6.txt","r",encoding='UTF-8') as f:


        dict = {}
        for line in f:
            summ = 0
            line_s = line.split(":")
            clue = line_s[0]
            line_2 = line.split()

            for i in line_2:
                ind = i.find("(")
                s = i[:ind]
                if ind  >= 0:
                   summ = summ + int(s)
            if clue != '\n' :
                dict[clue] = summ
        print(dict)


except IOError:
    print("Произошла ошибка ввода-вывода!")
