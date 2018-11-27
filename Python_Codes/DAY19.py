import numpy as np

def array():
    start = int(input('Enter a start of array: '))
    

    stop = int(input('Enter a stop of array: '))
    stop = (stop+1)

    

    a = stop - start

    for i in range(2,11):
        if a%i==0:
            p=k/i
            q=i


    ar = np.arange(start, stop).reshape(p,q)

    print(ar)

    num = input('Enter a number: ')
    num = int(num)

    new1 = np.where(ar%num==0,ar,0)

    new2 = np.where(ar%num!=0,ar,0)


    print(new1)
    print(new2)

    np.savetxt('ar',ar, delimiter=',')
    np.savetxt('new1',new1, delimiter=',')
    np.savetxt('new2',new2, delimiter=',')


array()

Q1.py
Displaying Q1.py.



#-----------------------------------------------------

laptops = np.array([[1,5,2,3], [5,6,3,1], [7,6,2,1]])
sales = np.array([30000,35000,40000])

totalsales = np.dot(sales,laptops)

print("Total Sales are: \n" + str(totalsales))

#--------------------------------------------------

a = np.array([118.4, 135.2])
b = np.array([[3, 3.5], [3.2, 3.6]])

c = np.dot(a, np.linalg.inv(b))

print("The no. of children are: " + str(int(c[0])))
print("The no. of adults are: " + str(int(c[1])))



   
