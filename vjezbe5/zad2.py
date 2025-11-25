import numpy as np
import polint as pol
import matplotlib.pyplot as plt
import scipy.interpolate as sp
#otvori i pretvori datoteku V(H-H).txt u V(H-H)_AK.txt s pretvorbom jedinica
with open("V(H-H)_AK.txt", "w") as file1:
    file1.write("#r/A       V/K\n")
    file1.write("#------    -------------\n")
    with open("V(H-H).txt", "r") as file2:
        check=1
        for line in file2:
            if check>2:
                part=line.split("   ")
                r=float(part[0])*0.52917721092
                V=float(part[1])*315775.04
                file1.write(f" {r:<8.4f}  {V:<13.6f}\n")
            check+=1

#učitane podatke iz V(H-H)_AK.txt u liste
with open("V(H-H)_Ak.txt", "r") as file3:
    x_lista=[]
    y_lista=[]
    check=0
    for line in file3:
        if check >1:
            x_lista.append(float(line.split("   ")[0].strip()))
            y_lista.append(float(line.split("   ")[1].strip()))
        check +=1

#funkcija za Lagrangeovu interpolaciju
def lagrange(xi,yi,x):
    from lagrange import linterpol
    p_list=linterpol(xi,yi,x)
    return p_list[-1]

#izračun interpoliranih vrijednosti na zadanom intervalu i spremanje u datoteku
interval=np.linspace(2.81,9.81,71)
lista_lagrange=[]
lista_neville=[]
lista_dV_neville=[]
lista_spline=[]
with open("V(H_H)_inter.txt","w") as file4:
    file4.write("#r/A       V/K_Lag        V/K_Nev        dV/K_Nev       V/K_spl        deltaV/K \n")
    file4.write("#------    ----------     ----------     ----------     ----------     ----------\n")
    for x in interval:
        V_lagrange=lagrange(x_lista,y_lista,x)
        lista_lagrange.append(V_lagrange)
        V_neville,dV_neville=pol.polint(x_lista,y_lista,len(x_lista),x)
        lista_neville.append(V_neville)
        lista_dV_neville.append(abs(dV_neville))
        V_spline=sp.CubicSpline(x_lista,y_lista,bc_type=((1,185.45048),(1,0.0309242)))(x)
        lista_spline.append(V_spline)
        V_diff=V_spline - V_neville
        file4.write(f" {x:<8.4f}  {V_lagrange:<13.6f}  {V_neville:<13.6f}  {dV_neville:<13.6f}  {V_spline:<13.6f}  {V_diff:<13.6f}\n")
#crtanje rezultata
plt.scatter(x_lista,y_lista,label='Data Points',color='blue',facecolor='none',s=50)
plt.ylabel('V (K)')
plt.xlabel('r (A)')
plt.errorbar(interval,lista_neville,yerr=lista_dV_neville,fmt='o',color='green',markersize=3,capsize=2)
plt.scatter(interval,lista_lagrange,color='red',s=20)
plt.legend([r"$(r_i,V_i)$",'Lagrange','Neville'])
plt.xlim(1,10)
plt.ylim(-10,10)
plt.savefig('V(H-H)_interpolation.png')
plt.show()

plt.scatter(x_lista,y_lista,label='Data Points',color='blue',facecolor='none',s=50)
plt.ylabel('V (K)')
plt.xlabel('r (A)')
plt.scatter(interval,lista_lagrange,color='red',s=30)
plt.scatter(interval,lista_neville,color='green',s=20)


plt.scatter(interval,lista_spline,color='yellow',s=10)
plt.legend([r"$(r_i,V_i)$",'Lagrange','Neville','Spline'])
plt.xlim(1,10)
plt.ylim(-10,10)
plt.savefig('V(H-H)_interpolation_spline.png')
plt.show()
