x = 42
y = 0

try:
  print(x / y)
except ZeroDivisionError as e:
  print('Not allowed to divided by zero, error: {0}'.format(e))
else:
  print('something else is wrong')
finally:
  print('this is a clean up code')