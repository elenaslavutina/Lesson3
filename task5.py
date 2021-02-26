f = open("my_file_5.txt","w+",encoding='UTF-8')
while True:
   l = input("Введите числа, разделенные пробелом. Для окончания введите пустую строку. ")
   if not l:
      break
   f.write(l)
   f.write('\n')
f.seek(0)
summ = 0
for el in f:
    m = el.split()
    for i in m:
        summ = summ + int(i)


print(f"Сумма числел в файле  = {summ}")
f.close()


