# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

import math
import numpy as np
import scipy.stats as stats


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
x=zp
y=ks

# расчет без использования intercept
n=10
B1=(n*np.sum(ks*zp)-np.sum(zp)*np.sum(ks))/(n*np.sum(zp**2)-np.sum(zp)**2)
print(B1)

def mse_(B1,y=y,x=x,n=10):
    return np.sum((B1*x-y)**2)/n

alpha=1*math.e**(-6)
print(alpha)
for i in range(80):
    B1-=alpha*(2/n)*np.sum((B1*x-y)*x)
    if i%5==0:
        print('Iteration={i},B1={B1}, mse={mse}'.format(i=i,B1=B1,mse=mse_(B1)))
