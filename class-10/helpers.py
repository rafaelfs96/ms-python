def display(message, is_warning = False):
  if is_warning:
    print(f'Warning!! {message}')
  else:
    print(message)