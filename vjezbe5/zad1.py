import matplotlib.pyplot as plt
import numpy as np
import lagrange as lg
x_list=[1,2,3,4,5]
y_list=[-5,-12,-15,-8,15]
legend=[]
for i in range(5):
    P_list= [lg.linterpol(x_list,y_list,x)[i] for x in np.linspace(0,5,100)]
    plt.plot(np.linspace(0,5,100),P_list,label='Lagrange Interpolation')
    legend.append(f'L{i}(x)')
P_list= [lg.linterpol(x_list,y_list,x)[len(x_list)] for x in np.linspace(0,5,100)]
legend.append('P(x)')
plt.plot(np.linspace(0,5,100),P_list,label='Lagrange Interpolation')
plt.scatter(x_list,y_list,label='Data Points',color='blue')
plt.legend(legend + ['Data Points'])
plt.savefig('lagrange_interpolation.png')
plt.show()