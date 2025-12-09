import math
import integracija as integ
m=3.37E-26 #kg
T=300 #K
k_b=1.38E-23 #J/K
konst=m/(2*k_b*T)
def maxwell(v):
    return 4*math.pi*((konst/math.pi)**1.5)*(v**2)*math.exp(-konst*v**2)
from Gauss import gauleg 
def gauss_int(a,b,n,f):
    x,w=gauleg(a,b,n)
    integral=0
    for i in range(n):
        integral += w[i]*f(x[i])
    return integral

v_sred=559.4 #m/s
lower=v_sred-50
upper=v_sred+50

with open("rezultati.txt","w") as f:
    f.write("Broj tocaka   Trapez              Simpson             Gauss-Legendre\n")
    f.write("-----------   ---------------     ---------------     ---------------\n")
    f.write(f"{10:<3d}           {integ.trapez(lower,upper,10,maxwell):<15.13f}     {integ.simpson(lower,upper,10,maxwell):<15.13f}     {gauss_int(lower,upper,10,maxwell):<15.13f}\n")
    f.write(f"{50:<3d}           {integ.trapez(lower,upper,50,maxwell):<15.13f}     {integ.simpson(lower,upper,50,maxwell):<15.13f}     {gauss_int(lower,upper,50,maxwell):<15.13f}\n")
    f.write(f"{100:<3d}           {integ.trapez(lower,upper,100,maxwell):<15.13f}     {integ.simpson(lower,upper,100,maxwell):<15.13f}     {gauss_int(lower,upper,100,maxwell):<15.13f}")
