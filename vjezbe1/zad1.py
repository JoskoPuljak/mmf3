import numpy as np
def exponentialerror(x,epsilon):
    sa=1.
    sb=1.
    sc=1.
    xn=1.
    f=1.
    k=0
    c=1.
    sk=1.
    while c>=epsilon:
        k=k+1
        xn=xn*x
        f=f*k
        c=xn/f
        sk=sk*(-x/k)
        if k%2==0:
            sa=sa+c
        else:
            sa=sa-c
        sb=sb+sk
        sc=sc+c
    file=open ("rezultati.txt", "a")
    file.write(f"{x:3d} {sa:15.3e} {sb:15.3e} {1/sc:15.3e} {np.exp(-x):15.3e} {k:3d} \n")
    file.close()
    print(x,sa,sb,1/sc,np.exp(-x),k)
    

#1e-10 greska, svi x-evi
file=open ("rezultati.txt", "a")
#file.write(f"{x:3d} {sa:15.3e} {sb:15.3e} {1/sc:15.3e} {np.exp(-x):15.3e} {k:3d} \n")
file.close()
for i in range (0,101,10):
    exponentialerror(i,1e-10)
#1e-50 greska, svi x-evi
for i in range (0,101,10):
    exponentialerror(i,1e-50)
def exponentialsteps(x,epsilon):
    sa=1.
    sb=1.
    sc=1.
    xn=1.
    f=1.
    k=0
    c=1.
    sk=1.
    while c>=epsilon:
        k=k+1
        xn=xn*x
        f=f*k
        c=xn/f
        sk=sk*(-x/k)
        if k%2==0:
            sa=sa+c
        else:
            sa=sa-c
        sb=sb+sk
        sc=sc+c
        print(k,c,sk,sa,sb,sc)
#1e-10 greska, svi koraci za x=20
exponentialsteps(20,1e-10)
#1e-50 greska, svi koraci za x=50
exponentialsteps(20,1e-50)