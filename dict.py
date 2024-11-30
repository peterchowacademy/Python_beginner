d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Dictionary =")
print(d)
del(d[1]) 
print("Data after deletion Dictionary=")
print(d)

# print(d.has_key(2))
print(d.__contains__(2))