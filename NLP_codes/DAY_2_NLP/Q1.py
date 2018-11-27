from textblob import TextBlob
from textblob import Word
W=Word(raw_input("Enter a singular noun: "))
print(W + " " + W.pluralize())

#-------------------------------------------------------------------------------

t=Word("Trees")
print(" Singular noun of the word is :", t + " " +t.singularize())


#-------------------------------------------------------------------------------

from textblob import TextBlob

sentence=TextBlob(raw_input("Enter a sentence: "))

print(sentence.tags)

#-------------------------------------------------------------------------------

f=open("USA.txt","r")
text=f.read()
Para=TextBlob(text)
theSentences=Para.sentences

print("No. of sentences: " + str(len(Para.sentences)))
print("No. of words: " + str(len(Para.words)))
noun=set()
for word,tag in Para.tags:
     if tag =="NN"or tag=="NNS":
         noun.add(word)

print(noun)

mainString=""
for n in noun:
    mainString= n+","+mainString
print("The main words are: ",mainString)

theSent=Para.sentences
title=theSent[0]
print(title)
Len=len(Para.sentences)
    

print("Summary of"+str(title))
print("-----------------------")

print(theSent[1])
print(theSent[Len-1])

