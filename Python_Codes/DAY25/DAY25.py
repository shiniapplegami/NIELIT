import pandas as pd
import re

#Function to remove Non-Numeric Values
def Rep(n):
	return re.sub('[^0-9\.]','',str(n))

ef1=pd.read_csv("emp.csv",header=None)
ef1.columns="E_name EmpNo E_Desig E_Salary EPhNo".split()
#--------------------------------------------------------------------------------------------------------------------

ef2=ef1.copy()
ef2['EPhNo']=ef2['EPhNo'].apply(Rep)
print ef2,"\n"

#-------------------------------------------------------------------------------------------------------------------

writer=pd.ExcelWriter("empx.xlsx")
et=ef2.drop(['EmpNo','EPhNo'],axis=1)
et.to_excel(writer,sheet_name="salary")

#------------------------------------------------------------------------------------------------------------------

ef2.drop(['EmpNo','E_Desig','E_Salary'],axis=1).to_excel(writer,sheet_name="phone")
writer.save()

#------------------------------------------------------------------------------------------------------------------

ef3=ef2.set_index(['E_Desig','EmpNo'])
print ef3,"\n"

#------------------------------------------------------------------------------------------------------------------

ef4=ef3.sort_index(level='E_Desig')
print ef4,"\n"

#-----------------------------------------------------------------------------------------------------------------

print ef4.loc['scientist',:],"\n"

#-----------------------------------------------------------------------------------------------------------------

print "Average Salary of Engineers : ",ef4.loc['engineer',:]['E_Salary'].mean(),"\n"

#-----------------------------------------------------------------------------------------------------------------

print "Minimum Salary of Scientist : ",ef4.loc['scientist',:]['E_Salary'].min(),"\n"
