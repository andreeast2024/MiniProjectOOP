"""
Miniproiect Piloni OOP
"""

"""
Creaza o clasa abstracta numita Gradinita,
cu urmatoarele metode abstracte:
activitate_practica()
ora_de_somn()
"""
from abc import ABC, abstractmethod

class Gradinita(ABC):

     @abstractmethod
     def activitate_practica(self):
         pass

     @abstractmethod
     def ora_de_somn(self):
         pass

"""
Implementati doua clase, numite GradinitaPublica si
GradinitaPrivata care sa implementeze clasa abstracta Gradinita.

GradinitaPublica:
activitate_practica() - printeaza "copiii invata sa deseneze"
ora_de_somn() - printeaza "copiii trebuie sa doarma la ora 5"

GradinitaPrivata:
activitate_practica() - printeaza "copiii invata sa modeleze cu plastilina"
"""


class GradinitaPublica(Gradinita):

    def __init__(self):
        self.elevi = {}

    def activitate_practica(self):
        print("copiii invata sa deseneze")

    def ora_de_somn(self):
        print("copiii trebuie sa doarma la ora 5")

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere):
        self.elevi[nume_elev] = {nume_elev:{"varsta": varsta_elev, "an_inscriere":an_inscriere}}
        print(self.elevi[nume_elev])


class GradinitaPrivata(Gradinita):

    def __init__(self, valoare_taxa = 5000):
        self.elevi = {}
        self.__valoare_taxa = valoare_taxa

    def activitate_practica(self):
        print("copiii invata sa modeleze cu plastilina")

    def ora_de_somn(self):
        print("copiii trebuie sa doarma la ora 5")

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere, taxa_platita):
        self.elevi[nume_elev] = {nume_elev:{"varsta": varsta_elev, "an_inscriere":an_inscriere, "taxa_platita": taxa_platita}}
        print(self.elevi[nume_elev])

    @property
    def taxa(self):
        return self.__valoare_taxa

    @taxa.getter
    def taxa(self):
        print("Getter")
        return f'{self.__valoare_taxa} lei'

    @taxa.setter
    def taxa(self, taxa_noua):
        print("Setter")
        if taxa_noua < 5000:
            print("Taxa e de 5000 lei. Trebuie achitata toata suma o data.")
        elif taxa_noua > 5000:
            self.__valoare_taxa = 5000
            diferenta_taxa = taxa_noua - self.__valoare_taxa
            print(f"Taxa a fost platita cu succes, iar diferenta returnata este de {diferenta_taxa} lei.")
        else:
            self.__valoare_taxa = taxa_noua
            print("Taxa a fost platita cu succes")


"""
3.
a. Rulati codul. Se intampla ceva?
b. Instantiati un obiect din clasa GradinitaPublica si rulati codul.
Se printeaza ceva pe ecran? De ce?
c. Apelati metoda activitate_practica() si rulati codul. Ce observati?
d. Instantiati un obiect din clasa GradinitaPrivata si rulati codul.
De ce va da eroare? Cum putem rezolva eroarea?
"""
gradinita_publica = GradinitaPublica()
gradinita_publica.ora_de_somn()
gradinita_publica.activitate_practica()
gradinita_privata = GradinitaPrivata()
gradinita_privata.activitate_practica()

"""
4. Creati o clasa, GradinitaPublica25, care sa mosteneasca clasa GradinitaPublica.
Implementati metoda activitate_practica() in felul urmator:
- printati mesajul "Copiii se joaca in curte pe balansoar.

- Instantiati un obiect din clasa GradinitaPublica25.
- Prin intermediul obiectului instantiat, apelati toate metodele disponibile
si observati rezultatele.
"""

class GradinitaPublica25(GradinitaPublica):

    def activitate_practica(self):
        print(f"Copiii se joaca in curte pe balansoar")

gradinitapublica25 = GradinitaPublica25()
gradinitapublica25.activitate_practica()
gradinitapublica25.ora_de_somn()
"""
5. Adauga un atribut pe obiect, numit elevi,
in clasele GradinitaPublica si GradinitaPrivata.
Initial, acesta va fi un dictionar gol.

Implementeaza o metoda in fiecare in aceste clase,
numita adauga_elev:

 In clasa GradinitaPublica, primeste urmatorii parametri:
- nume_elev, varsta_elev, an_inscriere
- salveaza aceste informatii in atributul elevi, sub forma
{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>}

 In clasa GradinitaPrivata, primeste urmatorii parametri:
- nume_elev, varsta_elev, an_inscriere, taxa_platita
- salveaza aceste informatii in atributul elevi, sub forma
{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>, "taxa_platita": <taxa_platita"}

- apeleaza aceasta metoda pe un obiect din fiecare clasa pentru a ilustra
polimorfismul
"""
gradinita_publica.adauga_elev(nume_elev="Alex",varsta_elev=13,an_inscriere=2000)
gradinita_publica.adauga_elev(nume_elev="Gabor",varsta_elev=16,an_inscriere=2020)
gradinita_privata.adauga_elev(nume_elev="Dumi",varsta_elev=10,an_inscriere=2010,taxa_platita="DA")


"""
6. 
Adauga un atribut privat in clasa GradinitaPrivata,
numit valoare_taxa.
Creeaza o proprietate care sa incapsuleze atributul privat valoare_taxa:
- sa aiba un getter:
    - sa returneze taxa ca string cu moneda atasata ("5000 lei")
- sa aiba un setter:
    - care verifica noua taxa ce se doreste a fi platita:
    - daca e mai mica decat 5000, nu se seteaza noua taxa, si se afiseaza mesajul 
"Taxa e de 5000 lei. Trebuie achitata toata suma o data."
    - daca e mai mare de 5000, setam taxa ca fiind 5000 si afisam un mesaj
in care spunem utilizatorului ca taxa e de 5000 lei, a fost platita cu succes si
restul de bani ce ii dam inapoi.
    - daca e exact 5000, atunci setam taxa.
"""

print(gradinita_privata.taxa)
gradinita_privata.taxa = 3000
print(gradinita_privata.taxa)
gradinita_privata.taxa = 11000
print(gradinita_privata.taxa)


