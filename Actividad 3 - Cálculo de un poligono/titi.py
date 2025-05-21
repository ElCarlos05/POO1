from math import radians, tan
class Figura:
    def area(nLados, vLado):
        if nLados > 0:
            angulo = radians(360 / (nLados * 2))
            apotema = vLado / (2 * (tan(angulo)))
            p = vLado * nLados
            areaFigura = (p * apotema) / 2
        print ("El area de la figuranes", areaFigura)

    def perimetro(nLados, vLado):
        perimetroFigura = vLado * nLados
        print ("El perimetro de la figura es", perimetroFigura)

#--------------------------------------------------------
unaFigura = Figura
unaFigura.area(2,6)
unaFigura.perimetro(8,7)