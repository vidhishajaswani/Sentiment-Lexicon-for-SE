# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:22:14 2018

@author: Vidhisha
"""
import pandas as pd
import string
import matplotlib.pyplot as plt
import numpy as np
import nltk

data=pd.read_csv('final.csv')

df = data
neg = len(df[df["oracle"] == -1])
pos = len(df[df["oracle"] == 1])
neu = len(df[df["oracle"] == 0])
plt.bar(np.arange(3),(neg,pos,neu))
plt.xticks(np.arange(3),("Negative","Positive","Neutral"))



def cleanup(data):
    data.sentence = data.sentence.dropna()
    data=data.dropna(subset=['sentence'])
    data["sentence"]=data['sentence'].str.lower()
    
    data["sentence"]=data['sentence'].map(lambda x: x.strip())
    
    
    for p in list(string.punctuation):
        data["sentence"]=data["sentence"].apply(lambda x: x.replace(p,''))
        
    for d in list(string.digits):
        data["sentence"]=data["sentence"].apply(lambda x: x.replace(d,''))


    return data

def tokenize_row(row):
        tokenizer=nltk.word_tokenize
        row["sentence"] = tokenizer(row["sentence"])
        row["tokenized_text"] = [] + row["sentence"]
        return row
def stemfunc(row):
    stemmer=nltk.PorterStemmer()
    row["sentence"] = list(map(lambda str: stemmer.stem(str.lower()), row["sentence"]))
    return row

  
       
df=cleanup(df)
df = df.apply(tokenize_row, axis=1)
df = df.apply(stemfunc, axis=1)


    










    