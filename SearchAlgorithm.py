import re
from DBFunctions import *
# Right now, this search function is vulnerable to SQL injection. It will be fixed.
def search(question):
    fixedquery = re.sub('\W', '', question)
    sql = "SELECT * FROM Threads WHERE `question` = '%s'" % fixedquery
    records = db.query(sql).fetchone()

    if records is not None:
        threadid = records[1]
        return int(threadid)
    else:
        sql = "INSERT INTO `Threads` (question) VALUES ('%s')" % fixedquery

        threadid = db.query(sql).lastrowid
        return int(threadid)
