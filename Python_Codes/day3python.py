#!/usr/bin/python
string=input("Enter string:")
a=0
for i in string:
      a=a+1
print("Length of the string is:")
print(a)

string=input("Enter string:")
b=string[::-1]
print(b)






string=input("Enter string:")
character=input("Enter a character")
a=0
for i in string:
  if i==character:
       a=a+1

print(a)




string=input("Enter string:").lower()
k=0
vowels='aeiou'
for char in string: 
  if char in vowels:
    print(char)
    k=k+1
if k>=2:
  print("The string has alteast two vowels")
