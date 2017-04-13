import sqlite3

# Database location
dbpath = '/home/margaretvail/mysite/db.sqlite3'

# Function to connect to sqlite database
def connectDB():
    dblocation = dbpath
    conn = sqlite3.connect(dblocation)
    return conn;

# Connect to database
db = connectDB()

# Select unique weeks from database
cursor = db.execute("SELECT DISTINCT week FROM reports_patent ORDER BY week")

weeks = []

# Add each week to weeks list
for row in cursor:
    weeks.append(row[0])

# For each week..
for week in weeks:
    # Get uspc, week, and patent count from the patents table
    SQL = "SELECT uspc, week,  COUNT(USPC) as patent_count FROM reports_patent WHERE week = %d GROUP BY uspc, week ORDER BY  patent_count DESC" % week
    cursor2 = db.execute(SQL)

    # insert the week, uspc, and patent count into a new table called reports_uspc
    for row2 in cursor2:
        SQL = "INSERT INTO reports_uspc(week,uspc,patent_count) VALUES (%d, %d, %d);" % (row2[1], row2[0], row2[2])
        cursor.execute(SQL)

    # commit all insert statements to database
    db.commit()

# close database
db.close()