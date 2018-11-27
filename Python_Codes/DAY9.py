class vector:
    def __init__(self,px,py):
        self.x = px
        self.y = py
    def display(self):
        print "vector : (%.3f,%.3f)"%(self.x,self.y)
    def __add__(self,v2):
        return vector(self.x+v2.x, self.y+v2.y )
        
s1= vector(3,2)
s2 = vector(2,3)
s3 = s1+s2
s1.display()
s2.display()
s3.display()
#-----------------------------------------------------------------------------

class mycomplex:
    def __init__(self,pa,pb):
        self.a = pa
        self.b = pb
    def display(self):
        print "complex : (%.3f+%.3fi)"%(self.a,self.b)
    def __add__(self,v2):
        return mycomplex(self.a+v2.a, self.b+v2.b )
    
s1= mycomplex(32,21)
s2 = mycomplex(21,32)
s3 = s1+s2
s1.display()
s2.display()
s3.display()
#-----------------------------------------------------------------------------

class mycomplex:
    def __init__(self,pa,pb):
        self.a = pa
        self.b = pb
    def display(self):
        print "complex : (%.3f+%.3fi)"%(self.a,self.b)
    def __add__(self,v2):
        return mycomplex(self.a+v2.a, self.b+v2.b )
    def __mul__(self,v2):
        return mycomplex((self.a*v2.a)+(-1*self.b*v2.b), (self.b*v2.a)+(self.a*v2.b) )
    
s1= mycomplex(3,2)
s2 = mycomplex(1,7)
s3 = s1*s2
s1.display()
s2.display()
s3.display()

#------------------------------------------------------------------------------

import abc

class vehicle:
    __metaclass__ = abc.ABCMeta
    no = 100
    def __init__(self):
        vehicle.no += 1
        self.vowner = raw_input("owner?")
        self.vno = vehicle.no
        self.vym = input("yearofmake?")
        self.vbp = input("buyingprice in tousands?") * 1000
        self.vpv = self.vbp
        
#    @abc.abstractmethod
    def cal_pv(self):
        pass
    
    def display(self):
        print " --- info ---\nType: %s, Vno : %s, owner : %s,\nNoofwheels : %s, yearofmake : %d, \nprice : %d, presentVal : %d "%(self.type,self.vno,self.vowner,self.vwheels,self.vym,self.vbp,self.vpv)

class car(vehicle):
    def __init__(self):
        self.type = "car"
        self.vwheels = 4
        vehicle.__init__(self)
    def cal_pv(self):
        self.vpv = self.vbp - (2018 - self.vym) * 5000
        
class bus(vehicle):
    def __init__(self):
        self.type = "bus"
        self.vwheels = 6
        vehicle.__init__(self)
    def cal_pv(self):
        self.vpv = self.vbp - (2018 - self.vym) * 1000
        
class truck(vehicle):
    def __init__(self):
        self.type = "truck"
        self.vwheels = 10
        vehicle.__init__(self)
    def cal_pv(self):
        self.vpv = self.vbp - (2018 - self.vym) * 12000
        
        
v1 = truck()
v1.cal_pv()
v1.display()
