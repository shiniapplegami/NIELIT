from textblob import TextBlob
para=TextBlob ("The titular threat of the Blob has always struck me as the ultimate movie.TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.")

sent = para.sentences

for t in sent:
    print t

words = para.words
for t in words:
    print t
para.noun_phrases
