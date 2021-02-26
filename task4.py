from translate import Translator
translator= Translator(from_lang="english",to_lang="russian")
one = open("my_file_4.txt", "r",encoding='UTF-8')
two = open("my_file_4_2.txt", "a+",encoding='UTF-8')

for el in one:
    l = el.split()
    l[0] = translator.translate(l[0])
    l.append('\n')
    m = " ".join(l)
    print(l)
    print(m)
    two.write(m)
one.close()
two.close()


