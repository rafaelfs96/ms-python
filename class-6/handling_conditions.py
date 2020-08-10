country = input('enter the name of your home country: ')

if country.capitalize() == 'Canada':
  province = input('what province/state do you live in? ')

  # if province == 'Alberta' or province == 'Nunavut' or province == 'Yukon':
  if province.capitalize() in('Alberta', 'Nunavut', 'Yukon'):
    tax = .05
  elif province.capitalize() == 'Ontario':
    tax = .13
  else:
    tax = .15
else:
  tax = 0
print(f'Tax is {tax}%')


gpa = float(input('what was your grade point average? '))
lowest_grade = float(input('what was your lowest grade? '))

honour_roll = gpa >= .85 and lowest_grade >= .70
if honour_roll:
  print('you made honour roll')