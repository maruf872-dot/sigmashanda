my_dict = {}

my_dict = {1: 'Foot', 2: 'Ball'}

my_dict = {'name': 'John Doe', 1: [2, 4, 3]}

my_dict = {'name': 'Jane Doe', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 28
print(my_dict)

my_dict['address'] = 'Old town road'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address : ", my_dict.get('address'))

my_dict.clear()
print(my_dict)

