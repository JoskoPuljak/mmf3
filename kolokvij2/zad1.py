import numpy as np
import math
m=3.37e-26 #kg
T=300 #K
k=1.38064852e-23 
vsr=np.sqrt(8*k*T/(np.pi*m))
def maxwell(v):
    return (m/(2*np.pi*k*T))**(3/2)*4*np.pi*(v**2)*np.exp((-m*v**2)/(2*k*T))

def gauleg(x1, x2, n):
    
 #   Za zadanu donju i gornju granicu integracije x1 i x2, i stupanj polinoma na ova funkcija vraća listu x i w duljine n, koji sadrže nultočke 
 #   i težine za kvadratur Gauss-Legendre kvadraturu na zadanom intervalu.  
  
    EPS = 1e-6  # Preciznost 
    m = (n + 1) // 2 # Broj simetričnih točaka (samo je potrebno izračunati polovicu nultočke zbog simetrije, uzima se cjelobrojni dio, +1 je zbog neparnih n-ova da se uključi srednja točka)
    xm = 0.5 * (x2 + x1) # Sredina intervala
    xl = 0.5 * (x2 - x1) # Pola širine intervala

    # Inicijalizacija
    x = np.zeros(n) # Nultočke
    w = np.zeros(n) # Težine

    # Pronalazak nultočke i težine

    for i in range(1, m + 1): 
        z = math.cos(math.pi * (i - 0.25) / (n + 0.5)) # Početna aproksimacija nultočke (periodička funkcija na intervalu [-1,1])
        while True: # Newton-Raphson metoda za pronalazak nultočke
            p1 = 1.0 # Prvi polinom
            p2 = 0.0  # Drugi polinom
            for j in range(1, n + 1):
                p3 = p2 # Privremena varijabla za pohranu prethodnog polinoma
                p2 = p1 # Privremena varijabla za pohranu trenutnog polinoma
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j  # Rekurzivna formula za Legendreove polinome (budući polinom)
            pp = n * (z * p1 - p2) / (z * z - 1.0) # Rekurzivna formula za derivaciju Legendreovog polinoma
            z1 = z # Pohrana prethodne aproksimacije
            z = z1 - p1 / pp #Newton-Raphson ažuriranje
            if abs(z - z1) < EPS: # Provjera konvergencije koja garantira preciznost
                break #Izlazak iz petlje ako je postignuta željena preciznost 
        x[i - 1] = xm - xl * z # Simetrična nultočka (dobivena skaliranjem i pomicanjem)
        x[n - i] = xm + xl * z # Druga simetrična nultočka (s druge strane sredine intervala) (i ide od nule kako bi se ispunile simetrijske točke)
        w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp) # Težina za nultočku
        w[n - i] = w[i - 1] #Težina za simetričnu nultočku je identična
    
    return x, w # Vraćanje nultočke i težina
n=10
x,w=gauleg(0,vsr,n)
integral=0
for i in range(n):
    integral+=w[i]*maxwell(x[i])
print(integral)
