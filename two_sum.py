# return indices of numbers in num_list that add up to a specific target

num_list = [3, 2, 7, 11, 15, -6, -2]
#9 - elem >[6, 7, 2, -2, -4,  3, 11 ]    
index_dict = {}
index_list= []
target = 9


# find complement
# verify if in dictionary, if Y, then complement adn current = target
# otherwise, store complement value in case some other current matches with it to = target

def two_sum(num_list, target):

     for i in range(len(num_list)):
          current = num_list[i]
          complement = target - current # current + complement = target
          if complement in index_dict:  
               # return [index_dict[complement], i]
               # add arr of indices of complement and current value in num_list
               index_list.append([i, index_dict[complement]])
               # returns as [[2, 1], [5, 4], [6, 3]]
               
               ### index_list.append([index_dict[complement], i])  # current + complement = target
               # returns as # [[1, 2], [4, 5], [3, 6]]
          else:
               index_dict[current] = i    
     return index_list

print(two_sum(num_list, target))    # [[1, 2], [4, 5], [3, 6]]            