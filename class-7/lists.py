# Lists can hold any type of data, in this case, a list of strings
# Obs: If you create a list of any type, that list could only holds that specific type of data
names = ['Rafael', 'Ferreira', 'Paulo', 'João']
names.append('Silva')

print(len(names)) # number of items
names.insert(0, 'Bill') # insert before index
print(names)
names.sort()
print(names)

names_by_index = names[1:3] # start by the index '1', including the index '1', and finish by the index '3', not including the index '3'
names_by_index = names[:3] # when the first index is ommitted, it'll start by the index of '0' to index '3', with the same rules applied
print(names_by_index)


# Lists of dictionaries
person1 = {}
person1['name'] = 'rafael'
person1['age'] = 24

person2 = {}
person2['name'] = 'joao'
person2['age'] = 50

people = []
people.append(person1)
people.append(person2)

people.append({ 'name': 'bill', 'age': 70 }) # you can also create a item on the fly

print(people)