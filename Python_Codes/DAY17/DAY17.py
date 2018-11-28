import numpy as np

l1=[1,2,3,4,5]

a=np.array(l1)

print(a)

#--------------------------------------------------------------------------------------

c=np.arange(6)

print(c)

#--------------------------------------------------------------------------------------

q=np.ones((2,4,5))
print(q.size)

#--------------------------------------------------------------------------------------

l1=[1,2,3]
l2=[6,7,8]

a1=np.asarray([l1,l2])

a2=np.array([l1,l2])

#---------------------------------------------------------------------------------------
t=np.eye(40)

print(t)
#----------------------------------------------------------------------------------------
z=np.zeros((2,5,4))

print(z.size)

#---------------------------------------------------------------------------------------

print(a.size)
print(c.size)
print(q.size)
print(t.size)
print(z.size)
print(a2.size)

print(a.ndim)
print(c.ndim)
print(q.ndim)
print(t.ndim)
print(z.ndim)
print(a2.ndim)

print(type(a))
print(type(c))
print(type(q))
print(type(t))
print(type(z))
print(type(a2))

print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)
print(a2.shape)
print(e.shape)
