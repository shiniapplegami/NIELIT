import pandas as pd
import numpy as np

#-------------------------------------------------------------------------------------

drinks=pd.read_csv("drinks.csv")
print drinks.head()
print "======================="
group=drinks.groupby('continent')
print "\nContinent that drinks more beer on average :",group['beer_servings'].mean().idxmax()
print "======================="
print "\n",group['wine_servings'].describe()
print "======================="
print "\n",group.mean()
print "======================="
print "\n",group.median()
print "======================="
print group['spirit_servings'].describe()[['mean','min','max']]
