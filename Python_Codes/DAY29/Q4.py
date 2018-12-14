import matplotlib.pyplot as plt
import numpy as np

fobj=plt.figure(figsize=(10,10))
spobj=fobj.add_subplot(1,1,1)

month_name_xticks='Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
x_val=np.arange(len(month_name_xticks))


barwidth=0.3
high=[32,32,33,33,32,30,30,30,30,30,31,31]
low=[23,23,24,25,25,24,24,24,24,24,23,23]

spobj.barh(x_val,high,alpha=0.5,height=0.3,color='b',label='high')
spobj.barh(x_val+barwidth,low,alpha=0.5,height=0.3,color='r',label='low')


spobj.set_yticks(x_val+barwidth)
spobj.set_yticklabels(month_name_xticks)
spobj.set_ylabel('Months')
spobj.set_xlabel('Temperatures')
spobj.set_title('whethr chart')
spobj.legend(loc='upper right')
plt.show()
