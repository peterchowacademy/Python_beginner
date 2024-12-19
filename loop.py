a =[0,1,2,3]
for element in a:
    if not element:
        continue
    print(f"continue {element}") #will not print after continue

for element in a:
    if not element:
        pass
    print(f"pass {element}") #will print after pass

for element in a:
    if not element:
        break
    print(f"break {element}")