import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

dset = np.array([2,4,10,12,3,20,30,11,25])

dset = sp.cast['f'](dset)

from scipy.cluster.vq import vq
from scipy.cluster.vq import kmeans

centr1,dist1 = kmeans(dset,2)

clust1,distan1 = vq(dset,centr1)

cx =np.arange(1,dset.size+1)
c1 = dset[clust1==0]
c2 = dset[clust1==1]

plt.scatter(cx[clust1==0],c1,color='g',label='clusterNumber1')
plt.scatter(cx[clust1==1],c2,color='r',label='clusterNumber2')
plt.legend(loc='best')
plt.show()

