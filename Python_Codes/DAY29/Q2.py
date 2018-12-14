#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

fobj = plt.figure(figsize=(10,10),facecolor='#FA8072')
spobj=fobj.add_subplot(3,3,1)

Parties='INC BJP Independent Others'.split()
votes=[114,15,4,3]
colrs='r y c g'.split()

#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)

patches,texts=spobj.pie(votes,colors=colrs,shadow=True,startangle=45)

print patches
print texts

plt.title("Madhya Pradesh")
plt.legend(patches,Parties,loc=2)

#--------------------------------------------------------------------------------------------------------------------------------

spobj=fobj.add_subplot(3,3,2)

Parties='INC BJP Independent Others'.split()
votes=[99,73,3,14]
colrs='r y c g'.split()

#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)

patches,texts=spobj.pie(votes,colors=colrs,shadow=True,startangle=45)

print patches
print texts

plt.title("Rajasthan")
plt.legend(patches,Parties,loc=2)


#--------------------------------------------------------------------------------------------------------------------------------

spobj=fobj.add_subplot(3,3,3)

Parties1='INC BJP BSP+ Others'.split()
votes=[68,15,9,7]
colrs='r y c g'.split()

#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)

patches,texts=spobj.pie(votes,colors=colrs,shadow=True,startangle=45)

print patches
print texts

plt.title("Chattisgarh")
plt.legend(patches,Parties1,loc=2)

#----------------------------------------------------------------------------------------------------------------------------------

spobj=fobj.add_subplot(3,3,4)

Parties2='TRS INC BJP Others'.split()
votes=[88,19,1,11]
colrs='r y c g'.split()

#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)

patches,texts=spobj.pie(votes,colors=colrs,shadow=True,startangle=45)

print patches
print texts

plt.title("Telangana")
plt.legend(patches,Parties2,loc=2)

#----------------------------------------------------------------------------------------------------------------------------------

spobj=fobj.add_subplot(3,3,5)

Parties3='MNF INC BJP Others'.split()
votes=[26,5,1,8]
colrs='r y c g'.split()

#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)

patches,texts=spobj.pie(votes,colors=colrs,shadow=True,startangle=45)

print patches
print texts

plt.title("Mizoram")
plt.legend(patches,Parties3,loc=2)
plt.show()




