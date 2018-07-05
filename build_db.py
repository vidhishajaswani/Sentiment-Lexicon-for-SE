# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:56:09 2018

@author: Vidhisha
"""
#reads sql file and builds the database in postgres
import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()
conn.autocommit=True
with open(r'C:\Users\Vidhisha\Desktop\New\Code\emotion_dataset_jira_issue_comment.sql',encoding="utf8") as fileobject:
    for line in fileobject:
        cur.execute(line)
               
conn.close()



