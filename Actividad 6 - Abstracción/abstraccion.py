class Actor:
    def __init__(self, personaje, papel):
        self.personaje = personaje
        self.papel = papel
    
    def decirDialogo(self):
        pass

class Villano(Actor):
    def decirDialogo(self):
        print("Hola soy ", self.personaje, " y soy el ", self.papel, " de la historia")

class Primario(Actor):
    def decirDialogo(self):
        print("Hola soy ", self.personaje, " y soy el ", self.papel, " de la historia")


#-----------------------------------------------------------
unRandom = Villano("Wiliam Afton", "antagonista")
otroRandom = Primario("Crying children", "Protagonista")
unRandom.decirDialogo()
otroRandom.decirDialogo()