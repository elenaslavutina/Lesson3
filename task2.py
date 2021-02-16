def dannie(name, surname, year_born, city, email, phones):
    res = name +"  " + surname +"  " + year_born +"  " + city  +"  "+ phones
    return res

print(dannie("Elena", "Slavutina", "1977", "Moskva", "slavutina@rambler.ru", "89202529241"))

def dannie2(name, surname, year_born, city, email, phones):
    print(f"Имя - {name} Фамилия - {surname}  {year_born} {city} {email} {phones}")

print(dannie2("Elena", "Slavutina", "1977", "Moskva", "slavutina@rambler.ru", "89202529241"))