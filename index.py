records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Sarah", "Sales"),
    ("Pranjal", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing"),
    ("Charles", "Marketing"),
    ("Brian", "Marketing"),
    ("Jordan", "Marketing"),
]

# Proposed Dictionary
# Keys will be Departments
# values array of names, or list of names
def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record # e.g. ("Alice", "Engineering")

        # Check if department is already in index
        if dept in index:
        # if it is, add name to the list
            index[dept].append(name)
        else:
        # else create new key with list with the name in it
            index[dept] = [name]

    return index

department_index = build_index(records)

print(department_index)




# print all the departments
print(department_index.keys()) # dict_keys(['Engineering', 'Sales', 'Marketing'])

# # print everyone in Engineering:
print(department_index['Engineering']) # # ['Alice', 'Dave', 'Erin', 'Frank']

# # print everyone in Sales:  
print(department_index['Sales']) # ['Bob', 'Carol', 'Sarah', 'Pranjal']

# # print everyone in Marketing:
print(department_index['Marketing']) # ['Grace', 'Charles', 'Brian', 'Jordan']
