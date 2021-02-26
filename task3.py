f = open("my_file_3.txt", "r",encoding='UTF-8')
sum = 0
count = 0
for el in f:
        l = el.split()
        count = count + 1
        sum = sum + int(l[1])
        if int(l[1])< 20000:
            print(f"Сотрудник {l[0]} имеет доход {int(l[1])}")

print(f"Средний доход сотрудников = {sum/count}")
f.close()


