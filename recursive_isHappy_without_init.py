# def isHappy(self, n, answer_set=None):
# def isHappy(n, answer_set=None):
#      if answer_set == None:
#           answer_set = set()
#      if n == 1:
#           return True
#      elif n in self.answer_set:
#           return False

#      new_num = sum([int(digit)**2 for digit in str(n)])
#      self.answer_set.add(n)
#      return self.isHappy(new_num, answer_set)

# 19 True
# 20 False

# print(isHappy(19)) 
# print(isHappy(20))    


def isHappy(n, answer_set=None):
     if answer_set == None:
          answer_set = set()
     if n == 1:
          return True
     elif n in answer_set:
          return False

     new_num = sum([int(digit)**2 for digit in str(n)])
     answer_set.add(n)
     return isHappy(new_num, answer_set)

print(isHappy(19)) 
print(isHappy(20))     