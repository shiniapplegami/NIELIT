import numpy as np
import pandas as pd
import xml.dom.minidom as dm
X=pd.read_csv("new.csv")
X=X.as_matrix()
doc=dm.Document()

e1=doc.createElement("Employees")


for i in range(3):
		es=doc.createElement('Employee')
		e11=doc.createElement('Eno')
		
		e12=doc.createTextNode(str(X[i,0]))
		e11.appendChild(e12)
		e2=doc.createElement('Ename')
		
                e21=doc.createTextNode(str(X[i,1]))
 		e2.appendChild(e21)
		e3=doc.createElement('Edesig')
		
                e31=doc.createTextNode(str(X[i,2]))
		e3.appendChild(e31)
		e4=doc.createElement('Esalary')
		
                e41=doc.createTextNode(str(X[i,3]))

                
		e4.appendChild(e41)
		es.appendChild(e2)
		es.appendChild(e3)
		es.appendChild(e4)
		es.appendChild(e11)
		e1.appendChild(es)



fd=open("new1.xml","w")



e1.writexml(fd,indent="\t",addindent="\t",newl="\n")
fd.close()
'''
#---------------------------------------------------------------------------------------------


import MySQLdb as db
class MysqlDb:
    def __init__(self):
        self.con = db.connect("127.0.0.1",'ai','ai','ai')
        self.cur = self.con.cursor()
       
    def createTable(self):
        try :
            tableName = input("enter table name:")
            query = "create table "  + tableName + "(eno int, ename varchar(20), edesig char(20),esalary int,primary key (eno))"
            self.cur.execute(query)
            self.con.close()
        except Exception,arg:
            print arg

    def insertData(self):
        try :
            tableName = input("enter table name to store data:")
            id2 = input("employee number:")
            name = input("enter name:")
            designation = input("enter designation:")
            salary = input("enter salary:")
            query ="insert into " + tableName + " values(" + str(id2) +",'" + name + "','" + designation + "'," + str(salary) + ")"
          
            self.cur.execute(query)
            self.con.commit()
            self.con.close()
            print "inserted 1 row:"
        except Exception,arg:
            print arg

       
s1 = MysqlDb()
#s1.createTable()
s1.insertData()

'''
