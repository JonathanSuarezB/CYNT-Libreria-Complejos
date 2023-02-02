import math

def sumaCplx(c1,c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    resultado = (real,img)
    return resultado

def multCplx(c1,c2):
    real = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    img = (c1[0]*c2[1])+(c1[1]*c2[0])  
    resultado = (real,img)
    return resultado

def restaCplx(c1,c2):
    real = c1[0] - c2[0]
    img = c1[1] - c2[1]
    resultado = (real,img)
    return resultado

def divisionCplx(c1,c2):
    real = (c1[0]*c2[0]+c1[1]*c2[1])/((c2[0]**2)+(c2[1]**2))
    img = (c1[1]*c2[0]-c1[0]*c2[1])/((c2[0]**2)+(c2[1]**2))
    resultado = (real, img)
    return resultado

def moduloCplx(c):
    modulo = math.sqrt(c[0]**2+c[1]**2)
    return modulo

def conjugadoCplx(c):
    return (c[0], -c[1])

def conversionCar(magnitud, angulo):
    a = magnitud * math.cos(angulo)
    b = magnitud * math.sin(angulo)
    return a, b

def conversionPol(a, b):
    magnitud = math.sqrt(a**2+b**2)
    angulo = math.degrees(math.atan2(b,a))
    return magnitud, angulo

def faseCpxl(c):
    fase = math.degrees(math.atan2(c[1], c[0]))
    return fase

def prettyPcplx(c):
    if c[1] > 0:
        print("{} + {}i".format(c[0], c[1]))
    else:
        print("{} - {}i".format(c[0], -c[1]))

#if __name__ == '__main__':

    #prettyPcplx(sumaCplx((3,-8),(4,6)))
    #prettyPcplx(multCplx((2,-3),(-1,1)))
    #prettyPcplx(restaCplx((3,-8),(4,6)))
    #prettyPcplx(divisionCplx((3,-8),(4,6)))
    #prettyPcplx(conjugadoCplx((3,-7)))
    #print(moduloCplx((-2,-3)))
    #print(conversionCar(12, 45))
    #print(conversionPol(4,6))
    #print(faseCpxl((10,5)))
