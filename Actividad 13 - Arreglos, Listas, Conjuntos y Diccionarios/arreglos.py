class Arreglo:
    def __init__(self):
        self.lista = []
        self.seleccion = 0
        self.terminar = False

    def separador(self):
        print("------------------------")

    def menu(self):
        print("Seleccione la acción que desea realizar")
        self.separador()
        print("1 - Insertar")
        print("2 - Eliminar")
        print("3 - Modificar")
        print("4 - Mostrar")
        print("5 - Salir")
        self.seleccion = int(input("-> "))
        if self.seleccion < 1 or self.seleccion > 5:
            print("Opción no encontrada, coloque otra")
            self.seleccion = int(input("-> "))
        
        if self.seleccion == 5:
            self.terminar = True

    def escoger(self):
        while self.terminar != True:
            if self.seleccion == 1:
                self.insertar()
            if self.seleccion == 2:
                self.eliminar()
            if self.seleccion == 3:
                self.modificar()
            if self.seleccion == 4:
                self.mostrarLista()
            self.menu()

    def insertar(self):
        print("Inserte un valor númerico para agregar a la lista")
        nuevo = int(input("-> "))
        self.lista.append(nuevo)
    
    def eliminar(self):
        print("Selecciona la posición que desea remover de la lista")
        print(self.lista)
        posicion = int(input("-> "))
        self.lista.pop(posicion - 1)
    
    def modificar(self):
        print("Seleccione la posición de la lista que desea modificar")
        print(self.lista)
        posicion = int(input("-> "))
        print("Coloque la modificación")
        modificacion = int(input("-> "))
        self.lista[posicion - 1] = modificacion

    def mostrarLista(self):
        print(self.lista)

#--------------------------------------------------------------------------
datos = Arreglo()
datos.menu()
datos.escoger()