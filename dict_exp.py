dict_count = {}
list = ['first', 'third', 'first']

for val in list:
    if val in dict_count:
        dict_count[val] += 1
    else:
        dict_count[val] = 1
    

print(dict_count)  # {'first': 2, 'third': 1}

print(dict_count["first"])


num_dict = {}
for item in range(10):
     num_dict[item] = str(item)

print(f' num_dict[5] is {num_dict[5]} type of value is {type(num_dict[5])}')

