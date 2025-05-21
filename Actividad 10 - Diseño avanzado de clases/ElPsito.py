class pisto:
    def __init__(self,hielera, hielera2):
        self.__hielera = hielera
        self.hielera2 = hielera2
        
    def pistear(self):
        self.__hielera =  "im going back to 505"
        return self.__hielera
    
    def pistear2(self):
        self.hielera2 = "nah, esta vacia boludo"
        return self.hielera2
    
    #---------------------------------
fiesta = pisto("Carton en hielera", "Unas cuantas frias")     
print(fiesta.pistear())
print(fiesta.pistear2())