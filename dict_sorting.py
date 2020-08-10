dict = {
    'first': 'Joe',
    'middle': 'Joe', # this is duplicate val, see Sets below
    'last': 'Smith',
#    'dog': True,
    'dog_name': 'Spot',
    'first': 'Joe',
    'first': 'Mike', # this just ovewrites first
}

#print key, value pairs  item() method sets up key-value pairs
for k, v in dict.items():
    print(f'key: {k}, value: {v}')
print("\n")

# key: first, value: Mike
# key: middle, value: Joe
# key: last, value: Smith
# key: dog_name, value: Spot


# print all keys  # keys() method is optional
for ccc in dict:
    print("key is: ", ccc)    
print("\n")

# print all keys
for ccc in dict.keys():
    print("key is: ", ccc)    
print("\n")

# key is:  first
# key is:  middle
# key is:  last
# key is:  dog_name

# print values
for v in dict.values():    
    print(f'Value is: {v}')
print("\n")    

# Value is: Mike
# Value is: Joe
# Value is: Smith
# Value is: Spot


# print in sorted order by VALUE
for v in sorted(dict.values()):
    print(f'Sorted val: {v}')
print("\n") 

# Sorted val: Joe
# Sorted val: Mike
# Sorted val: Smith
# Sorted val: Spot

# print in sorted order by KEY
for k in sorted(dict): 
    print(f' Sorted key is: {k}')    
print("\n")

#  Sorted key is: dog_name
#  Sorted key is: first
#  Sorted key is: last
#  Sorted key is: middle


# just print of values as interated
for v in dict.values():    
    print(f'dict Value is: {v}')
print("\n")

for v in set(dict.values()):
    print(f' Unique Set values from dict are: {v}')  

#  Unique Set values from dict are: Spot
#  Unique Set values from dict are: Joe
#  Unique Set values from dict are: Mike
#  Unique Set values from dict are: Smith    

print("\n")
# check if Spot belongs to dict as key
print('Spot' in dict)      # False

print("\n")
# check if Spot belongs to dict as value
print('Spot' in dict.values())     # True
print("\n")
print('last' in dict)       # True