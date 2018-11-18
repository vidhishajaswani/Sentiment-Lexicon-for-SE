#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:06:36 2018

@author: vidhishajaswani
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)


data=pd.read_csv("sent_convo.csv")
train=data.iloc[:,1:3]
test=data.iloc[:,3:4]
test.columns=['sentence']

#clean the data
def cleanup(data):
    data.sentence = data.sentence.dropna()
    data=data.dropna(subset=['sentence'])
    data["sentence"]=data['sentence'].str.lower()
    
    data["sentence"]=data['sentence'].map(lambda x: x.strip())

    return data

train_clean=pd.DataFrame()
train_clean = cleanup(train)
test_clean = cleanup(test)


#word cloud
all_words = ' '.join([text for text in data['sentence']])
wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)
plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()


#vectorization
bow_vectorizer = CountVectorizer(binary=True)
bow = bow_vectorizer.fit_transform(train_clean['sentence'])
X = bow_vectorizer.transform(train_clean['sentence'])
X_test = bow_vectorizer.transform(test_clean['sentence'])

#model
X_train, X_val, y_train, y_val = train_test_split(
    X, train_clean['oracle'], train_size = 0.75
)
for c in [0.01, 0.05, 0.25, 0.5, 1]:
    
    lr = LogisticRegression(C=c)
    lr.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" 
           % (c, accuracy_score(y_val, lr.predict(X_val))))


final_model = LogisticRegression(C=0.01)
final_model.fit(X, train_clean['oracle'])
predictions=final_model.predict(X_test)
print ("Final Accuracy: %s" 
       % accuracy_score(train_clean['oracle'], final_model.predict(X_test)))

df=pd.DataFrame()
df['matches']= np.where(train_clean['oracle']==predictions, 
                                           'yes', 'no')
pd.value_counts(df['matches'].values, sort=False)
