import numpy as np
import matplotlib.pyplot as plt

m= 200
l=0.284902028828339
theta_0=np.radians(4)
g=9.81
T=2*np.pi*np.sqrt(l/g)

t_0=0
t_N=20*T


def y_anal(x):
    omega=np.sqrt(g/l)
    A=theta_0
    return A*np.cos(omega*x)
def graph_anal(t_in,t_fin,N,f):
    step=((t_fin-t_in)/N)
    x_list=np.arange(t_in,t_fin,step)
    print(x_list)
    y_list=f(x_list)
    print(y_list)
    plt.plot(x_list,y_list)
    plt.show()

def omega_dot(x):
    return -(g/l)*np.sin(x)
def euler(t_in,t_fin,N,f):
    step=(t_fin-t_in)/N
    t=[0]
    omega=[0]
    theta=[theta_0]
    for i in np.arange(t_in,t_fin,step):
        k_omega=f(theta[-1])
        k_theta=omega[-1]
        t.append(i)
        omega.append(k_omega*step+omega[-1])
        theta.append(k_theta*step+theta[-1])
    return t,theta,omega

#x,y,y_dot=euler(t_0,t_N,1000,omega_dot)
#print(x,y)
#plt.plot(x,y)
#plt.show()

def runge_kutta(t_in,t_fin,N,f):
    step=(t_fin-t_in)/N
    t=[0]
    omega=[0]
    theta=[theta_0]
    for i in np.arange(t_in,t_fin,step):
        #prvi korak (k1)
        t.append(i)
        k_omega=f(theta[-1])
        sw=k_omega
        k_theta=omega[-1]
        sk=k_theta
        #drugi korak(k2)
        omega_p=omega[-1]+k_omega*(step/2)
        theta_p=theta[-1]+k_theta*(step/2)
       
        k_omega=f(theta_p)
        sw+=2*k_omega
        k_theta=omega_p
        sk+=2*k_theta
        #treći korak(k3)
        omega_p=omega[-1]+k_omega*(step/2)
        theta_p=theta[-1]+k_theta*(step/2)
        k_omega=f(theta_p)
        sw+=2*k_omega
        k_theta=omega_p
        sk+=2*k_theta
        #zadnji korak
        omega_p=omega[-1]+k_omega*(step)
        theta_p=theta[-1]+k_theta*(step)
        k_omega=f(theta_p)
        sw+=k_omega
        k_theta=omega_p
        sk+=k_theta
        #konacno
        omega.append(omega[-1]+(sw/6)*step)
        theta.append(theta[-1]+(sk/6)*step)

    return t,theta,omega

x,y,y_dot=runge_kutta(t_0,t_N,10000,omega_dot)
print(x,y)
plt.plot(x,y)
plt.show()
