input_login = str(input("Ведіть логін: "))
input_password = int(input("Ведіть пароль: "))

user1 = "Maksim"
user2 = "Vanya"
user3 = "Andrey"
user4 = "Lax"

Maksim = (10, 2, 8, 4, 9)
Vanya = (7, 4, 4, 10, 9)
Andrey = (3, 2, 5, 4, 9)
Lax = (8, 10, 7, 10, 3)

MaxPassword = 1234
VanyaPassword = 0000
AndreyPassword = 1111
LaxPassword = 9999

Yep = int()
Nope = int()

if input_login == user1 and input_password == MaxPassword:
    print("Ласкаво просимо",input_login,"!")
    print("Ваші оцінки: ",Maksim)
    for number in Maksim:
        if number > 4:
            Yep = Yep + 1
        else: Nope = Nope + 1
    print("Кількість задовільних оцінок: ",Yep)
    print("Кількість незадовільних оцінок: ",Nope)
elif input_login == user2 and input_password == VanyaPassword:
    print("Ласкаво просимо",input_login,"!")
    print("Ваші оцінки: ",Vanya)
    for number in Vanya:
        if number > 4:
            Yep = Yep + 1
        else: Nope = Nope + 1
    print("Кількість задовільних оцінок: ", Yep)
    print("Кількість незадовільних оцінок: ", Nope)
elif input_login == user3 and input_password == AndreyPassword:
    print("Ласкаво просимо",input_login,"!")
    print("Ваші оцінки: ", Andrey)
    for number in Andrey:
        if number > 4:
            Yep = Yep + 1
        else: Nope = Nope + 1
    print("Кількість задовільних оцінок: ", Yep)
    print("Кількість незадовільних оцінок: ", Nope)
elif input_login == user4 and input_password == LaxPassword:
    print("Ласкаво просимо",input_login,"!")
    print("Ваші оцінки: ", Lax)
    for number in Lax:
        if number > 4:
            Yep = Yep + 1
        else:Nope = Nope + 1
    print("Кількість задовільних оцінок: ", Yep)
    print("Кількість незадовільних оцінок: ", Nope)
else:
    print("Невірний логін або пароль")






'''
bla= int(input("Ведіть цифру: "))

if bla >= 10:
    print("cool")
else:
    print("not cool")
'''
