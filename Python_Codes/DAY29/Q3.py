import matplotlib.pyplot as plt
import numpy as np

fobj=plt.figure(figsize=(10,10),facecolor='#F08080')
spobj=fobj.add_subplot(1,1,1)

month_name_xticks='Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
x_val=np.arange(len(month_name_xticks))
#x_val=np.linspace(0,200,len(stud_name_xticks))
barwidth=0.3
high=[32,32,33,33,32,30,30,30,30,30,31,31]
low=[23,23,24,25,25,24,24,24,24,24,23,23]
spobj.bar(x_val,high,width=barwidth,alpha=0.5,color='b',label='high')
spobj.bar(x_val+barwidth,low,width=barwidth,alpha=0.5,color='r',label='low')
#plt.xticks(x_val,stud_name_xticks)
spobj.set_xticks(x_val+barwidth)
spobj.set_xticklabels(month_name_xticks)
spobj.set_xlabel('months')
spobj.set_title('Assessment chart')
spobj.legend(loc='center')
plt.show()
