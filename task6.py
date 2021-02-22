def factorial(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Укажите n чтобы узнать n! \n"))
for fact in factorial(n):
    print(fact)