# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:06:55 2018

@author: Vidhisha
"""

import sys
import csv

csv.field_size_limit(100000000)

import psycopg2
import pandas as pd
conn = psycopg2.connect("dbname=postgres user=postgres")
jira_convo = pd.read_sql_query('select comment from jira_issue_comment',con=conn)
jira_convo.to_csv('jira_convo.csv')
conn.close()

jira_sent=pd.read_csv(r"C:\Users\Vidhisha\Desktop\New\Code\Final\JIRA_sentences.csv",engine="python");
jira_sent["convo"]=""

jira_convo_csv=pd.read_csv(r"C:\Users\Vidhisha\Desktop\New\Code\Final\jira_convo.csv",engine="python");


            
for sentence in jira_sent['sentence']:
    for convo in jira_convo_csv['comment']:
        #print(convo)
        try:
            if sentence in convo:
                jira_sent.loc[jira_sent["sentence"]==sentence,"convo"]+="NEW ENTRY\n"
                jira_sent.loc[jira_sent["sentence"]==sentence,"convo"]+=convo
        except:
            pass


jira_sent.to_csv('jira.csv')
