import sqlite3

dbpath = '/home/margaretvail/mysite/db.sqlite3'

def connectDB():
    dblocation = dbpath
    conn = sqlite3.connect(dblocation)
    return conn;

db = connectDB()

cursor = db.execute("SELECT DISTINCT week FROM reports_patent ORDER BY week")

weeks = []
for row in cursor:
    weeks.append(row[0])

for week in weeks:
    SQL = "SELECT uspc, week,  COUNT(USPC) as patent_count FROM reports_patent WHERE week = %d GROUP BY uspc, week ORDER BY  patent_count DESC" % week
    cursor2 = db.execute(SQL)

    for row2 in cursor2:
        SQL = "INSERT INTO reports_uspc(week,uspc,patent_count) VALUES (%d, %d, %d);" % (row2[1], row2[0], row2[2])
        cursor.execute(SQL)

    db.commit()


db.close()