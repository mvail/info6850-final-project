import sqlite3

dbpath = 'C:/Users/mvail.DS/Dropbox/MLIS/2016-2017/INFO 6850/Final Project/django/mysite/db.sqlite3'
path = "C:/Users/mvail.DS/Dropbox/MLIS/2016-2017/INFO 6850/Final Project/data/data/"

def connectDB():
    dblocation = dbpath
    conn = sqlite3.connect(dblocation)
    return conn;

def parse_metadata_csv(filename):
    print filename
    infile = open(filename,'r')
    line_count = 0
    db = connectDB()
    cursor = db.cursor()

    for line in infile:
        if line_count == 0:
            line_count += 1
            continue
        line = line.strip().split(',')
        
        SQL = "INSERT INTO reports_patent (pid,uspc,claims,inventors,week,ptext) VALUES (%d,%d,%d,%d,%d,'');" % (int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]))
        cursor = db.execute(SQL)
        
    db.commit()
    db.close()
    

def parse_texts_txt(filename):
    infile = open(filename,'r')
    line_count = 0;
    db = connectDB()
    cursor = db.cursor()

    for line in infile:
        if line_count == 0:
            line_count += 1
            continue
        line = line.strip().split('\t')
       
        SQL = "UPDATE reports_patent SET ptext = \"%s\" WHERE pid = %d;" % (line[1],int(line[0]))
        cursor = db.execute(SQL)
        
    db.commit()
    db.close()
    

parse_metadata_csv(path + 'metadata.csv')
parse_texts_txt(path + 'texts.txt')