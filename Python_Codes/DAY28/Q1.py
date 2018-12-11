import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7))
sub =fig.add_subplot(1,1,1)

y = np.random.randint(1,100,10)
print('y = {0}'.format(y))
y.sort()
y1 = y[y<50]

y2 =y[y>50]

print('y1 = {0}'.format(y1))
#print('y2 = {0}'.format(y2))

y2 = np.insert(y2,0,y1[-1])
print('y2 = {0}'.format(y2))

x = np.arange(2,21,2)
print('x = {0}'.format(x))

sub.plot(x[:y1.size],y1,linestyle='solid',marker='o',color='b',markerfacecolor='r')
sub.plot(x[y1.size-1:],y2,linestyle='solid',marker='o',color='y',markerfacecolor='r')


plt.show()
