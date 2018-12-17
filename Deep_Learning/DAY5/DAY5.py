import tensorflow as tf

def session(X):
    sess= tf.Session()
    r = sess.run(X)
    '''writer=tf.summary.FileWriter("./MyFile",sess.graph)
    writer.close()'''
    print(r)

#--------------------------------------------------------------------------------------------------------
    
x=tf.zeros([2,3],tf.int32)
session(x)

#---------------------------------------------------------------------------------------------------------

X= tf.constant([[1,2,3],[4,5,6]],tf.int32)
session(X)

#---------------------------------------------------------------------------------------------------------

X1=tf.zeros([3,3],tf.int32)
session(X1)

#---------------------------------------------------------------------------------------------------------

y=tf.ones([2,3])
session(y)

#---------------------------------------------------------------------------------------------------------

A= tf.constant([[1,2,3],[4,5,6]],tf.int32)
session(A)

A1=tf.ones([3,3],tf.int32)
session(A1)

#----------------------------------------------------------------------------------------------------------

B=tf.ones([2,3],tf.int32)
B5=B*5
session(B)
session(B5)

#-----------------------------------------------------------------------------------------------------------

C=tf.constant([[1,3,5],[4,6,8]],tf.float32)
session(C)

#-----------------------------------------------------------------------------------------------------------

D=tf.constant([[4,4,4],[4,4,4]])
session(D)

#-----------------------------------------------------------------------------------------------------------

E= tf.linspace(5.0,10.0,50)
session(E)

#-----------------------------------------------------------------------------------------------------------

F=tf.random_normal([2,3], mean=0, stddev=2)
session(F)

#-----------------------------------------------------------------------------------------------------------

G= tf.random_uniform([3,2], minval=0, maxval=2)
session(G)

#-----------------------------------------------------------------------------------------------------------

X= tf.constant([[1, 2], [3, 4], [5, 6]])

X1=tf.random_shuffle(X)
session(X1)

#-----------------------------------------------------------------------------------------------------------

H= tf.random_normal([10,10,3])

H1=tf.random_crop(H,[5,5,3])
session(H1)

#-----------------------------------------------------------------------------------------------------------

I=tf.constant([[-1, -2, -3], [0, 1, 2]],tf.int32)
I1=tf.zeros([2,3],tf.int32)

I2=tf.not_equal(I,I1)
session(I2)

#----------------------------------------------------------------------------------------------------------

J= tf.constant([[1,2,3],[4,5,6]],tf.int32)

K= tf.constant([[1,3,5],[4,6,8]],tf.int32)

L= tf.constant([[4,4,4],[4,4,4]])

add=tf.add(J,K)
session(add)

sub=tf.subtract(K,J)
session(sub)

multiply= tf.multiply(J,K)
session(multiply)

mul=tf.multiply(J,5)
session(mul)

add1=tf.add(add,L)
session(add1)

#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------

w=tf.Variable(1.0, name="weight")
init= tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)
print(sess.run(w))
sess.close()

#-------------------------------------------------------------------------------------------------------------

x=tf.Variable(5,name="x")
y=tf.Variable(15,name="y")
z=tf.Variable(25,name="z")

add=tf.Variable(x+y+z,name='add')
init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)

print(sess.run(add))

#-------------------------------------------------------------------------------------------------------------

p=tf.placeholder(tf.float32)

sess=  tf.Session() 
sess.run(tf.global_variables_initializer())
print(sess.run(p, feed_dict={p:5.0}))
sess.close()

#-------------------------------------------------------------------------------------------------------------

p1=tf.placeholder(tf.float32)
p2=tf.placeholder(tf.float32)
p3=tf.placeholder(tf.float32)

sess=  tf.Session() 
sess.run(tf.global_variables_initializer())
psum=tf.add_n([p1,p2,p3])
print(sess.run(psum,feed_dict={p1:10,p2:20,p3:30}))

#-------------------------------------------------------------------------------------------------------
