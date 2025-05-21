class CuentaDeBanco:
    def __init__ (self, nombre, nip, saldo):
        self.nombre = nombre
        self.__nip = nip
        self.__saldo = saldo
    
    def mostrarSaldo(self):
        return self.__saldo

#---------------------------------------Iniciating 
tarjeta = CuentaDeBanco("Jaime perez", 1234, 500)
print(tarjeta.nombre)
print(tarjeta.mostrarSaldo())