def logger(func):
  def wrapper():
    print('logging execution')
    func()
    print('done logging')
  return wrapper

@logger
def log():
  print('bla')

log()