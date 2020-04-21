import re
from DBFunctions import *
def search(question):
    fixedquery = re.sub('\W', '', question)

    sql = '''SELECT * FROM Threads WHERE `question` = "''' + str(fixedquery) + '"'
    records = db.query(sql).fetchone()

    if records is not None:
        threadid = records[1]
        return int(threadid)
    else:
        sql = "INSERT INTO `Threads` (question) VALUES ('" + str(fixedquery) + "')"
        threadid = db.query(sql).lastrowid
        return int(threadid)
