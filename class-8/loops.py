people = ['Rafael', 'Joao']
for name in people:
  print(name)

# range will simply create an array with the passed parameters ('0' is the starting number, '2' is the number of items), in this case: [0, 1]
for index in range(0, 2):
  print(index)

index = 0
while index < len(people):
  print(people[index])
  # the condition must change in every interaction, in this case, while 'index < len(people)' is True, the interaction is going to happen
  index = index + 1
  