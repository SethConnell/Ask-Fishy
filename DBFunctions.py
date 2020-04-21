import MySQLdb

# Open database connection
class DB:
  conn = None

  def connect(self):
    self.conn = MySQLdb.connect(host="{USERNAME}.mysql.pythonanywhere-services.com",user="{USERNAME}",passwd="{PASSWORD}",db="{DATABASE NAME}" )

  def query(self, sql):
    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
      self.connect()
      cursor = self.conn.cursor()
      cursor.execute(sql)
    return cursor

db = DB()


def Setup():
    # Create infastructure for "Questions".
    sql ='''CREATE TABLE IF NOT EXISTS `Threads`(
       `question` CHAR(255) NOT NULL,
       `questionid` MEDIUMINT NOT NULL AUTO_INCREMENT,
       PRIMARY KEY (questionid)
    )'''
    db.query(sql)

    # Create infastructure for "Answers".
    sql ='''CREATE TABLE IF NOT EXISTS `User`(
       `name` CHAR(50) NOT NULL,
       `userid` MEDIUMINT NOT NULL AUTO_INCREMENT,
       PRIMARY KEY (userid)
    )'''
    db.query(sql)

    # Create infastructure for "Answers".
    sql ='''CREATE TABLE IF NOT EXISTS `Answers`(
       `questionid` MEDIUMINT NOT NULL,
       `answer` CHAR(255) NOT NULL
    )'''
    db.query(sql)

Setup()
