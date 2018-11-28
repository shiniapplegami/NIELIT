#!/usr/bin/python
A=raw_input("Enter a sentence")
A=A.split(' ')
A=A[::-1]
print A


N=raw_input("Enter a sentence").lower()
N=N.split(' ')
k=0
for word in N:
  if word==word[::-1]:
   k+=1
   print("Number pf palidnromes are",k)




A=raw_input("Enter a string")
ccd=dict()
for ch in A:
    if ch in ccd:
          ccd[ch]+=1
    else:
          ccd[ch]=1
print ccd





A=raw_input("Enter a sentence")
A=A.split(' ')
ccd=dict()
for word in A:
   if word in ccd:
      ccd[word]+=1
   else:
      ccd[word]=1
print ccd 
