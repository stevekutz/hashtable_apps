## Hashtable fast because memory location(not linear like an array) is located via hashing

# Declare list with [ ]

x = ["first", "second", "third", "fourth"]

# print(x[0])   # first
# print(x[-4])    # first
# print(x[-5])    # IndexError: list index out of range

# # SLICING with lists
# # >>>>> slice(start, end, step)
# # >>>>>   [:n]   starts at beginning, ends JUST BEFORE index n
# # >>>>>   [m:]   starts at m and goes to the end

# print(x[0:2]) # ['first', 'second']
# print(x[1:2]) # ['second']
# print(x[1])   # second

# print(x[-1])   # fourth
# print(x[0:-1]) # ['first', 'second', 'third']
# print(x[1:-1]) # ['second', 'third']
# print(x[2:-1]) # ['third']
# print(x[3:-1]) # []

# print(x[-2:-1]) # ['third']
# print(x[-4:-1]) # ['first', 'second', 'third']
# print(x[-4:0]) # []
# print(x[-4:-5]) # []



# print(x[:2])     # ['first', 'second']
# print(x[:-1])  # ['first', 'second', 'third']
# print(x[:-2])  # ['first', 'second']

# print(x[2:])  # ['third', 'fourth']
# print(x[3:])  # ['fourth']


# print(x[:])   # ['first', 'second', 'third', 'fourth']

y = [0, 1, 2, 3]
# print(y[-4])    # 0
# print(y[-5])    # IndexError: list index out of range

# # SLICING with lists
# # >>>>> slice(start, end, step)
# # >>>>>   [:n]   starts at beginning, ends JUST BEFORE index n
# # >>>>>   [m:]   starts at m and goes to the end

# print(y[0:2]) # [0, 1]
# print(y[1:2]) # [1]
# print(y[1])   # 1

# print(y[-1])   # 4
# print(y[0:-1]) # [0, 1, 2]
# print(y[1:-1]) # [1, 2]
# print(y[2:-1]) # [2]
# print(y[3:-1]) # []

# print(y[-2:-1]) # [2]
# print(y[-4:-1]) # [0, 1, 2]
# print(y[-4:0]) # []
# print(y[-4:-5]) # []


# print(y[:2])     # [0, 1]
# print(y[:-1])  # [0, 1, 2]
# print(y[:-2])  # [0, 1]

# print(y[2:])  # [2, 3]
# print(y[3:])  # [3]


# print(y[:])   # [0, 1, 2, 3]

# z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# z = list(range(0, 10))

# print(z[1:9:3])         # [1, 4, 7]
# print(z[0:8:11])        # 0
# print(z[1::2])          # [1, 3, 5, 7, 9]
# print(z[::2])           # [0, 2, 4, 6, 8]
# print(z[:1:3])          # [0]
# print(z[::3])           # [0, 3, 6, 9]
# print(z[::])            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# list of common collections
list = [0, 2, "apple", {"key_name": "first_value"}, {0, 1, 2}, ("zero", "one")]
for index, item in enumerate(list): # must have index first with enumerate
    print(f' index {index} contains {item} of type {type(item)}')
    

#  index 0 contains 0 of type <class 'int'>
#  index 1 contains 2 of type <class 'int'>
#  index 2 contains apple of type <class 'str'>
#  index 3 contains {'key_name': 'first_value'} of type <class 'dict'>
#  index 4 contains {0, 1, 2} of type <class 'set'>
#  index 5 contains ('zero', 'one') of type <class 'tuple'>   

# list of dictionaries, enumerate to get index
list_dict = [{"first": "one", "second": "two", "third": "three"}]
for item in list_dict:
    for index, (k,v) in enumerate(item.items()):
        print(f' at index {index:<5} key is \t {k:<15} value is \t {v:<10}')

#  at index 0     key is   first           value is        one       
#  at index 1     key is   second          value is        two       
#  at index 2     key is   third           value is        three      


# Sort dictionary by key
##