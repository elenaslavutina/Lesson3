def dannie(name, surname, year_born, city, email, phones):
    return name +"  " + surname +"  " + year_born +"  " + city  +"  "+ phones


print(dannie("Elena", "Slavutina", "1977", "Moskva", "slavutina@rambler.ru", "89202529241"))

def dannie2(name, surname, year_born, city, email, phones):
    print(f"Имя - {name} Фамилия - {surname}  {year_born} {city} {email} {phones}")

print(dannie2("Elena", "Slavutina", "1977", "Moskva", "slavutina@rambler.ru", "89202529241"))