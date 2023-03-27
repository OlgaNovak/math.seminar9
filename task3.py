# Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге
# одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

import math
import numpy as np
import scipy.stats as stats


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
x=zp
y=ks

# расчет с использованием intercept
B=(np.mean(zp*ks)-np.mean(zp)*np.mean(ks))/((np.mean(zp**2))-np.mean(zp)**2)
print(B)
A=np.mean(ks)-B*np.mean(zp)
print(A)

def mse_(A,B,y=y,x=x,n=10):
    return np.sum(((A+B*x)-y)**2)/n

alpha=1*math.exp(-6)
print(alpha)
for i in range(80):
    A-=alpha*2*np.sum((A+B*x)-y)/len(x)          # alpha  на производную функции mse_ по A
    B-=alpha*2*np.sum(((A+B*x)-y)*x)/len(x)      # alpha  на производную функции mse_ по B
    if i%1==0:
        print('Iteration={i},A={A},B={B}, mse={mse}'.format(i=i,A=A,B=B,mse=mse_(B)))
