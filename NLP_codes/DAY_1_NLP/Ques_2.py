from textblob import TextBlob

a=raw_input("Enter a string:")

o= TextBlob (a)

b=a.correct()

print b
