# J = "aA"
J = "aAb"
# J = "z"

S = "aAAbbbb"

# print(list(J))  # ['a', 'A']


class Solution:
     def numJewelsInStones(self, J: str, S: str) -> int: 

          # Defining data types for function parameters and the return 
          # value can be used to let user know the expectations of the functions
          # 
          # def prime_numbers(x:int) -> (int, list):
          #      l=[]
          #      for i in range(x+1):
          #      if checkPrime(i):
          #           l.append(i)
          #      return len(l), l


          # j_dict = {}
          total = 0

          # for jewel in J:
          #      j_dict[jewel] = 0 # could set anything as value, we jsut want to see if key exists

          # another way to create dict from keys & assign value to None (default)
          # j_dict = dict.fromkeys(J)



          for stone in S:
               if stone in dict.fromkeys(J):  # even better !!!!!!
               # if stone in j_dict:  # after creating j_dict above
                    total += 1     

          return total


sol = Solution()
print(sol.numJewelsInStones(J, S))


# for ch in S:
#      if ch in J:
#           # if ch not in dict:
#           #      dict[ch] = 1
#           # else:
#           #      dict[ch] += 1     
#           total += 1     

# # for v in dict.values():
# #      total += v

# # looks clean, but has O(n^2) because in J is like a for loop iteration
# for ch in S:
#      if ch in J:   
#           total += 1  

# print(dict)
# print(total)

# for v in dict.values():
#      total += v