import xml.dom.minidom as dm

f = open("kl.csv")

content = f.readlines()
elements = content[0].strip().split(',')


doc = dm.Document()


root = doc.createElement('root')

for c in content[1:]:
    datas = c.strip().split(',')
    emp = doc.createElement('employee')
    i=0
    for data in datas:
        child = doc.createElement(elements[i])
        child.appendChild(doc.createTextNode(data))
        emp.appendChild(child)    
        i +=1
    root.appendChild(emp)
    
doc.appendChild(root)

fd = open('employee.xml','w')

doc.writexml(fd)
