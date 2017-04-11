# -*- coding: utf-8 -*-

import sqlite3
from collections import defaultdict
import string
from nltk.corpus import stopwords

path = 'C:/Users/mvail.DS/Dropbox/MLIS/2016-2017/INFO 6850/Final Project/'
dbpath = 'C:/Users/mvail.DS/Dropbox/MLIS/2016-2017/INFO 6850/Final Project/django/mysite/db.sqlite3'
#path = 'C:/Users/margaret/Dropbox/MLIS/2016-2017/INFO 6850/Final Project/'

def connectDB():
    dblocation = dbpath
    conn = sqlite3.connect(dblocation)
    return conn;

def getDataForKeywords():
    db = connectDB()
    cursor = db.execute("SELECT ptext, week from reports_patent")

    data = defaultdict(list)
    for row in cursor:

        line = row[0].strip()
        week = row[1]
       
        data[week].append(line)
    
    db.close()

    return data

data = getDataForKeywords()

stops = set(stopwords.words('english'))

def clean_text(d):
    '''removes punctuation from all abstracts, returns 
    dict keyed by year, with cleaned abstract text as list values'''

    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    new_d = defaultdict(list)
    for week in d:
        for abstract in d[week]:
            cleaned = abstract.lower().translate(remove_punctuation_map)
            new_d[week].append(cleaned)
    return new_d
        
cleaneddata = clean_text(data)
        
from collections import Counter

def common_words(d, n):
    '''takes a dictionary keyed by year, with lists of abstracts as values
    returns a dictionary keyed by the same years, but values 
    will be a list of the n most common words from that year'''
    new_d = {}
    for year in d:
        words = []
        for abstract in d[year]:
            allwords = abstract.split()
            for word in allwords:
                if word not in stops and not word.isdigit() and len(word) > 3:
                    words.append(word)
        #DO YOUR COUNTER MAGIC HERE AFTER THE 'words' LIST IS COMPLETE
        top_words = []
        top = Counter(words).most_common(n)
        for tword in top:
            top_words.append(tword[0])
        new_d[year] = top_words
        #ADD YOUR LIST OF TOP WORDS TO new_d AT THE CORRECT YEAR
    return new_d

        
topwords = common_words(cleaneddata,50);


def insertTopwords(topwords):
    db = connectDB()
    c = db.cursor()
    
    for week in topwords:
        for word in topwords[week]:
            SQL = "INSERT INTO reports_keywords(word,word_count,week) VALUES ('%s', %d, %d);" % (word, word_count, week)
            c.execute(SQL)
    
    db.commit()
    db.close()
            

insertTopwords(topwords);