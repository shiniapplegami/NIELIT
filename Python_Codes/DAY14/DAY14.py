'''
import re
fd=open('emp.csv','r').read().split('\n')
f1=open('sci.csv','w')

for d in fd:
    mo=re.search('scientist', d)
    if mo:       
        f1.write(d+'\n')
        print(d)
f1.close()
'''

#-----------------------------------------------------------------------------

'''
import re
fd=open('emp.csv','r').read().split('\n')
f1=open('ini1.csv','w')

for d in fd:
    mo=re.match(r'^[A-Z]' ,d)
    if mo:       
        f1.write(d + '\n')
        
f1.close()
'''

#-----------------------------------------------------------------------------

'''
import re
fd=open("emp.csv",'r').read().split('\n')
f1=open("ini2.csv",'w')

for d in fd:
	mo=re.match('.*[A-Z]\\.',d)
	if mo:
		f1.write(d +'\n')
f1.close() 
'''

#-----------------------------------------------------------------------------

'''
import re
fd=open("emp.csv",'r').read().split('\n')
f1=open("empphno.csv",'w')
for d in fd:
	#mo=re.match('[^,]+',i)
	me=re.split((','),d)
	if me:
		name=me[0]
		no=me[-1]
		no=re.sub('[^0-9]+','',no)
		f1.write("%s,%s\n" % (name,no))
f1.close() 
'''

#---------------------------------------------------------------------------
'''
import re
fd=open("emp.csv",'r').read()
f1=open("emp2.csv",'w')
for d in fd:
	mo=re.split(',',d)
	me=re.match('[2-9][0-9][0-9]',mo[1])
	if me:
		f1.write(d)
f1.close() 
'''
