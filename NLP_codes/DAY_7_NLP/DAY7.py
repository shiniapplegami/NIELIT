from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
from textblob import Word
import math

s1="NLP is a way for computers to analyze, understand, and derive meaning from human language in a smart and useful way."
s2="The field of study that focuses on the interactions between human language and computers is called Natural Language Processing, or NLP for short"
s3="Natural Language Processing (NLP) is a sub field of Artificial Intelligence focussing on enabling computers to understand and process human languages, to get computers closer to a human level understanding of language."
s4="NLP algorithms are typically based on machine learning algorithms."
s5="One of the most compelling ways NLP offers valuable intelligence is by tracking sentiment, the tone of a written message (tweet, Facebook update, etc.)  and tag that text as positive, negative or neutral."

t1= TextBlob(s1)
t2= TextBlob(s2)
t3= TextBlob(s3)
t4= TextBlob(s4)
t5= TextBlob(s5)

docList=[t1,t2,t3,t4,t5]

for doc in docList:
    Wordlist = doc.words
    for word in Wordlist:
        tf=doc.words.count(word)
        print('{0} - - {1}'.format(word,str(tf)))

print("====================================")

data=[s1,s2,s3,s4,s5]
print(data)
print(tf)
'''        
tfidf=TfidfVectorizer(stop_words='english')

tfidf.fit(data)
dict=(tfidf.vocabulary_)

data1=tfidf.vocabulary_

print(data1.keys())
print(data1.values())

print(dict.keys())
print(dict.values())

for value in (dict.values()):
    print(value)
dict=tfidf.vocabulary_
documentnos=(
'''
