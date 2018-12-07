from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


f=open("data.txt")
data=f.read()

query="India is the populous country and Bounded by the Indian Ocean while its Andaman and Nicobar Islands share a maritime border"

data=(query,data)

tfidf=TfidfVectorizer()

matrix=tfidf.fit_transform(data)

dict=tfidf.vocabulary_

for key in dict.keys():
    print(key+" "+str(dict[key]))

print("=====================")

#print(matrix)

print(cosine_similarity(matrix[0:1],matrix))

#-------------------------------------------------------------------------------------------------------------------
from textblob import TextBlob as tb

para=tb(data)

sent=para.sentences

s1=str(sent[0])
s2=str(sent[1])
s3=str(sent[2])
s4=str(sent[3])

query="India is the populous country and Bounded by the Indian Ocean while its Andaman and Nicobar Islands share a maritime border"

data=(query,s1,s2,s3,s4)

tfidf=TfidfVectorizer()

matrix=tfidf.fit_transform(data)

dict=tfidf.vocabulary_

for key in dict.keys():
    print("{0}  {1}" .format(key,dict[key]))

print("=====================")

#print(matrix)

print(cosine_similarity(matrix[0:1],matrix))
