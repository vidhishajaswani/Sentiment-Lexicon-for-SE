# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:06:55 2018

@author: Vidhisha
"""
import psycopg2
import pandas as pd
conn = psycopg2.connect("dbname=postgres user=postgres")
jira_convo = pd.read_sql_query('select * from jira_issue_comment',con=conn)
conn.close()


jira_sent=pd.read_csv("JIRA_sentences.csv",engine="python");
jira_sent["convo"]=""

            
for sentence in jira_sent['sentence']:
    for convo in jira_convo['comment']:
        if sentence in convo:
                jira_sent.loc[jira_sent["sentence"]==sentence,"convo"]+=convo


jira_sent.to_csv('jira.csv')