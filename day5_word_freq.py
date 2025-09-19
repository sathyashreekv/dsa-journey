name="Sathyashree"
my_dict={}
for char in name:
    if char not in my_dict:
        my_dict[char]=my_dict.get(char,0)+1
    else:
        my_dict[char]+=1
print(my_dict)