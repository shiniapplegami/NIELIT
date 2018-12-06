from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

s1="NLP is a way for computers to analyze, understand, and derive meaning from human language in a smart and useful way."
s2="The field of study that focuses on the interactions between human language and computers is called Natural Language Processing, or NLP for short"
s3="Natural Language Processing is a field that covers computer understanding and manipulation of human language, and it’s ripe with possibilities for news gathering."
s4="NLP algorithms are typically based on machine learning algorithms."
s5="One of the most compelling ways NLP offers valuable intelligence is by tracking sentiment — the tone of a written message (tweet, Facebook update, etc.) — and tag that text as positive, negative or neutral."

query="NLP focuses on machine learning algorithms and offers valuable intelligence"

data=(query,s1,s2,s3,s4,s5)

tfidf=TfidfVectorizer()

matrix=tfidf..fit_transform(data)

dict=tfidf.vocabulary_

for key in dict.keys():
    print(key+" "+str(dict[key]))

print("=====================")

print("matrix")

print(cosine_similarity(matrix[0:1],matrix))
