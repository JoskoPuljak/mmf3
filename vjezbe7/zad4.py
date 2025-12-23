import numpy as np
import matplotlib.pyplot as plt

m= 200
l=0.284902028828339
theta_0=np.radians(4)
g=9.81
T=2*np.pi*np.sqrt(l/g)

t_0=0
t_N=20*T

def omega_dot(x):
    return -(g/l)*np.sin(x)
def JUG(t_in,t_fin,N,theta0,f):
    step=(t_fin-t_in)/N
    t=[0]
    omega=[0]
    theta=[theta0]
    for i in np.arange(t_in,t_fin+step,step):
        a=f(theta[-1])
        t.append(t[-1]+step)
        theta.append(theta[-1]+omega[-1]*step+0.5*a*step**2)
        omega.append(omega[-1]+a*step)
    return t,theta,omega
def euler(t_in,t_fin,N,theta0,f):
    step=(t_fin-t_in)/N
    t=[0]
    omega=[0]
    theta=[theta0]
    for i in np.arange(t_in,t_fin+step,step):
        k_omega=f(theta[-1])
        k_theta=omega[-1]
        t.append(i)
        omega.append(k_omega*step+omega[-1])
        theta.append(k_theta*step+theta[-1])
    return t,theta,omega



def runge_kutta(t_in,t_fin,N,theta0,f):
    step=(t_fin-t_in)/N
    t=[0]
    omega=[0]
    theta=[theta0]
    for i in np.arange(t_in,t_fin+step,step):
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
def y_anal(x,theta0=theta_0):
    omega=np.sqrt(g/l)
    A=theta0
    return A*np.cos(omega*x)

t,theta,omega=euler(t_0,t_N,20000,theta_0,omega_dot)
brojkorakautitraju=20000//20
omega_1=np.array(omega[1+17*brojkorakautitraju:20*brojkorakautitraju+2])
theta_1=np.array(theta[1+17*brojkorakautitraju:20*brojkorakautitraju+2])
plt.plot(theta_1,omega_1,label="Eulerova metoda")
t,theta,omega=runge_kutta(t_0,t_N,20000,theta_0,omega_dot)
omega_2=np.array(omega[1+17*brojkorakautitraju:20*brojkorakautitraju+2])
theta_2=np.array(theta[1+17*brojkorakautitraju:20*brojkorakautitraju+2])
plt.plot(theta_2,omega_2,label="Runge Kutta metoda")
t,theta,omega=JUG(t_0,t_N,20000,theta_0,omega_dot)
omega_3=np.array(omega[1+17*brojkorakautitraju:20*brojkorakautitraju+2])
theta_3=np.array(theta[1+17*brojkorakautitraju:20*brojkorakautitraju+2])
plt.plot(theta_3,omega_3,label="Metoda jednostavnog ubrzanog gibanja")
plt.xlabel("theta")
plt.ylabel("omega")
plt.legend()
plt.show()
