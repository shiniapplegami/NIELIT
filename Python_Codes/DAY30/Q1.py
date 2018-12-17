import scipy.optimize as spo
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

x=np.array([2,3,5,7,9])
y=np.array([4,5,7,10,15])

fxf=lambda m,x,c: m*x+c

popt,pcov= spo.curve_fit(fxf, x, y)

print(popt)

fxf(popt[0], 10 , popt[1])

vfxf= sp.vectorize(fxf)

cy = vfxf(popt[0],x,popt[1])

plt.plot(x,y,'r:o', label='observed')
plt.plot(x,cy,'b-v',label='calculated')
plt.legend(loc='best')
plt.show()
