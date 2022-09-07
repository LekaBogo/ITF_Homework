'''
Tema 3 + ToDo sesiunea 3
'''
import numpy as np
#1.
#x = int(input("Introduceti numarul X: "))
note_muzicale = ['do','re','mi','fa','so','la','si','do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
#2.
# Do apare de 2 ori
#3.
a = [3,1,0,2]
b = [6,5,4]
c = a + b
print(c)
#4.
c.sort()
print(c)
c.remove(0)
print(c)
#5.
if len(c) > 1:
    print("Lista nu este goala")
else:
    print("Lista este goala")
#6.
#'del(c) pentru a sterge lista'
c.clear()
#7.
if len(c) > 1:
    print("Lista nu este goala")
else:
    print("Lista este goala")
#8.
dict1 ={
    'Ana':8,
    'Gigel':10,
    'Dorel':5
}
print(dict1.keys())
#9.
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")
#10.
dict1.update({"Dorel":6})
print(f"Dorel a luat nota {dict1['Dorel']}")
#11.
del dict1['Gigel']
dict1.update({'Ionica':9})
print(dict1.keys())
#12.
zile_sapt = {'luni','marti','miercuri','joi','vineri','sambata','duminica'}
weekend = {'sambata','duminica'}
zile_sapt.add('luni')
print(zile_sapt)
#13.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii')
else:
    print('Weekend nu este un subset al zilelor din săptămânii')
#14.
print(zile_sapt.difference(weekend))
#15.
print(zile_sapt.intersection(weekend))
#16.
jucatori = ['Alex','Robert','Raul']
jucator = input("Introduceti un jucator: ")
schimbari_player =int(input("Introduceti numarul de schimbari: "))
schimbari_max = 3
x =input("Introduceti numele jucatorului pe care doriti sa-l schimbati: ")
if x in jucatori and schimbari_player < schimbari_max:
    jucatori.remove(x)
    jucatori.append(jucator)
    print(f'A iesit {x}.A intrat {jucator}. Mai ai {schimbari_player -1 }')
else:
    print("Jucatorul nu exista in teren")

#ToDo din sesiunea live
# afisare lista fara duplicate
mylist = ["apple", 1, 5, True, 5, 12, "Pear", "apple"]
list = list(dict.fromkeys(mylist))
# print(list)
# slicing pe lista
# print(mylist[-2])
# print(mylist[3:7])
# print(mylist[3:8:2])

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(f'Original Array:\n{arr1}')

arr1_transpose = arr1.transpose()

# print(f'Transposed Array:\n{arr1_transpose}')

mymatrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
mymatrix_transpose = mymatrix.transpose()
print(mymatrix_transpose)
mylist.append('x')
print(mylist)
my_dict = {
    "year": 2000,
    "Nume":"Bogoros",
    "Prenume": ["Vasile","Alexandru"],
    "Oras" : {
        "Localitate":"Schela",
        "Judet":"Galati"},
    "Cont_La_Banca":[{"Cont1": 'BCR',
                      "IBAN" : 1234,
                      "PIN" : 6969},
                     {"Cont2": 'Nume',
                      "IBAN" : 12353461,
                      "PIN" : 4444449},
                     {"Cont3": 'BT',
                      "IBAN" : 1234,
                      "PIN" : 6969},
                     {"Cont4": 'ING',
                      "IBAN" : 1234545345,
                      "PIN" : 6875}]
}
print(my_dict.keys())
print(my_dict["Cont_La_Banca"])