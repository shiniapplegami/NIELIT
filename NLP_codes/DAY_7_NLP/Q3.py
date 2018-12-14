
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
"NLP is a way for computers to analyze, understand, and derive meaning from human language in a smart and useful way.",
"The field of study that focuses on the interactions between human language and computers is called Natural Language Processing, or NLP for short.",
"Natural Language Processing (NLP) is a sub field of Artificial Intelligence focussing on enabling computers to understand and process human languages, to get computers closer to a human level understanding of language.",
"NLP algorithms are typically based on machine learning algorithms.",
"One of the most compelling ways NLP offers valuable intelligence is by tracking sentiment, the tone of a written message (tweet, Facebook update, etc.)  and tag that text as positive, negative or neutral."]

tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(documents)
dict = tfidf.vocabulary_
print tfidf.vocabulary_
counts = dict.values()

length = len(dict.keys())
x_lab = []
for key in dict.keys():
	x_lab.append(key)

print 'Length :', length
words = np.arange(0,length)

model = KMeans(n_clusters=length);
X = list(zip(words, counts))
model.fit(X)

print(model.labels_)
print dict.keys()

plt.scatter(words,counts,c=model.labels_)
plt.xlabel("Words")
plt.ylabel("Occurance")
plt.xticks(words, x_lab, rotation=90)
#plt.legend(loc="best", labels=x_lab)
plt.show()
