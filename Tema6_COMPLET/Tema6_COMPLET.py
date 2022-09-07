'''
Tema 6 COMPLET
'''
# 1.
from cmath import pi
from datetime import date


class Cerc:
    raza = 2
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(self.raza)
        print(self.culoare)

    def aria(self):
        print(pi * self.raza * self.raza)

    def diametru(self):
        print(self.raza * 2)

    def circumferinta(self):
        print(2 * pi * self.raza)


cerc1 = Cerc(2, 'rosu')
cerc2 = Cerc(4, 'albastru')
cerc1.descriere_cerc()
cerc2.descriere_cerc()
cerc2.aria()
cerc2.diametru()
cerc1.circumferinta()
cerc1.aria()


# 2.
class Dreptunghi:
    lungime = 2
    latime = 10
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dreptunghi(self):
        print(self.lungime)
        print(self.latime)
        print(self.culoare)

    def aria(self):
        print(self.lungime * self.latime)

    def perimetru(self):
        print(self.lungime * 2 + self.latime * 2)

    def schimba_culoarea(self, a):
        self.culoare = a


dreptunghi1 = Dreptunghi(10, 5, 'roz')
dreptunghi2 = Dreptunghi(6, 4, 'mov')
dreptunghi1.descriere_dreptunghi()
dreptunghi2.aria()
dreptunghi1.perimetru()
dreptunghi1.schimba_culoarea('albastru')
dreptunghi1.descriere_dreptunghi()


# 3.
class Angajat:
    nume = 'Alex'
    prenume = 'Epure'
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        print(self.prenume)
        print(self.nume)
        print(self.salariu)

    def nume_complet(self):
        print(self.prenume + ' ' + self.nume)

    def salariu_lunar(self):
        print(self.salariu)

    def salariu_anual(self):
        print(self.salariu * 12)

    def marire_salariu(self, a):
        self.salariu = self.salariu + a / 100 * self.salariu


angajat1 = Angajat('Enache', 'Andrei', 1000)
angajat2 = Angajat('Roberta', 'Toader', 1500)
angajat1.descriere_angajat()
angajat2.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(10)
angajat1.salariu_lunar()


# 4.
class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma {self.sold}')

    def debitare_cont(self, suma):
        self.sold = self.sold - suma

    def creditare_cont(self, suma):
        self.sold = self.sold + suma


cont1 = Cont(9945, 'Epure Alex', 200)
cont2 = Cont(7321, 'Ancuta Bogdan', 100)
cont1.afisare_sold()
cont2.afisare_sold()
cont2.creditare_cont(200)
cont2.afisare_sold()
cont1.debitare_cont(50)
cont1.afisare_sold()
# 5.
azi = date.today()


class Factura:
    seria = 32712
    numar = None
    nume_produs = 'sampon'
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, a):
        self.cantitate = a

    def schimba_pretul(self, b):
        self.pret_buc = b

    def schimba_nume_produs(self, c):
        self.nume_produs = c

    def genereaza_factura(self):
        print(
            f'Factura seria {self.seria} numar {self.numar}\n Data: {azi} \n {self.nume_produs}  |{self.cantitate}         |{self.pret_buc} \n Telefon|Cantitate|pret bucata')


factura1 = Factura(1211, 'biscuiti', 5, 20)
factura1.genereaza_factura()
factura1.schimba_cantitatea(25)
factura1.schimba_nume_produs('alfers')
factura1.genereaza_factura()


# 6.
class Masina:
    marca = 'Audi'
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'alb', 'rosu', 'galben', 'albastru', 'mov'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(self.marca)
        print(self.model)
        print(self.viteza_maxima)
        print(self.culoare)
        print(self.viteza_actuala)
        print(self.inmatriculata)

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culo):
        if culo in self.culori_disponibile:
            self.culoare = culo

    def accelereaza(self, viteza):
        if viteza < 0:
            raise IndexError('Viteza trebuie sa fie pozitiva')
        elif viteza < self.viteza_maxima:
            self.viteza_actuala = viteza
        else:
            self.viteza_actuala = self.viteza_maxima

    def franeaza(self):
        self.viteza_actuala = 0


masina1 = Masina('A61', 250)
masina2 = Masina('B26', 300)
masina1.descrie()
masina1.inmatriculare()
masina1.descrie()
masina2.vopseste('mov')
masina2.accelereaza(100)
masina2.descrie()


# 7.
class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
    def finalizeaza_task(self,nume):
        self.todo[nume].clear()
    def afiseaza_todo_list(self):
        print(self.todo.keys())
    def afiseaza_detalii_suplimentare(self,nume_task):
        if nume_task not in self.todo:
            x = input('Doriti sa-l adaugati in Todo list?')
            if x.lower() == 'nu':
                print('La revedere')
            if x.lower() == 'da':
                y=input('Detalii task')
                self.todo[nume_task] = y
todoList1 = TodoList()
todoList1.adauga_task('wow','funtioneaza')
todoList1.afiseaza_detalii_suplimentare('gatit')
todoList1.afiseaza_todo_list()


