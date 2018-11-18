#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:02:38 2018

@author: vidhishajaswani
"""

import csv

csv.field_size_limit(100000000)

import pandas as pd


jira_sent=pd.read_csv(r"/Users/vidhishajaswani/Desktop/Padhai/Independent Study/sentences.csv",engine="python");
jira_sent=jira_sent.iloc[1:]

jira_convo_csv=pd.read_csv(r"/Users/vidhishajaswani/Desktop/Padhai/Independent Study/comments.csv",engine="python");

lst=[]

for i in range(1,len(jira_sent['sentence'])):
    sentence=jira_sent.loc[i].sentence
    oracle=jira_sent.loc[i].oracle
    for convo in jira_convo_csv['comment']:
        try:
            if sentence in convo:
                lst.append([sentence,oracle,convo])
        except:
            pass

cols=['sentence','oracle','comment']
sent_convo=pd.DataFrame(lst,columns=cols)
sent_convo.to_csv('sent_convo.csv')
