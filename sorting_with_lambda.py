
###########################
# a lambda in Python is just an anonymous function that has one or more arguments, but only one expression.
###########################
# Syntax:
# lambda arguments : expression
# Example
add_ten = lambda a : a + 10
print(type(add_ten))
# Prints <class 'function'>
print(add_ten(5))
# Prints 15


my_list = [1, 8, 5, 2]
sort_list = lambda x : sorted(x)
result = sort_list(my_list)

my_list.sort()
print(my_list)  # [1, 2, 5, 8]
print(result)   # [1, 2, 5, 8]


def daily_activity(order, day, activity):
         return {'order': order, 'day': day, 'activity': activity}

mon_activity = daily_activity(0, 'Mon', 'Baseball')
tue_activity = daily_activity(1, 'Tue', 'Swim')
wed_activity = daily_activity(2, 'Wed', 'Soccer')
thu_activity0 = daily_activity(3, 'Thu', 'Basketball')
thu_activity1 = daily_activity(4, 'Thu', 'Dance')
thu_activity2 = daily_activity(5, 'Thu', 'Football')
activities = [mon_activity, tue_activity, wed_activity, thu_activity0, thu_activity1, thu_activity2]

# print(activities)  # prints in one wrapable row
def print_nice(val):
     for item in val:
          print(item)


# to sort by a key value
sorted_activities = sorted(activities, key= lambda x : x['order'], reverse = True)
print(f' sort by activities')
print_nice(sorted_activities)

print(f' original')
print_nice(activities)


#  to sort by more than one Key
sorted_activities2 = sorted(activities, key = lambda x  : (x['order'], x['activity']), reverse = True  )
print(f" sort by \'order\' and then by \'activity\'  ")
print_nice(sorted_activities2)


# the itemgetter function cna be used to represent the sequence of keys
from operator import itemgetter

sorted_activities3 = sorted(activities, key = itemgetter('day', 'activity'), reverse = True)
print(f" sort by \'day\' and then by \'activity\'  ")
print_nice(sorted_activities3)


# we can use a function to define the key as well
def sort_keys(day):
     return (day['day'])

sorted_activities4 = sorted(activities, key = sort_keys)
print(f"sorted by \'day\'")
print_nice(sorted_activities4)
