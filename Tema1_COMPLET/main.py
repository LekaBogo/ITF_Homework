'''
Tema1
'''

# 1. Variabila este o zona de memorie careia ii asignam o valoare
# 2.
a = "Andrei"
b = 4634
c = 463464.4332
d = True
# 3.
# print(type(a))
# print(type(b))
# 4.
# if type(c) == float:
#     c = round(c)
# else:
#     print("Numarul nu este float")
# print(c)
# 5.
# print(f"Numele meu este {a}")
# print(f"Retragerea de {b} lei a fost autorizata")
# print(f"Numarul dupa rotunjire este {c}")
# print(d)
# 6.
# nume = input("Introduceti numele ")
# prenume = input("Introduceti prenumele ")
# print(f"Numele complet are {len(nume + prenume)}")
# 7.
# lungimea = int(input("Introduceti lungimea "))
# latimea = int(input("Introduceti latimea "))
# print(f"Aria dreptunghilui este {lungimea * latimea}")
# 8.
# stri = "Coral is either the stupidest animal or the smartest rock"
# z = int(input("introduceti numarul "))
# y = len(stri)
# print(stri[0:y - z])
# 9.
# a.
# strin = "Coral is either the stupidest animal or the smartest rock"
# r = strin[0:5] + strin[-5:]
# print(r)
# b.
# print(strin.count("the"))
# c.
# v = strin.replace("the", "THE")
# print(v)
# d.
# variabila = strin.find("rock")
# print(variabila)
# 10.
a = "anA"
# assert a[0].lower() == a[-1].lower()
# 11.
#a.
# numar = "0123456789"
# lista = list(numar)
# print(lista)
# for elem in lista:
#     if int(elem) % 2 == 0:
#         print(elem)
#b.
# print(numar[1::2])
# 12.
# str9d = "Coral is either the stupidest animal or the smartest"
# assert str9d.isalpha() == False
# x = str9d.find('rock')
# print(x)
# print(str9d[:x])
#
#Exercitii optionale
#1.
# a = "roberts"
# print(a[int(len(a)/2)])
#2.
# b = "radar"
# assert b == b[::-1]
#3.
# tast =str(input("Introduceti string-ul: "))
# x = tast.split(' ')
# print(x[0])
# print(type(tast))
# print(x[-1])
#4.
tastatura = input("introduceti string-ul: ")
prim = str(tastatura[0])
ultim = str(tastatura[-1])
print(prim)
lm = prim.upper()
print(lm)
y = tastatura[1:-1]
y = y.replace(prim,lm)
print(prim + y + ultim)
#5.
login = input('Please press enter in order to login')
user = input('Please enter the user:')
password = input('Please enter the password:')
sold = int(input('Please enter the current sold:'))
#print(f'Your username is {user}')
#print(f'Your password is {password}')
if user == 'Stefan' and password == 'One Piece':
    print('Welcome to your account')
    print('Your password is ' + len(password)*'*')
    print(f'Your current sold is {sold}')
option = input('Do you want to retrieve an amount of cash?\n')
if option == 'yes':
    cash = int(input('Plese select your amount of cash\n'))
    if cash > sold:
        print('You cannot withdraw')
    else  :
        print('Your transfer will reach your account right now')
elif option == 'no':
    print('See you later,alligator :)')