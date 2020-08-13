J = "aA"
# J = "aAb"
# J = "z"

print(list(J))  # ['a', 'A']
dict = {}

S = "aAAbbbb"
total = 0

for ch in S:
     if ch in J:
          # if ch not in dict:
          #      dict[ch] = 1
          # else:
          #      dict[ch] += 1     
          total += 1     

# for v in dict.values():
#      total += v


for ch in S:
     if ch in J:   
          total += 1  

print(dict)
print(total)

for v in dict.values():
     total += v