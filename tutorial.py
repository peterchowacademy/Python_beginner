'''
### String Method ###
course = 'Python for beginner'
## to replace the string with anther in 'replace' method
print(course.replace("Python", "Djgon"))
## to find the index of the string in the string 'find' method
print(course.find("for"))
## return 'True' or 'False' from the string by 'in' method
print('Python' in course)


### other string methods ###
print(course.title())
print(course.upper())
print(course.lower())
print(course.find("for"))
print(course.replace("beginner", "experienced user"))


##algorithm in python ###
print(10 % 3)
print(10 % 2)
print(10 ** 4 )
x = 3
x -= 4
print(x)




##Math Function - import math module ###
import math
x = -2.9
print(abs(x))
print(math.ceil(3.4))
print(math.fmod(4.6, 5.8))
print(math.fabs(-5.656))



##If statement##
house_price = 1000000
good_credit = True
if good_credit:
    down_payment = int(house_price * 0.1)
else:
    down_payment = int(house_price * 0.2)
print(f"you need to pay $ {down_payment} ")

##comparison operators##
name = input("enter your name ")
if len(name) < 3:
    print("Name must be 3 characters or above")
elif len(name) > 50:
    print("Name must be less than 50 characters")
else:
    print(f"Your name {name} look good")


###while loop###
i = 1
while i <=5:
    print('B' * i)
    i += 1
print("Done")


##for loop - like a iritation in the string##
for item in "python":
    print(item)
for item in ['Mosh', 'John', 'April', 'Kevin']:
    print(item)
for item in (0,1,3,4):
    print(item)
for item in range(0,9,2):
    print(item)

price = [10,20,30]
sum = 0
for i in price:
    sum += i 
print(f"final price of the price items are {sum}")

###nest loop challenge ### 
number = [5,2,5,2,2]
for xcount in number:
    output = ''
    for count in range(xcount):
        output += 'x '
    print(output)
'''

###list - find the largest number from the list ###
number = [9,10,12,4,23,51,2,7]
max = number[0]
for i in number:
    if i > max:
        max = i
print(max)

###list - find the lowest number from the list ###
list = [-1, 5, 45, 10, 0, 1]
min = list[0]
for i in list:
    if i < min:
        min = i
print(min)

## 2D List ##

