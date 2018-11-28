class employee:
    def store(self,name,empno,salary):
        self.name= name
        self.empno= empno
        self.salary= salary
    def display(self,name,empno,salary):
        print("Name is :", name)
        print("Empno is :", empno)
        print("Salary is:", salary)


#---------------------------------------------------------

class employee1:
    def __init__(self, name, empno, salary):
        self.name = name
        self.empno = empno
        self.salary = salary
    def display(self):
        print("Name is :", self.name)
        print("Empno is :", self.empno)
        print("Salary is:", self.salary)

p1= employee()
p1.display("Mayank", 25, 1290009)

p2= employee1("Hank", 3, 18032480)
p2.display()

#-------------------------------------------------------
class BankAccounts:
    cnt=0
    bank={}
    def __init__(self, an, ab, at, name, addr):
        self.AccountNumber= an
        self.AccountBalance= ab
        self.AccountType= at
        self.name= name
        self.address= addr

        bank=dict(AccountNumnber=self.AccountNumber, AccountBalance=self.AccountBalance, AccountType=self.AccountType, name=self.name, address=self.address)
        print(bank)
        BankAccounts.cnt+=1
        print("total accounts are", BankAccounts.cnt)

    def deposit(self):
        print("Account No", self.AccountNumber)
        print("Account Balance", self.AccountBalance)
        print("Account Type", self.AccountType)


    def getdetails(self):
        print("Account User Name", self.name)
        print("Users Address", self.address)
        print("Account Balance", self.AccountBalance)
        print("Account Type", self.AccountType)


p=BankAccounts(7,45000000000000000,"saving","Ankit_Ambani_Mittal_reliance's_owner_for_life","Jupiter_resident")
