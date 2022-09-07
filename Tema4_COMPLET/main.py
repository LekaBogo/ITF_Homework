'''
Tema 4 COMPLET + #ToDo sesiune live
'''

#1.
from random import randint

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat',
'Trabant', 'Opel']
x = 0
# for i in masini:
#     print(f'Masina mea preferata este {i}')
# while len(masini) != 0:
#     print(f'Masina mea preferata este {x}')
#     if len(masini) == 0:
#         break
#     else:
#         x = masini[0]
#         masini.remove(x)
#2.
# for i in range(len(masini)-2):
#     masini[i+1] = masini[i+1].upper()
# else:
#     print(masini)
#3.
for masina in masini:
    if masina == 'Mercedes':
        print("Am gasit masina!!!!!!!!!!!!!!!")
        break
    print(f'Am gasit masina {masina}')
#4.
for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        continue
    print(f"S-ar putea sa va placa masina {masina}")
#5.
masini_vechi = []
for i in range(len(masini)):
    if masini[i]=="Lastun" or masini[i] == "Trabant":
        masini_vechi.append(masini[i])
        masini[i] = "Tesla"
else:
     print(f'Modele vechi: {masini_vechi}')
     print(f'Modele noi: {masini}')
#6.
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
for i in pret_masini:
    if pret_masini[i] < 15000:
        print(i)
for i in pret_masini:
    print(i, pret_masini[i])
for i in pret_masini:
    if pret_masini[i] < 15000:
        print(f'Puteti alege masina {i}')
#7.
numere = [5,7,3,9,3,3,1,0,-4,3]
for i in numere:
    if i == 3:
        x += 1
else:
    print(f'Numarul 3 apare de {x} ori')
#8.
sum = 0
for i in numere:
    sum = sum + i
else:
    print(sum)
#9.
max=0
for i in numere:
    if i > max:
        max = i
else:
    print(max)
#10.
for i in range(len(numere)):
    numere[i] = -numere[i]
else:
    print(numere)
#11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if i > 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)
    if i %2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
else:
    print(numere_impare)
    print(numere_pare)
    print(numere_pozitive)
    print(numere_negative)
#12.
for n in range(len(numere)-1, 0, -1):
        for i in range(n):
            if numere[i] > numere[i + 1]:
                numere[i], numere[i + 1] = numere[i + 1], numere[i]
else:
    print(numere)
#13.
numar_ghicit = int(input("Introduceti numarul: "))
numar_secret = 0
while numar_secret != numar_ghicit:
    numar_secret = randint(1, 30)
    if numar_ghicit > numar_secret:
        print("Nr secret e mai mic")
    elif numar_ghicit < numar_secret:
        print("Nr secret e mai mare")
else:
    print("Felicitari! Ai ghicit")
#14.
numar = int(input("Introduceti numarul: "))
for i in range(numar):
    for j in range(i+1):
        print(i+1, end="")
    print("\n")
#15.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for item in tastatura_telefon:
    for i in item:
        print(f"Cifra curent este {i}")

# ToDo sesiune live
my_dict = {
    "year": 2000,
    "Nume": "Bogoros",
    "Prenume": ["Vasile", "Alexandru"],
    "Oras": {
        "Localitate": "Schela",
        "Judet": "Galati"},
    "Cont_La_Banca": [{"Cont1": 'BCR',
                       "IBAN": 1234,
                       "PIN": 6969},
                      {"Cont2": 'Nume',
                       "IBAN": 12353461,
                       "PIN": 4444449},
                      {"Cont3": 'BT',
                       "IBAN": 1234,
                       "PIN": 6969},
                      {"Cont4": 'ING',
                       "IBAN": 1234545345,
                       "PIN": 6875}]
}
assert my_dict.get("year") == 2000
my_dict.update({"year": 2010})
print(my_dict.values())

my_list = [4, 25, 22, 3, 7, 255, 97, 92, 100]
my_list.sort()
# my_list.reverse()
for element in reversed(my_list):
    if element % 2 == 0:
        print(element)
        break
# Apart pacanele
# x = randint(1, 10)
# c = True
# while c:
#
#     z = int(input("Introdu un numar in intervalul [1,10]. "))
#     if z < 1 or z > 10:
#         z = int(input("Introduceti din nou numarul care trebuie sa fie in intervalul [1,10]"))
#     if z == x:
#         print("Esti norocos!!!!!!!")
#         break
#     else:
#         print("Try again")
# else:
#     print("Alege alt numar")
list2 = []
pseudolist = ['salut', 2, 3534, 2, 'mama', True, 333, 'tTa', 'tata', 'tata']
for pseudoelement in pseudolist:
    if pseudolist.count(pseudoelement) > 1:
        list2.append(pseudoelement)
        print(pseudoelement)
print(list(set(list2)))

# Selection sort
list3 = [1, 6436, 4, 346, 3246, 78, 34, 5]


def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


size = len(list3)
selectionSort(list3, size)
print('Sorted Array in Ascending Order:')
print(list3)