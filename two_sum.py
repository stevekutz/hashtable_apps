# return indices of numbers in num_list that add up to a specific target

num_list = [3, 2, 7, 11, 15, -6, -2]
index_dict = {}
index_list= []
target = 9

def two_sum(num_list, target):

     for i in range(len(num_list)):
          current = num_list[i]
          complement = target - current
          if complement in index_dict:
               # return [index_dict[complement], i]
               index_list.append([index_dict[complement], i])
          else:
               index_dict[current] = i    
     return index_list

print(two_sum(num_list, target))               