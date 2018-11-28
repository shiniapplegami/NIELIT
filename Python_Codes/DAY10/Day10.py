
import abc

class Employee(object):
    __metaclass__=abc.ABCMeta
    def __init__(self, name, no, basicpay):
        self.name= name
        self.no= no
        self.basicpay=basicpay
        self.salary=0
        self.da=0
        self.hra=0
        self.spa=0

    def display(self):
        print "%s with id number %d has a salary of %f"%(self.name, self.no, self.salary)
        
    

    @abc.abstractmethod
    def getda(self): pass

    @abc.abstractmethod
    def getspa(self):pass

    @abc.abstractmethod
    def gethra(self): pass
    
    
    def calcsalary(self):
        self.salary=self.basicpay+self.da+self.hra+self.spa

class Engineer(Employee):
    def getda(self):
        self.da=0.3*self.basicpay

    def gethra(self):
        self.hra=0.1*self.basicpay
    def getspa(self):
        self.spa=0.2*self.basicpay

class Officer(Employee):
    def getda(self):
        self.da=0.3*self.basicpay

    def gethra(self):
        self.hra=0.1*self.basicpay
    def getspa(self):
        self.spa=0.1*self.basicpay

class jeng(Engineer):
    def gethra(self):
        self.hra=500+self.hra

class seng(Engineer):
    def gethra(self):
        self.hra=1000+self.hra



s1=jeng("Amitabh Bacchan", 07, 15000)
s1.getda()
s1.gethra()
s1.getspa()
s1.calcsalary()
s1.display()




#---------------------------------------------------------------------------

class vector:
    def __init__(self,px,py):
        self.x = px
        self.y = py
        
    def display(self):
        print "vector : (%.3f,%.3f)"%(self.x,self.y)
        
    def __add__(self,v2):
        return vector(self.x+v2.x, self.y+v2.y )
    
    def __eq__(self,v2):
        return (self.x == v2.x and self.y == v2.y)
 
v1 = vector(2,1)
v2 = vector(2,2)
print v1 == v2

#------------------------------------------------------------------------------

class Father(object): 
    def weight(self):
        print("Weight is 89 kg")
  
class Mother(object): 
    def height(self): 
        print ("Height is 5 foot 6 inches")
  
class Child(Father, Mother):
    pass

c=child()
print("Child\'s inherited qualities:")
c.weight()
c.height()


#-------------------------------------------------------------------------------

class vehicle:
    no=1001
    def __init__(self):
        vehicle.no += 2
        self.owner = raw_input("Owner?")
        self.wheels = 0
        self.vno = vehicle.no
        
class truck(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        self.cat = "Truck"
        self.wheels = 12

class carrier(car):
    def __init__(self):
        truck.__init__(self)
        self.subc = "carrier"
    
    def display(self):
        print "--info--\n Owner:%s\n Vehicle no:%d\n No wheels:%d\n Type:%s\n Category:%s"%(self.owner,self.vno,self.wheels,self.cat,self.subc)
        
lamb = carrier() 
lamb.display()

#------------------------------------------------------------------------------

from mod import*

try:
    if e==0:
        raise IOERROR
    else:
        def mod(k):
            if k == 1:
                import mod

            elif k == 2:
                con = a + 10 * b * c - 5 * d / e
                print con
            elif k == 3:
                reload(mod)
                con = a + 10 * b * c - 5 * d / e
                print con
            elif k == 0:
                next
            else:
                print 'ERROR-INVALID INPUT'
    
except Exception:
    print "e cannot be zero"

#-----------------------------------------------------------------------------


def subclass(cname,count=0):
    print '-'*count,cname.__name__
    for subc in cname.__subclasses__():
        subclass(subc,count+1)
        
subclass_info(Exception)






