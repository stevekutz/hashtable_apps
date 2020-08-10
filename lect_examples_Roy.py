import time

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
print(fib_1(3)) # 2
print(fib_1(5)) # 5
print(fib_1(6)) # 8
print(fib_1(8)) #21

print(f' this should take longer')
t1 = time.time()
print(fib_1(35))  # 9227465  because our recursion has exponential complexity

print("Time to find fib: %f " % (time.time() - t1))  # Time to find fib: 3.014418

# NOW do same thing but add a cache tp save previously calculated values
cache = {}
def fib(n):
     if n <= 1:
          return n
     if n in cache:
          return cache(n)

     else:
          cache[n] = fib(n-1) + fib(n-2)        
