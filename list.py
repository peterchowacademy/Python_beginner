a = [5, 2, 9, 1, 5, 6]

# Sort the value in increasing order
# a.sort()
# print(a[-1])


list = [6, 6, 5, 3, 2]
a = set(list)



score = [2, 3, 6, 6, 5, 12, 10, 10] #list
score2 = set(score) #convert list to set >> remove duplicate
print(f"set is {score2}")ß
score3 = sorted(score2, reverse=True) #sorted() >> sequence from small to big  #convert set to list
print(f"new sorted list is {score3}")
print(f"runner-up score is {score3[1]}")

