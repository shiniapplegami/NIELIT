import numpy as np
import pandas as pd


dt1 = np.dtype({'names':['ename','eno','edesig','esalary','ephno'],'formats':['S20','i8','S20','f8','S20']})

f1 = np.loadtxt('emp.csv', delimiter=',', dtype=dt1, skiprows=1)

print(f1)

def choice(num):
    if num==1:
        f1 = np.loadtxt('emp.csv', delimiter=',', dtype=dt1, skiprows=1)
        print(f1)
    elif num==2:
        f1 = np.loadtxt('emp.csv', delimiter=',', dtype=dt1, skiprows=1)
        name=str(input("Enter an emp_name: "))
        no=int(input("Enter an emp_no: "))
        desig=str(input("Enter an emp_designation: "))
        salary=float(input("Enter an emp_salary: "))
        phone=str(input("Enter an emp_phone: "))

        data=np.array([(name,no,desig,salary,phone)], dtype=dt1)

        g=np.array(f1)
        
        f2=np.concatenate([g,data], axis=0)
        print(f2)
    elif num==3:
        e_no= input("Enter an employee number: ")

        for i in range(g, shape[0]):
            if g["eno"][i]==e_no:
                g = np.delete(g, (i), axis=0)
        print(g)

    elif num==4:
        rec=input("Enter employee name or number: ")

        for i in range(g,shape[0]):
            if g["ename"][i]==rec:
                print(g[i])
            elif g["eno"][i]==rec:
                print(g[i])

    elif num==5:
        totalemp=0
        print("Total employees are ", g.shape[0])
        print("total salary is", g["esalary"].sum())

    elif num==6:
        np.savetxt('f2', g1,  delimiter=',')

    elif num==7:
        global cond
        cond = False
        
cond = True

while cond:
    print('==========================')
    print('CHOOSE A DIGIT ')
    print('1 - Load Data')
    print('2 - Append Data')
    print('3 - Remove Employee Records')
    print('4 - Display Employee Records')
    print('5 - Display Summary')
    print('6 - Save All')
    print('7 - Exit')
    choose = input('Choose a Digit : ')
    choose = int(choose)
    for i in range(8):
        if i == choose:
            action(i)


#action(2)
