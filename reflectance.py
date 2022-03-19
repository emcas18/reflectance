n0 = 1
ns = 1.5
Mgf = 1.36
SiO = 1.45
AlO = 1.65
NbO = 2.0
TaO = 2.2
TiO = 2.3

n1 = TiO
n2 = TiO
n3 = TiO

r = ((n0*ns*(n2**2)) - ((n1**2)*(n3**2)))/((n0*ns*(n2**2)) + ((n1**2)*(n3**2)))

print(r)