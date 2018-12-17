#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anm

fo=plt.figure(figsize=(6,6))
so=fo.add_subplot(111)
so.set_ylim([0,51])
x=np.arange(4)

xlabels='SONY MI LG Asus'.split()
sa=np.array([0,0,0,0])

bc1=so.bar(x,sa,align='center')

so.set_xticks(x)
so.set_xticklabels(xlabels)

def animbar(i):
 global bc1
 sa=np.random.randint(1,50,4)
 print sa
 for bar1,h1 in zip(bc1,sa):
  bar1.set_height(h1)
 return bc1
anm1=anm.FuncAnimation(fo,animbar,interval=3000)
plt.show()
