# this is a comment line
''' 
this is multi line comment 
'''
var = "this is a variable"
name = "azizul" # python variable can declare directly
print(name) # print is build in python code printer
print(type(name)) # type is build in keyword for check data type

# data type in py
#string #integer float list tuple boolean dictionary
string = "abc"
integer = 124
float = 12.21
listInPy =["index",'1 index']
tuple = (1,2,3,4)
print(type(tuple))
bool = True, False
dictionary = {
    "name" : "azizul",
    "age":12
    }

# if else statements
x = 10
if x < 20 : print("x is less than 2o")
else: print("x is greater than 20")

# loop in py (for loop)

alphabet = ['a',"b","c","e","f"]

for letter in alphabet : 
    print(letter,"single letter")

    # range loop
for number in range(0,100) :
    print(number)

#  while loop 
a = 0
while a < 100 :
    print(a,"while looop")
    a+=1

    #  function in py
#  to write a block of code
# that can be reuseable

def multipy(x,y) :
    return x * y

print(multipy(10,10))

# module 
# use for other's code in my code via module
from math import *
print(pi)

# tuple vs list 
# tupple is immutable
# list is mutable
tuple2 = (12,12,12)
print(tuple2[2])
#  but we can't change 
# tuple2[2]  = 99  give me error
print(tuple2[2])
  

#   list 
list2 = [12,12,12]
print(list2[2])  # output : 12
list2[2] = 99
print(list2[2]) # output: 99
