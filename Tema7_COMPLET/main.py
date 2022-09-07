'''
Tema7_COMPLET
'''


# 1.
from abc import ABC
from cmath import pi


class FormaGeometrica(ABC):
    pi = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):
    __latura = 1

    def __init__(self,latura):
        self.latura = latura

    def get_latura(self):
        return self.__latura

    def set_latura(self, selecteaza_latura):
        self.__latura = selecteaza_latura

    def deleter_patrat(self):
        print('Am sters patratul')
        self.__latura = None
    def aria(self):
        print(f'Aria este {self.__latura*self.__latura} m^2')
#!
p1=Patrat(3)
p1.set_latura(2)
p1.aria()
# 2.
class Cerc(FormaGeometrica):
    __raza = 1
    def __init__(self,raza):
        self.raza = raza
    def get_raza(self):
        return self.__raza

    def set_raza(self, selecteaza_raza):
        self.__raza = selecteaza_raza

    def deleter_cerc(self):
        print('Am sters patratul')
        self.__latura = None
    def aria(self):
        print(f'Aria este {self.__raza*self.__raza*pi} m^2')
    def descrie(self):
        print("Eu nu am colturi")
c1=Cerc(50)
c1.aria()
c1.set_raza(5)
c1.aria()