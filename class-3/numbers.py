num1 = 6
num2 = 2

print(num1 + num2)
print(num1 ** num2)

print('\nPrint numbers with strings using "f"')
print(f'{num1} plus {num2} is equals to {num1 + num2} \n')

print('Or print numbers with strings converting the numbers into string using "str(number)"')
print(str(num1) + ' plus ' + str(num2) + ' is equals to ' + str(num1 + num2) + '\n')

# Converting strings into numbers using 'int(string)' or 'float(string)'
# Obs: 'input()' method always returns a string
first_num = input('Enter a number: ')
second_num = input('Enter another number: ')
first_num = int(first_num)
second_num = float(second_num)

print(first_num)
print(second_num)
