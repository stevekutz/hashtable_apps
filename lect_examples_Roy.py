import time, math

# fib sequence
# num is sum of previous 2 numbers
# e.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, .....

## components for recursion to work
# 1) base case >> where to stop recursion
# 2) calls itself from within
# 3) each iteration approaches base case

# recursive func for fib
# Find nth value in fib sequence
# F(n) = F(n-1) + F(n-2) where F1 & F2 = 1

# COMPLEXITY recursive-fibonacci's complexity is O(2^n)
def fib_1(n):
     # stop condition >> base case
     if n <= 1:
          return n
     return fib_1(n-1) + fib_1(n-2)     

# at index 4
# starting at index[0] the 'first' 1: the index[4] fib number is 5
# print(fib_1(3)) # 2
# print(fib_1(5)) # 5
# print(fib_1(6)) # 8
# print(fib_1(8)) #21

# print(f' this should take longer')
# t1 = time.time()
# print(fib_1(35))  # 9227465  because our recursion has exponential complexity

# print("Time to find fib: %f " % (time.time() - t1))  # Time to find fib: 3.014418

# NOW do same thing but add a cache tp save previously calculated values
# cache = {}
# def fib(n):
#      if n <= 1:
#           return n
#      if n in cache:
#           return cache[n]

#      else:
#           cache[n] = fib(n-1) + fib(n-2) 
#           # print(f' current cache is {cache[n]}')
#      return cache[n]             

# print(f' this should go fast !!! ')
# t1 = time.time()
# print(fib(35))  # 9227465  because we cached previously used fib seq values

# print("Time to find fib: %f " % (time.time() - t1))  # Time to find fib: 0.000025

# memoization or memoisation is an optimization technique used primarily to speed up 
# computer programs by storing the results of expensive function calls and returning the 
# cached result when the same inputs occur again

# refactored
# cache = {}
# def fib(n):
#      if n <= 1:
#           return n
#      if n not in cache:
#           cache[n] = fib(n-1) + fib(n-2)     

#      return cache[n]

# print(f' this should go fast as well, just refactored !!! ')
# t1 = time.time()
# print(fib(35))  # 9227465  because we cached previously used fib seq values

# print("Time to find fib: %f " % (time.time() - t1))  # Time to find fib: 0.000024          


# # Lookup table example with inverse roots
# lookup_table = {}

# def inverse_root(n):
#      return 1/ math.sqrt(n)

# def build_lookup_table():
#      for i in range(1,1001):
#           lookup_table[i] = inverse_root(i)

# # build up some value to store and retrieve          
# build_lookup_table()

# t1 = time.time()
# inverse_root(556)
# print("Time to find inverse root: %f " % (time.time() - t1))


# t1 = time.time()
# print(lookup_table[556])
# print("Time to lookup inverse root: %f " % (time.time() - t1))  # Time to find inverse root: 0.000006  

# # sorting dicts
# d = {
#      'Austin': 12,
#      'Michael': 24,
#      'Troy': 35,
#      'Jorge': 99,
#      'David': 42
# }

# # 
# print(f'{d}')
# # [('Austin', 12), ('David', 42), ('Jorge', 99), ('Michael', 24), ('Troy', 35)]


# ##### CONVERT TO LIST EXAMPLES  
# # one method is to covert to a list  & we sort(by key) for fun
# list_from_dict = sorted(list(d.items()))  # [('Austin', 12), ('David', 42), ('Jorge', 99), ('Michael', 24), ('Troy', 35)]
# print(list_from_dict)

# # REMEMBER sort does sort in place and mututes orig list
# sort_list_from_dict = list(d.items())
# print(sort_list_from_dict)  # [('Austin', 12), ('Michael', 24), ('Troy', 35), ('Jorge', 99), ('David', 42)]
# # when we use sort, list is now changed and sorted
# sort_list_from_dict.sort()
# print(sort_list_from_dict)  # [('Austin', 12), ('David', 42), ('Jorge', 99), ('Michael', 24), ('Troy', 35)]

# ## SORT by item value
# # Use list comprehension to sort dict
# print(f' v,k for k,v {sorted([(v,k) for k,v in d.items()])}') 
# # v,k for k,v [(12, 'Austin'), (24, 'Michael'), (35, 'Troy'), (42, 'David'), (99, 'Jorge')]

