num = 32
# string_of_digits = list(str(num))

# nicer way
class Solution:
     def __init__(self):
          self.seen_values = set()

     # def isHappy(self, n: int) -> (int, bool):   # works
     def isHappy(self, n: int) -> (bool):          # works    
     # def isHappy(self, n: int) -> bool:   ## ERROR in syntax, hmmmm   
          n = abs(n)
          
          if n == 1:
               return True

          # if n is in cache
          if n in self.seen_values:
               return False

          # Add n (even initial value) to cache
          self.seen_values.add(n)               


          # calculate another value
          # sum squre of all digits in str
          # new_num = sum([int(digit)**2  for digit in str(n)  ])

          # uglier way instead of using comprension
          new_num = 0
          for digit in str(n):
               new_num += int(digit)**2

          # enter recursion if we get this far
          return self.isHappy(new_num)



sol = Solution()
print(sol.isHappy(13))   # True 
print(sol.isHappy(12))   # False 
print(sol.isHappy(0))   # False  
print(sol.isHappy(-100)) # True      