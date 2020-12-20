def sorter(item):
  return item['age']

presenters = [
  {'name': 'rafael', 'age': 24},
  {'name': 'joao', 'age': 10},
  {'name': 'maria', 'age': 4}
]

presenters.sort(key=lambda item: item['name'])
print(presenters)

presenters.sort(key=sorter)
print(presenters)