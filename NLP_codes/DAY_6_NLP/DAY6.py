from textblob import TextBlob

s1="Ankit and Johnathan are good friends."

t1=TextBlob(s1)

#print(t1.sentiment)

if t1.sentiment.polarity>0:
    print("Positive")
elif t1.sentiment.polarity>0:
    print("Negative")
elif t1.sentiment.polarity>0:
    print("Neutral")

print("==================Question1End=============================")
    
#--------------------------------------------------------------------------------------------------------------------------------------------


import tweepy

consumer_key="bVRSYDDWk1aYk0RjXc9fLunJD"
consumer_secret="mvdY9mqvxEmMaAFYCidWcCKiKuLk4ywB7eCOuwnD7K2yRjOf0Q"
access_token="2601487261-qMaD0jHqMJWygUB6C8mttXASsI9QmcU6LFrWabU"
access_token_secret="Sfs7G46aMhpDGI779xUFtL2BUsYqo0AGmRIBjhClYXC9X"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token=(access_token,access_token_secret)

api=tweepy.API(auth)

posCount=0
negCount=0
neuCount=0

public_tweets=api.user_timeline("@FIFAcom",count=10)

for tweets in public_tweets:
    print("==============================================")

    print (tweets.text)
    
    t1=TextBlob(tweets.text)
    if t1.sentiment.polarity>0:
        print("Positive")
        posCount+=1
    if t1.sentiment.polarity<0:
        print("Negative")
        negCount+=1 
    if t1.sentiment.polarity==0:
        print("Neutral")
        neuCount+=1

print("Positive count:{0}" .format(posCount))
print("Negative count:{0}" .format(negCount))
print("Neutral count:{0}" .format(neuCount))
