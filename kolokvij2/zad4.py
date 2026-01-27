import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 2*x
def prediktor_korektor(x_in,x_fin,N,V0,f):
    step=(x_fin-x_in)/N
    x=[0]

    V=[V0]
    for i in np.arange(x_in,x_fin+step,step):
        #prediktor
        k_V=f(x[-1])
        V_p=k_V*step+V[-1]
        sV=k_V
        #korektor
        k_V=f(x[-1]+step)
        sV+=k_V

        V.append(0.5*(sV)*step+V[-1])
        x.append(i)
    return x,V

x,V=prediktor_korektor(1,9,10,0,f)
plt.scatter(x,V)
x2,V2=prediktor_korektor(1,9,1000,0,f)
plt.scatter(x2,V2,color="red")
plt.xlabel("x")
plt.ylabel("V(x)")
plt.show()