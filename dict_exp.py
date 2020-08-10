dict_count = {}
list = ['first', 'third', 'first']

for val in list:
    if val in dict_count:
        dict_count[val] += 1
    else:
        dict_count[val] = 1
    

print(dict_count)