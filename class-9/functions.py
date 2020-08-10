from datetime import datetime

def print_time(task_name):
  time = datetime.now()
  print(f'\'{task_name}\' completed in {time}')

# Parameters might have a default value, in this case, 'force_uppercase' is 'True' by default
def get_initial(word, force_uppercase = True):
  if force_uppercase:
    initial = word[:1].upper()
  else: 
    initial = word[:1]

  return initial

for name in ['rafael', 'joao']:
  # Parameters can be passed to a function using named notation, simply type the parameter name and set it equals to the value you want to pass
  # in this case, get_initial(force_uppercase=True, word=name)
  initial = get_initial(force_uppercase=True, word=name)
  print(f'{name} with initial {initial}')
  
print_time('for loop')