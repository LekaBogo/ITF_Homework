'''
Tema2 Complet
'''
# 1.
# If else este un bloc care exectuta o comanda in funtie de ramura pe care se incadreaza
# 2.
from random import randrange

# x = int(input("Introduceti numarul X: "))
# if x > 0:
#     print("X e numar natural")
# else:
#     print("X nu e numar natural")
# 3.
# if x > 0:
#     print("X e numar pozitiv")
# elif x < 0:
#     print("X e numar negativ")
# else:
#     print("X este numar neutru")
# 4.
# if x > -2 and x < 13:
#     print("Numarul se afla in acest interval")
# else:
#     print("Numarul nu se afla in acest interval")
# 5.
# y = int(input("introduceti numarul Y: "))
# if x-y > 5:
#     print("Diferenta e mai mica de 5")
# else:
#     print("Diferenta nu e mai mica de 5")
# 6.
# if not (x >= 5 and x<= 27) == True:
#     print("Numarul NU este in acest interval")
# else:
#     print("Numarul se afla in acest interval")
# #7.
# if x == y:
#     print("Numerele sunt egale")
# elif x-y > 0:
#     print("X este mai mare")
# else:
#     print("Y este mai mare")
# 8.
# z = int(input("introduceti numarul Z: "))
# if x == y == z:
#     print("Triunghiul este echilateral")
# elif x == y or x == z or z==y:
#     print("Triunghiul este isoscel")
# else:
#     print("Triunghiul este oarecare")
# 9.
# a = input("Introdu litera: ")
# if a.lower() == "a" or a.lower() == "e" or a.lower() == "i" or a.lower()== "o" or a.lower() == "u":
#     print("Litera este vocala")
# else:
#     print("Litera nu e vocala")
# 10.
# nota = int(input("Introduceti nota: "))
# if nota > 9:
#     print("A")
# elif nota > 8:
#     print("B")
# elif nota > 7:
#     print("C")
# elif nota > 6:
#     print("D")
# elif nota > 4:
#     print("E")
# elif nota < 4:
#     print("F")
# 11.
# if x > 1000:
#     print("Numarul are minim 4 cifre")
# else:
#     print("Numarul nu are 4 cifre")
# 12.
# if x > 100000 and x < 999999:
#     print("Numarul are exact 6 cifre")
# else:
#     print("Numarul nu are exact 6 cifre")
# # 13.
# if x % 2 == 0:
#     print("X este numar par")
# else:
#     print("Numarul este impar")
# 14.
# if x > y and x > z:
#     print("X este cek mai mare numar")
# elif y > x and y > z:
#     print("Y este cel mai mare numar")
# else:
#     print("Z este cel mai mare numar")
# # 15.
# if x + y + z == 180:
#     print("Triunghiul este valid")
# else:
#     print("Triunghiul nu este valid")
#16.
# varsta =int(input("Introduceti varsta: "))
# insotit_mama = input("Insotit de mama? ")
# insotit_tata = input("Insotit de tata? ")
# pasaport = input("Detineti pasaport? ")
# act_mama= input("Detineti act permisiune mama? ")
# act_tata= input("Detineti act permisiune tata? ")
# if varsta >= 18 and pasaport.lower() == "da":
#     print("Va puteti imbarca")
# elif varsta < 18 and insotit_mama.lower()=="da" and insotit_tata.lower()=="da":
#     print("Va puteti imbarca")
# elif varsta < 18 and insotit_mama.lower()=="da" and act_tata.lower() == "da":
#     print("Va puteti imbarca")
# elif varsta < 18 and insotit_tata.lower()=="da" and act_mama.lower() == "da":
#     print("Va puteti imbarca")
# else:
#     print("Nu va puteti imbarca")
#17
# dice_roll = randrange(1,6)
# alegere = int(input("Introduceti numarul care va fi pe fata zarului: "))
# if alegere > dice_roll:
#     print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {alegere} dar a fost {dice_roll}")
# elif alegere < dice_roll:
#     print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {alegere} dar a fost {dice_roll}")
# else:
#     print(f"Ai ghicit.Ai ales {alegere} si zarul a fost {dice_roll}")