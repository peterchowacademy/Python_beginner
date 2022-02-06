from fruit_original import fruit_original

# fruit_original.instantiate_from_csv() #this is the argument pass to the classmethod, iterite as a list of dictionary


#object:
fruit1 = fruit_original("Frusdfsdfsdfsdfsdfsdit", 25, 30)
fruit1.apply_increment(0.2)
print(fruit1.price)
print(fruit1.send_email())
# fruit2 = fruit_item("bannanannaana", 23, 15, 3)


# print(fruit_price.payrate) # return the value of the class attributes
# print(fruit_price.__dict__) # return all attributes on class level
# print(fruit1.__dict__) #return all attributes on instance level

# #apply the  global attribute to the class
# fruit1.apply_discount()
# print(fruit1.price)
#
# #apply the attribute to the instance only
# fruit2.payrate = 0.6
# fruit2.apply_discount()
# print(fruit2.price)


# for instance in fruit_price.all:
#     print(instance.fruit)

# print(fruit_price.all) #a more meaningful representative is given by __repr__ function