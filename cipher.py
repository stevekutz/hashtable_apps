# Substitution Ciphers
# Or how to transform data from one thing to another


### important concept is here is >> How to use hashtables to map one data type to another(e.g. wesite state dropdown maps to state's abbreviation)
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

### CREATE decode_table
# we are basically swapping keys <--> values
decode_table = {}

###### ANOTHER way
# #### SWAP   key & value 
# # A dict comprehension to swap k & v
decode_table = {v: k for k,v in encode_table.items()}

### Iterate through encode table and build decode by assigning key>> value and assigned value>> key
# for key, value in encode_table.items():
#     decode_table[value] = key    

# print(decode_table)


# iterate through and build up string using encode table
def encode(plain_text):
     cipher = ""

     for char in plain_text:
          if char.isspace():# if space, returns True
               cipher += ' ' # pad cipher with space
          else:
               cipher += encode_table[char.upper()] # assign encode value to stored key for char

     return cipher



# iterate through and build up string from decode_table
def decode(cipher_text):
     plain_text = ''
     for char in cipher_text:
          if char.isspace():
               plain_text += ' '
          else:
               plain_text += decode_table[char.upper()]
     return plain_text


cipher = encode("Dictionaries are awesome")
print(f' cipher is : {cipher}')

reversed_plain_text = decode(cipher)
print(f' decoded is: {reversed_plain_text}')