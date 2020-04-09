import MySQLdb

# Open database connection
db = MySQLdb.connect(host="{USERNAME}.mysql.pythonanywhere-services.com",user="{USERNAME}",passwd="{PASSWORD}",db="{DATABASE NAME}" )

cursor = db.cursor()

def Setup():
    # Create infastructure for "Questions".
    sql ='''CREATE TABLE IF NOT EXISTS `Threads`(
       `question` CHAR(255) NOT NULL,
       `questionid` MEDIUMINT NOT NULL AUTO_INCREMENT,
       PRIMARY KEY (questionid)
    )'''
    cursor.execute(sql)

    # Create infastructure for "Answers".
    sql ='''CREATE TABLE IF NOT EXISTS `User`(
       `name` CHAR(50) NOT NULL,
       `userid` MEDIUMINT NOT NULL AUTO_INCREMENT,
       PRIMARY KEY (userid)
    )'''
    cursor.execute(sql)

    # Create infastructure for "Answers".
    sql ='''CREATE TABLE IF NOT EXISTS `Answers`(
       `questionid` MEDIUMINT NOT NULL,
       `answer` CHAR(255) NOT NULL
    )'''
    cursor.execute(sql)

Setup()
