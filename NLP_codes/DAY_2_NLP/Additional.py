from textblob import TextBlob
from textblob import Word
import pandas as pd
import random

noun = pd.read_csv('noun.txt', header = None)
print("TYPE 'Exit' ANY TIME TO EXIT THE GAME")

arr = []
for i in range(0, len(noun.iloc[:,0])):
    arr.append(noun.iloc[i,0])

while(True):
    r = random.randint(0, len(noun.iloc[:,0]))
    print('--------------------------------')

    x = noun.iloc[r,0]
    s = raw_input('Enter the Plural form for ' + x + ' ')

    theWord = Word(x)

    if (s == theWord.pluralize()):
        print('Well Done! You did a good job.')
    elif(s == 'exit'):
        break
    else:
        print('Sorry! Your answer was incorrect.')
        print('The correct answer is: ' + '"' + theWord.pluralize() + '"')

    r = random.randint(0, len(noun.iloc[:,0]))
    print('--------------------------------')
    x = noun.iloc[r,0]
    theWord = Word(x)
    y = theWord.pluralize()
    s = raw_input('Enter the Singular form for ' + y + ' ')

    if (s == x):
        print('Well Done! You did a good job.')
    elif(s == 'exit'):
        break
    else:
        print('Sorry! Your answer was wrong.')
        print('The correct answer is: ' + '"' + x + '"')
