import math

print("Hello World")

x = 10
y = 12

print (x)
print (y)

def print_message():
 print ("Hello World")

print_message()

#---------------------------------------------------------------------------------------------------------
def power():
 n1 = input("Enter the base: ")
 n2 = input("Enter the radical: ")
 print(n1**n2)

power()

#----------------------------------------------------------------------------------------------------------
def pwr(a, b):
 print (a**b)

n1 = input("Enter the base: ")
n2 = input("Enter the radical: ")
pwr(n1, n2)

#----------------------------------------------------------------------------------------------------------

def dist(x1, y1, x2, y2):
 a = (x2 - x1)**2
 b = (y2 - y1)**2
 c = a + b
 d = math.sqrt(c)
 print(c)

a  = input("Enter x1: ")
b  = input("Enter y1: ")
c  = input("Enter x2: ")
d  = input("Enter y2: ")

dist(a, b, c, d)

#-------------------------------------------------------------------------------------------------------------
import numpy as np
print "Enter the coordinates of First point"
x1=input()
y1=input()
print "Enter the coordinates of Second point"
x2=input()
y2=input()
x=(x2-x1)**2
y=(y2-y1)**2
distance=np.sqrt(x+y)
print "The distance between points is",distance

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
def dist(x1,y1,x2,y2):
	x=(x2-x1)**2
	y=(y2-y1)**2
	distance=np.sqrt(x+y)
	print "The distance between points is",distance

print "Enter the coordinates of First point"
x1=input()
y1=input()
print "Enter the coordinates of Second point"
x2=input()
y2=input()
dist(x1,y1,x2,y2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def dist(x1,y1,x2,y2):
	x=(x2-x1)**2
	y=(y2-y1)**2
	distance=(x+y)**0.5
        return distance	
print "Enter the coordinates of First point"
x1=input()
y1=input()
print "Enter the coordinates of Second point"
x2=input()
y2=input()
distance=dist(x1,y1,x2,y2)
print "The distance between points is",distance
