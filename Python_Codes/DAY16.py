'''
from Tkinter import *
mwin=Tk()
mwin.geometry('200x200')
vexp=''
def b1han():
 global vexp
 vexp+='1'
 t1.set(vexp)
def b2han():
 global vexp
 vexp+='2'
 t1.set(vexp)
def b3han():
 global vexp
 vexp+='3'
 t1.set(vexp)
def b4han():
 global vexp
 vexp+='4'
 t1.set(vexp)
def b5han():
 global vexp
 vexp+='5'
 t1.set(vexp)
def b6han():
 global vexp
 vexp+='6'
 t1.set(vexp)
def b7han():
 global vexp
 vexp+='7'
 t1.set(vexp)
def b8han():
 global vexp
 vexp+='8'
 t1.set(vexp)
def b9han():
 global vexp
 vexp+='9'
 t1.set(vexp)
def b0han():
 global vexp
 vexp+='0'
 t1.set(vexp)

def bphan():
 global vexp
 vexp+='+'
 t1.set(vexp)
def bmhan():
 global vexp
 vexp+='-'
 t1.set(vexp)
def bchan():
 global vexp
 vexp+='*'
 t1.set(vexp)
def bdhan():
 global vexp
 vexp+='/'
 t1.set(vexp)
def behan():
 global vexp
 t1.set(str(eval(vexp)))
 vexp=''
def bcehan():
 global vexp
 t1.set(str(""))
 vexp=''

 
mwin.title('calculator')
t1=StringVar()
e1=Entry(mwin,textvariable=t1)
b1=Button(mwin,text='1',command=b1han)
b2=Button(mwin,text='2',command=b2han)
b3=Button(mwin,text='3',command=b3han)
b4=Button(mwin,text='4',command=b4han)
b5=Button(mwin,text='5',command=b5han)
b6=Button(mwin,text='6',command=b6han)
b7=Button(mwin,text='7',command=b7han)
b8=Button(mwin,text='8',command=b8han)
b9=Button(mwin,text='9',command=b9han)
b0=Button(mwin,text='0',command=b0han)
bp=Button(mwin,text='+',command=bphan)
bm=Button(mwin,text='-',command=bmhan)
bc=Button(mwin,text='X',command=bchan)
bd=Button(mwin,text='/',command=bdhan)
bce=Button(mwin, text = "AC", command=bcehan)

be=Button(mwin,text='=',command=behan)
e1.grid(row=0,column=0,columnspan=4)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b0.grid(row=4,column=1)

bp.grid(row=1,column=3)
bm.grid(row=1,column=4)
bc.grid(row=2,column=3)
bd.grid(row=2,column=4)
be.grid(row=3,column=3,columnspan=4)
bce.grid(row=4,column=1, columnspan=4)


mwin.mainloop()
'''

#-------------------------------------------#


from Tkinter import *
import MySQLdb as db

class Record:
    def SaveRecord(self):
        name = self.name1.get()
        designation = self.desig.get()
        salary1= self.salary.get()
        con = db.connect("127.0.0.1",'ai','ai','ai')
        cur = con.cursor()
        query ="insert into ai7_emp (name,designation,salary)"  + " values('" + name +"','" + designation + "'," + str(salary1) + ")"
        print query
        cur.execute(query)
        con.commit()
        con.close()
        print "inserted 1 row:"
        self.name1.set('')
        self.salary.set('')
        self.desig.set('')
        self.getData()

    def getData(self):
        con = db.connect("127.0.0.1",'ai','ai','ai')
        cur = con.cursor()
        query ="Select * from ai7_emp"
        cur.execute(query)
        result = cur.fetchall()
        i = 11
        totalSalary = 0
        for res in result: #Rows
            i = i +1
            name1 = StringVar()
            name2 = StringVar()
            name3 = StringVar()
            name1.set(res[1])
            name2.set(res[2])
            name3.set(res[3])
            totalSalary += res[3]
            Entry(self.mainWindow,font = ("Times",12,'bold'), textvariable = name1).grid(row=i+1,column=0,columnspan=4)
            Entry(self.mainWindow, textvariable = name2).grid(row=i+1,column=3,columnspan=4)
            Entry(self.mainWindow, textvariable = name3).grid(row=i+1,column=6,columnspan=4)
        con.close()
        #=====total salary========
        totallabel = Label(self.mainWindow, text="Total salary:")
        totallabel.grid(row=i+2,column=1,columnspan=4)
        total = StringVar()
        total.set(totalSalary)
        Entry(self.mainWindow, textvariable = total).grid(row=i+2,column=4,columnspan=4)
        return result
    def CreateFram(self):
        self.mainWindow = Tk()
        self.mainWindow.title("Employee Data")
        self.mainWindow.geometry("600x500")

        self.name1 = StringVar()
        self.desig = StringVar()
        self.salary = IntVar()
        nameLabel = Label(self.mainWindow, text="Enter employee Name:")
        desigLabel = Label(self.mainWindow,text = "Enter employee Designation:")
        salaryLabel = Label(self.mainWindow, text = "Enter employee Salary:")

        e1 = Entry(self.mainWindow, textvariable = self.name1)
        e2 = Entry(self.mainWindow, textvariable = self.desig)
        e3 = Entry(self.mainWindow, textvariable = self.salary)

        nameLabel.grid(row=0,column=0,columnspan=4)
        e1.grid(row=0,column=5,columnspan=4)

        desigLabel.grid(row=2,column=0,columnspan=4)
        e2.grid(row=2,column=5,columnspan=4)

        salaryLabel.grid(row=4,column=0,columnspan=4)
        e3.grid(row=4,column=5,columnspan=5)

        btn = Button(self.mainWindow,bg="red",command = lambda : self.SaveRecord(),text = "Submit_final")
        btn.grid(row=7,column=4,rowspan = 4)

        self.getData() # Get data  
        self.mainWindow.mainloop()
s1 = Record()

s1.CreateFram()

