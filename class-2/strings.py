first_name = input('what is your first name? ')
last_name = 'ferreira'

print('hello ' + first_name + ' ' + last_name)

print(first_name.upper())
print(first_name.lower())
print(first_name.capitalize())
print(first_name.count('a'))

format_without_index = 'Hello, {} {}'.format(first_name, last_name)
print(format_without_index)

format_with_index = 'Hello, {1} {0}'.format(last_name, first_name)
print(format_with_index)

# Only available in python3
format_inline = f'Hello, {first_name} {last_name}'
print(format_inline)
