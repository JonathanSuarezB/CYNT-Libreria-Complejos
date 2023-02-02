import math

import libcplx as cplx

c1 = (3, -8)
c2 = (4, 6)
c3 = (5, 6)
c4 = (1, 9)
#Prueba suma
passed = 0
failed = 0

resp = cplx.sumaCplx(c1, c2)

if resp[0] == 7 and resp[1] == -2:
    passed += 1
else:
    failed += 1

resp = cplx.sumaCplx(c3, c4)

if resp[0] == 6 and resp[1] == 15:
    passed += 1
else:
    failed += 1

print("Suma -> passed:", passed, "failed:", failed)

#Prueba Producto
passed = 0
failed = 0

resp = cplx.multCplx(c1, c2)

if resp[0] == 60 and resp[1] == -14:
    passed += 1
else:
    failed += 1

resp = cplx.multCplx(c3, c4)

if resp[0] == -49 and resp[1] == 51:
    passed += 1
else:
    failed += 1

print("Producto -> passed:", passed, "failed:", failed)

#Prueba Resta
passed = 0
failed = 0

resp = cplx.restaCplx(c1, c2)

if resp[0] == -1 and resp[1] == -14:
    passed += 1
else:
    failed += 1

resp = cplx.restaCplx(c3, c4)

if resp[0] == 4 and resp[1] == -3:
    passed += 1
else:
    failed += 1

print("Resta -> passed:", passed, "failed:", failed)

#Prueba Division
passed = 0
failed = 0

resp = cplx.divisionCplx(c1, c2)

if resp[0] == -(9/13) and resp[1] == -(25/26):
    passed += 1
else:
    failed += 1

resp = cplx.divisionCplx(c3, c4)

if resp[0] == 59/82 and resp[1] == -39/82:
    passed += 1
else:
    failed += 1

print("Division -> passed:", passed, "failed:", failed)

#Prueba Modulo
passed = 0
failed = 0

resp = cplx.moduloCplx(c1)

if resp == math.sqrt(73):
    passed += 1
else:
    failed += 1

resp = cplx.moduloCplx(c3)

if resp == math.sqrt(61) :
    passed += 1
else:
    failed += 1

print("Modulo -> passed:", passed, "failed:", failed)

#Prueba Conjugado
passed = 0
failed = 0

resp = cplx.conjugadoCplx(c1)

if resp[0] == 3 and resp[1] == 8:
    passed += 1
else:
    failed += 1

resp = cplx.conjugadoCplx(c3)

if resp[0] == 5 and resp[1] == -6:
    passed += 1
else:
    failed += 1

print("Conjugado -> passed:", passed, "failed:", failed)

#Prueba Conversion entre representaciones polar y cartesiano
passed = 0
failed = 0

resp = cplx.conversionPol(c2[0],c2[1])

if resp == (math.sqrt(4**2+6**2), math.degrees(math.atan2(6,4))):
    passed += 1
else:
    failed += 1

resp = cplx.conversionCar(c4[0],c4[1])

if resp == (1*math.cos(9), 1*math.sin(9)):
    passed += 1
else:
    failed += 1

print("Conversion -> passed:", passed, "failed:", failed)

#Prueba Fase
passed = 0
failed = 0

resp = cplx.faseCpxl(c3)

if resp == math.degrees(math.atan2(6, 5)):
    passed += 1
else:
    failed += 1

resp = cplx.faseCpxl(c1)

if resp == math.degrees(math.atan2(-8, 3)):
    passed += 1
else:
    failed += 1

print("Fase -> passed:", passed, "failed:", failed)


