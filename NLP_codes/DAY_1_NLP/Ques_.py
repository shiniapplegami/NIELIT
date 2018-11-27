from textblob import TextBlob
para=TextBlob ("The titular threat of the Blob has always struck me as the ultimate movie")
sent = para.sentences

print sent


from textblob import TextBlob

a=raw_input("Enter a string:")

o= TextBlob(a)

b=o.correct()

print b

d=o.translate(to='fr')
print (d)
print ("Translation in French is")