# print(f' k,v for k,v {sorted([(k,v) for k,v in d.items()])}') 
# # k,v for k,v [('Austin', 12), ('David', 42), ('Jorge', 99), ('Michael', 24), ('Troy', 35)]

# #### SWAP   key & value 
# # A dict comprehension to swap k & v
# reversed_dict = {v: k for k,v in d.items()}
# print(f' v: k  {reversed_dict} ')  
# # v: k  {12: 'Austin', 24: 'Michael', 35: 'Troy', 99: 'Jorge', 42: 'David'}

# # using lambda to sort by index using key parameter in sort
# sorted_list2 = list(d.items())
# print(f' List is : {sorted_list2}')


# def anon_func(pair):
#      return pair[1]

# sorted_list2.sort(reverse=True, key = anon_func)
# print(sorted_list2)
# # [('Jorge', 99), ('David', 42), ('Troy', 35), ('Michael', 24), ('Austin', 12)]

# # Another way  sort by index[1]>> value   & in REVERSE order
# sorted_list3 = list(d.items())
# sorted_list3.sort(reverse=True, key = lambda x: x[1])
# print(f' reverse sort vy value  {sorted_list3}')
# # reverse sort vy value  [('Jorge', 99), ('David', 42), ('Troy', 35), ('Michael', 24), ('Austin', 12)]


# # Another way
# sorted_list3.sort(reverse=True, key = lambda x: x[0])
# print(f' reverse sorted by key {sorted_list3}')
# # reverse sorted by key [('Troy', 35), ('Michael', 24), ('Jorge', 99), ('David', 42), ('Austin', 12)]

# # MORE lambda examples using map
# nums = [2, 7 ,3 ,1, 9, 5, 0]

# map_list = list(map(lambda x: x*2, nums))
# print(f'lambda map ex {map_list}')  # lambda map ex [4, 14, 6, 2, 18, 10, 0]

# # another way
# triple = lambda val: val*3
# map_list2 = list(map(triple, nums))
# print(f'calling lambda {map_list2}')
# print(f' nums is {nums}')

# USING HASHTABLES to print letter count in string
def print_letter_count(s):
     tally = {}

     s = s.lower()
     for char in s:
          # to make sure char counted is actual char & not space
          # if char >= 'a' and char <= 'z':
          # if char != ' ':
          if not char.isspace():
               if char in tally:
                    tally[char] += 1
               else:
                    tally[char] = 1

     ########  return tally using 'sorted'
     # to return sorted by 'key'
     # return sorted(tally.items(), key = lambda x: x[0], reverse = True )
          # [('y', 1), ('s', 5), ('p', 1), ('m', 1), ('l', 1), ('i', 1)]

     # return sorted(tally.items(), key = lambda x: x[1], reverse = True)
          # [('s', 5), ('i', 1), ('m', 1), ('p', 1), ('l', 1), ('y', 1)]

     ######## return using list   REMEMBER!!!  'sort' works in place
     #  sort by value
     # tally_list = list(tally.items())   # convert to list
     # tally_list.sort( key = lambda x: x[1], reverse = True)  # returns None if called
     # return tally_list
     # # [('s', 5), ('i', 1), ('m', 1), ('p', 1), ('l', 1), ('y', 1)]

     # tally_list = list(tally.items())   # convert to list
     # tally_list.sort( key = lambda x: (-(x[1]))) 
     # return tally_list
     # # [('s', 5), ('i', 1), ('m', 1), ('p', 1), ('l', 1), ('y', 1)]

     # # to just return printed list
     # #  sort by value
     # tally_list = list(tally.items())   # convert to list
     # tally_list.sort( key = lambda x: x[1], reverse = True)  # returns None if called

     # for pair in tally_list:
     #      print(f' letter {pair[0]} key {pair[1]}')
     #      letter s key 5
     # # letter i key 1
     # # letter m key 1
     # # letter p key 1
     # # letter l key 1
     # # letter y key 1


     # BEST WAY
     # print out sorted dict using lambda, sort by value
     print({key: value for key, value in sorted(tally.items(), key = lambda item: item[1], reverse = True)})
     # {'s': 5, 'i': 1, 'm': 1, 'p': 1, 'l': 1, 'y': 1}le

s = "simply ssss"
# print_letter_count(s)
print(print_letter_count(s))
