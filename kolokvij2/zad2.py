import numpy as np
import matplotlib.pyplot as plt
m=2
def F(x,v):
    return 2*x-5*v+0.5
def runge_kutta(t_in,t_fin,N,x0,f):
    step=(t_fin-t_in)/N
    t=[0]
    v=[0]
    x=[x0]
    F=[f(x0,0)]
    for i in np.arange(t_in,t_fin+step,step):
        #prvi korak (k1)
        t.append(i)
        k_v=f(x[-1],v[-1])/m
        sw=k_v
        k_x=v[-1]
        sk=k_x
        #drugi korak(k2)
        v_p=v[-1]+k_v*(step/2)
        x_p=x[-1]+k_x*(step/2)
       
        k_v=f(x_p,v_p)/m
        sw+=2*k_v
        k_x=v_p
        sk+=2*k_x
        #treći korak(k3)
        v_p=v[-1]+k_v*(step/2)
        x_p=x[-1]+k_x*(step/2)
        k_v=f(x_p,v_p)/m
        sw+=2*k_v
        k_x=v_p
        sk+=2*k_x
        #zadnji korak
        v_p=v[-1]+k_v*(step)
        x_p=x[-1]+k_x*(step)
        k_v=f(x_p,v_p)/m
        sw+=k_v
        k_x=v_p
        sk+=k_x
        #konacno
        v.append(v[-1]+(sw/6)*step)
        x.append(x[-1]+(sk/6)*step)
        F.append(f(x[-1],v[-1]))

    return t,x,v,F
t,x,v,F=runge_kutta(0,5,5000,0,F)
plt.plot(t,x,label='x(t)')
plt.plot(t,v,label='v(t)') 
plt.plot(t,F,label='F(t)')
plt.legend()
plt.xlabel("t(s)")
plt.show()
print (x[-1],v[-1])