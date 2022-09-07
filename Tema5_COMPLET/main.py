'''
Tema5_COMPLET + ToDo sesiune live
'''
# 1.
from cmath import pi


def suma(a, b):
    return a + b


print(suma(4, 12))


# 2.
def paritate(a):
    if a % 2 == 0:
        return True
    else:
        return False


# 3.
def nr_carac(nume, prenume, nume_mijlociu):
    return len(nume) + len(prenume) + len(nume_mijlociu)


print(nr_carac('alex', 'wow', 'ww'))


# 4.
def aria_dreptungi(a, b):
    return a * b


# 5.
def aria_cerc(r):
    return pi * r * r


print(aria_cerc(1))
# 6.
ok = 1
caracter = input("Introdu caracterul: ")


def caut(a):
    for i in range(len(a)):
        if a[i] == caracter:
            print("Gasit!")
            ok = 0
    if ok == 1:
        print("Nu a fost gasit")


caut("Alex")


# 7.
def afis(a):
    upper = 0
    lower = 0
    for i in a:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
    print(f'Nr de caractere lower case este {lower}')
    print(f'Nr de caractere upper case este {upper}')


afis('ALexA')


# 8.
def pozitive_list(a):
    b = []
    for i in a:
        if i >= 0:
            b.append(i)
    else:
        print(b)


pozitive_list([3, 6, -2, -10, 3])


# 9.
def functie_crazy(x, y):
    if x == y:
        print(f"Numerele sunt egale.")
    elif x < y:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
    else:
        print(f"Primul număr {x} este mai mare decat al doilea nr {y}")


functie_crazy(5, 8)


# 10.
def functie_set(set, b):
    if b in set:
        print("Nu am adaugat numărul în set. Acesta există deja")
        return False
    else:
        print("Am adaugat numărul nou în set")


functie_set({1, 2, 3, 4, 5, 6}, 7)
# 11.
lunile = {
    'ianuarie': 31,
    'februarie': 28,
    'martie': 31,
    'aprilie': 30,
    'mai': 31,
    'iunie': 30,
    'iulie': 31,
    'august': 31,
    'septembrie': 30,
    'octombrie': 31,
    'noiembrie': 30,
    'decembrie': 31
}


def lunile_anului(a={}):
    x = input('Introduceti luna: ')
    print(a.get(x))


lunile_anului(lunile)


# 12.
def operatii(a, b):
    print(f'Suma este {a + b}')
    print(f'Diferenta este {a - b}')
    print(f'Inmultirea este {a * b}')
    print(f'Impartirea este {a / b}')


operatii(5, 6)
# 13.
paste = [1, 3, 1, 5, 9, 7, 7, 5, 5]
dict = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}


def numara(l):
    for i in range(len(paste)):
        if paste[i] == 0:
            dict['0'] = dict['0'] + 1
        elif paste[i] == 1:
            dict['1'] = dict['1'] + 1
        elif paste[i] == 2:
            dict['2'] = dict['2'] + 1
        elif paste[i] == 3:
            dict['3'] = dict['3'] + 1
        elif paste[i] == 4:
            dict['4'] = dict['4'] + 1
        elif paste[i] == 5:
            dict['5'] = dict['5'] + 1
        elif paste[i] == 6:
            dict['6'] = dict['6'] + 1
        elif paste[i] == 7:
            dict['7'] = dict['7'] + 1
        elif paste[i] == 8:
            dict['8'] = dict['8'] + 1
        else:
            dict['9'] = dict['9'] + 1
    else:
        print(dict)


numara(paste)


# 14.
def maxim(a, b, c):
    if a > b and a > c:
        print("a e cel mai mare")
    elif b > a and b > c:
        print("b e cel mai mare")
    else:
        print("c e cel mai mare")


# 15.
def suma_num(a):
    s = 0
    for i in range(a):
        s = s + i
    else:
        s += a
        print(s)


suma_num(5)


# 16.
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


print(intersection(paste, [4, 6, 9]))
# 17.
def reducere(a):
    if a < 0:
        print("Introduceti un pret pozitiv")
    c = a - 10/100 *a
    return c
print(reducere(100))
# 18.
import time;
def local_time():
    localtime = time.asctime( time.localtime(time.time()) )
    print ("Local current time :", localtime)
# 19.
def calc_zi(a):
    if a < 359:
        print(f"Mai sunt {359 - a}")
    elif a > 359:
        print(f'Mai sunt {365 - a + 359} zile')
    else:
        print("Este craciunul!!!!!!!!!!!!!!!")
calc_zi(20)

#ToDo sesiune live
'''
Conectare la o baza de date de tip dictionar
'''
n = input("Introdu numele de utilizator: ")
m = input("Introdu parola: ")
def conectare(user,parola):
    for item in dic:
        if dic.get(item) == parola:
            print("Te-ai conectat cu succes!")
            break
    else:
        print("Ai introdus date gresite!")

dic = {
    'Leka' : 'Bogo',
    'Raul' : 'Panait',
    'Robert': 'Enache'}
conectare(n,m)


#Funtia de chat
def chat(a,b):
    a = input("Scrie aici mesajul pe care vrei sa-i afisezi grupului: ")
    print (f"{b}:{a}")
chat(2,n)

#people list function
def people_list(a='ON'):
    if a == "ON":
        print("People list is here")
    else:
        print("People list is hidden")

#call funtions
def leave_call(a):
    a=input("1 pentru a mentine apelul/0 pentru a inchide apelul")
    if a == 1:
        print("The call is still going")
    else:
        print("The call has ended")