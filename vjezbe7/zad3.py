import numpy as np
import matplotlib.pyplot as plt

m= 200
l=0.284902028828339
theta_0=np.radians(4)
g=9.81
T=2*np.pi*np.sqrt(l/g)

t_0=0
t_N=20*T


def y_anal(x,theta0=theta_0):
    omega=np.sqrt(g/l)
    A=theta0
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

for i in [100,200,500,1000,5000,10000]:
    t,theta,omega=euler(t_0,t_N,i,theta_0,omega_dot)
    brojkorakautitraju=i//20
    t_1=np.array(t[1:brojkorakautitraju+2])
    theta_1=np.array(theta[1:brojkorakautitraju+2])
    theta_anal1=y_anal(t_1)
    error1=theta_anal1-theta_1
    plt.plot(t_1,error1,label="N={}".format(i))
plt.legend()
plt.title("Greška između Eulerove metode i analitičke metode za N koraka (1. Titraj)")
plt.xlabel("t")
plt.ylabel("error")
plt.show()
for i in [100,200,500,1000,5000,10000]:
    t,theta,omega=euler(t_0,t_N,i,theta_0,omega_dot)
    brojkorakautitraju=i//20
    t_2=np.array(t[1+19*brojkorakautitraju:20*brojkorakautitraju+2])
    theta_2=np.array(theta[1+19*brojkorakautitraju:20*brojkorakautitraju+2])
    theta_anal2=y_anal(t_2)
    error2=theta_anal2-theta_2
    plt.plot(t_2,error2,label="N={}".format(i))
plt.legend()
plt.title("Greška između Eulerove metode i analitičke metode za N koraka (20. Titraj)")
plt.xlabel("t")
plt.ylabel("error")
plt.show()


for i in [10000,2000]:
    t,theta,omega=euler(t_0,t_N,i,theta_0,omega_dot)
    brojkorakautitraju=i//20
    t_1=np.array(t[1+19*brojkorakautitraju:20*brojkorakautitraju+2])
    print(t_1)
    theta_1=np.array(theta[1+19*brojkorakautitraju:20*brojkorakautitraju+2])
    print(theta_1)
    #plt.plot(t,theta)
    #Runge Kutta
    t,theta,omega=runge_kutta(t_0,t_N,i,theta_0,omega_dot)
    theta_2=np.array(theta[1+19*brojkorakautitraju:20*brojkorakautitraju+2])
    plt.plot(t_1,theta_1,label="Euler, N={}".format(i))
    
    plt.plot(t_1,theta_2,label="Runge Kutta, N={}".format(i))
plt.legend()
plt.title("Usporedba Eulerove i Runge Kutta metode za titranje matematičkog njihala")
plt.xlabel("t")
plt.ylabel("theta")
plt.show()

for i in [4,8,16,32,64]:
    t,theta,omega=runge_kutta(t_0,t_N,10000,np.radians(i),omega_dot)
    brojkorakautitraju=10000//20
    t_1=np.array(t[1:7*brojkorakautitraju+2])
    theta_anal=y_anal(t_1,theta0=np.radians(i))
    theta_1=theta[1:7*brojkorakautitraju+2]
    plt.plot(t_1,theta_anal,label="analitička, theta_0={}°".format(i))
    plt.plot(t_1,theta_1,label="Runge_Kutta, theta_0={}°".format(i))
plt.legend()
plt.title("Usporedba Runge Kutta i analitičke metode za različite kutove")
plt.xlabel("t")
plt.ylabel("theta")
plt.show()