class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        return "guau"

class Gato(Animal):
    def hacerSonido(self):
        return "miau"

class Vaquita(Animal):
    def hacerSonido(self):
        return "Muuu"

#-------------------------------------Progaming iniciating------------------------------------------
unAnimal = Perro("Abdiel negrooooo")
otroAnimal = Gato("Brianstorm")
elAnimal = Vaquita("Varesa")
print(unAnimal.nombre, " hace ", unAnimal.hacerSonido())
print(otroAnimal.nombre, " hace ", otroAnimal.hacerSonido())
print(elAnimal.nombre, " hace ", elAnimal.hacerSonido())