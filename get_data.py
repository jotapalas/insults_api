import MySQLdb
import MySQLdb.cursors
import config

def connect_to_db():
  mysql = MySQLdb.connect(
    host=config.DATABASE_CONFIG['host'],
    user=config.DATABASE_CONFIG['user'],
    passwd=config.DATABASE_CONFIG['password'],
    db=config.DATABASE_CONFIG['dbname'],
    cursorclass=MySQLdb.cursors.DictCursor
  )
  return mysql.cursor()

def get_data(table, fields=[]):
  query_fields = '*'
  if len(fields) > 0:
    query_fields = ','.join(fields)
  cursor = connect_to_db()
  query = "select %s from %s" % (query_fields, table)
  cursor.execute(query)
  return cursor.fetchall()
  
def get_data_mapped(table, fields=[], key='id'):
  data = get_data(table, fields)
  result = {}
  for d in data:
    result[d[key]] = d
  return result