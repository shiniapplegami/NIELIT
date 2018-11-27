import os
from textblob.classifiers import NaiveBayesClassifier
f=open("CategoryDescription.txt")
dsc=[]
filename=[]
traindata=[]
data=f.readline().strip()
while data:
    #data=f.readline().strip()
    datasplit=data.split(",")
    con=datasplit[0]
    cat=datasplit[1]
    tuple=(con,cat)
    dsc.append(tuple)
    data=f.readline().strip()
    #print tuple
for i in dsc:
    #print i[1]
    s="/"+str(i[1])+"/file.txt"
    path=os.getcwd()+s
    f=open(path)
    data=f.readline().strip()
    while data:
        splitdata=data.split()
        #print splitdata[4]
        tuple=(splitdata[4],i[1])
        #print tuple
        filename.append(tuple)
        data=f.readline().strip()
for i in filename:
    s="/"+str(i[1])+"/"+str(i[0])
    path=os.getcwd()+s
    f=open(path)
    data=f.read()
    while data:
        #splitdata=data.split()
        #print data
        tuple=(data,i[1])
        #print tuple
        traindata.append(tuple)
        data=f.readline().strip()
#print traindata[1]        
classifier=NaiveBayesClassifier(traindata)
print classifier.classify("""Excitatory amino acids in the developing brain: ontogeny, plasticity, and excitotoxicity.
 Besides their role as neurotransmitters, excitatory amino acids (EAAs) in the developing brain are crucially involved in plasticity and excitotoxicity which are modified by their distinct ontogeny.
 Along with incomplete neuritogenesis and synaptogenesis, presynaptic markers of the EAA system are immature in the developing brain; however, postsynaptic EAA system activities, particularly of the N-methyl-D-aspartate and quisqualate receptors, are transiently enhanced early in life.
 This transient enhancement is presumably beneficial to the immature brain because physiologic activation of the EAA system plays a critical role in plasticity of early learning and morphogenesis.
 At the same time, this transient hypersensitivity renders the immature brain vulnerable to pathologic excitation of the EAA system (excitotoxicity) as observed during neonatal hypoxia-ischemia.
""")
