class Loggable:
  def __init__(self):
    self.title = ''
  def log(self):
    print(f'log message from {self.title}')

class Connection:
  def __init__(self):
    self.server = ''
  def connect(self):
    print(f'connecting to database on {self.server}')

# use the framework
# inherit from Connection and Loggable
class SqlDatabase(Connection, Loggable):
  def __init__(self):
    self.title = 'sql connection demo'
    self.server = 'some_server'

def framework(item):
  if isinstance(item, Connection):
    item.connect()
  if isinstance(item, Loggable):
    item.log()

sql_connection = SqlDatabase()
framework(sql_connection)