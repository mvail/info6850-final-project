import sqlite3

# Database location
dbpath = '/home/margaretvail/mysite/db.sqlite3'
# Data location
path = "/home/margaretvail/data/"

# Function to connect to sqlite database
def connectDB():
    dblocation = dbpath
    conn = sqlite3.connect(dblocation)
    return conn;

# Parse and insert metadata.csv data into sqlite database
def parse_metadata_csv(filename):

    # open file
    infile = open(filename,'r')
    line_count = 0

    # Connect to database
    db = connectDB()
    cursor = db.cursor()

    # Insert data from the csv file into the database
    for line in infile:
        if line_count == 0:
            line_count += 1
            continue
        line = line.strip().split(',')

        SQL = "INSERT INTO reports_patent (pid,uspc,claims,inventors,week,ptext) VALUES (%d,%d,%d,%d,%d,'');" % (int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]))
        cursor = db.execute(SQL)

    # commit all insert statements to database
    db.commit()
    # close database
    db.close()

# Parse and insert texts.txt data into sqlite database
def parse_texts_txt(filename):

    # open file
    infile = open(filename,'r')
    line_count = 0;

    # Connect to database
    db = connectDB()
    cursor = db.cursor()

    # Insert data from the txt file into the database
    for line in infile:
        if line_count == 0:
            line_count += 1
            continue
        line = line.strip().split('\t')

        SQL = "UPDATE reports_patent SET ptext = \"%s\" WHERE pid = %d;" % (line[1],int(line[0]))
        cursor = db.execute(SQL)

    # commit all insert statements to database
    db.commit()
    # close database
    db.close()

#call parse_metadata_csv function with file name
parse_metadata_csv(path + 'metadata.csv')
#call parse_texts_txt function with file name
parse_texts_txt(path + 'texts.txt')