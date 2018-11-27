class baseEmp:
    no = 100
    
    def __init__(self,bpay):
        baseEmp.no += 1
        self.empno = baseEmp.no
        self.name = raw_input("Name?")
        self.basicpay = bpay
        
class scientist(baseEmp):
    
    def __init__(self):
        baseEmp.__init__(self,50000)
        self.tech_allowance = raw_input("tech allowance?")
        self.category = "Scientist"
    
    def disp(self):
        print "------\nName : %s\nEmpNo : %s\nBasicpay : %s rs\nTechAllow : %s\nCategory : %s"%(self.name,self.empno,self.basicpay,self.tech_allowance,self.category)
        
class officer(baseEmp):
    
    def __init__(self):
        baseEmp.__init__(self,30000)
        self.grade = raw_input("grade?")
        self.department = raw_input("department?")
        
    def disp(self):
        print "------\nName : %s\nEmpNo : %s\nBasicpay : %s rs\nGrade : %s\nDepartment : %s"%(self.name,self.empno,self.basicpay,self.grade,self.department)    
        
        

s1=scientist()
s2=officer()
s1.disp()
s2.disp()

#--------------------------------------------------------------------------------


class scientist(baseEmp):
    
    def __init__(self):
        baseEmp.__init__(self,50000)
        self.tech_allowance = raw_input("tech allowance?")
        self.category = "Scientist"
    
    def disp(self):
        print "------\nName : %s\nEmpNo : %s\nBasicpay : %s rs\nTechAllow : %s\nCategory : %s"%(self.name,self.empno,self.basicpay,self.tech_allowance,self.category)
    
    def __str__(self):
        
        return "Scientis %s with id %s has a salary of %s\n"%(self.name,self.empno,self.basicpay)
        
class officer(baseEmp):
    
    def __init__(self):
        baseEmp.__init__(self,30000)
        self.grade = raw_input("grade?")
        self.department = raw_input("department?")
        
    def disp(self):
        print "------\nName : %s\nEmpNo : %s\nBasicpay : %s rs\nGrade : %s\nDepartment : %s"%(self.name,self.empno,self.basicpay,self.grade,self.department)    
        
    def __str__(self):
        
        return "Officer %s with id %s has a salary of %s\n"%(self.name,self.empno,self.basicpay)       
        

s1=scientist()
s2=officer()
str(s1)
str(s2)
