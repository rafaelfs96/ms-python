from colorama import init, Fore

def display(message, is_warning = False):
  if is_warning:
    print(f'{Fore.RED}Warning!! {message}')
  else:
    print(f'{Fore.BLUE}{message}')