# -*- coding: utf-8 -*-

import sqlite3
from collections import defaultdict
import string
from nltk.corpus import stopwords

# location of data files
path = 'C:/Users/mvail.DS/Dropbox/MLIS/2016-2017/INFO 6850/Final Project/'
'''Database location. Had to run this script on my personal computer because the server did not
have enough memory. I then exported the table and imported it on the server.'''
dbpath = 'C:/Users/mvail.DS/Dropbox/MLIS/2016-2017/INFO 6850/Final Project/django/mysite/db.sqlite3'

# Function to connect to sqlite database
def connectDB():
    dblocation = dbpath
    conn = sqlite3.connect(dblocation)
    return conn;

# Function to get the text data and week from the table reports_patent
def getDataForKeywords():

    # Connect to database
    db = connectDB()
    # Select text and week from table reports_patent
    cursor = db.execute("SELECT ptext, week from reports_patent")

    # create a default dictionary
    data = defaultdict(list)

    # for each row from the select statement
    for row in cursor:

        # Stip unneeded blank spaces from text. Assign ptext to line.
        line = row[0].strip()
        # assing week to week
        week = row[1]
        # add a new value to dict with the key week and the value line
        data[week].append(line)

    # Close database connection
    db.close()

    # return default dicitonary
    return data


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
            top_words.append(tword)
        new_d[year] = top_words
        #ADD YOUR LIST OF TOP WORDS TO new_d AT THE CORRECT YEAR
    return new_d

# Function to insert the top words into the database table reports_keywords
def insertTopwords(topwords):
    db = connectDB()
    c = db.cursor()

    for week in topwords:
        for word in topwords[week]:
            SQL = "INSERT INTO reports_keywords(word,word_count,week) VALUES ('%s', %d, %d);" % (word[0], word[1], week)
            c.execute(SQL)

    # commit all insert statements to database
    db.commit()
    # close database
    db.close()

# Get Keywords in a default dictionary
data = getDataForKeywords()

# get stop words
stops = set(stopwords.words('english'))

# remove punctuation from all text
cleaneddata = clean_text(data)

# get the top 200 words
topwords = common_words(cleaneddata,200);

# Call function insertTopwords
insertTopwords(topwords);