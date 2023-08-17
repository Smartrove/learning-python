
# print(2 + 5)
# if(5 > 2):
#     print("Five is greater than two")

# x = str(3)
# print(type (x))

# name = "Shade"
# lowerCaseName = name.lower()
# print(lowerCaseName)


# x, y, z = "Banana", "Pawpaw", "Orange"
# print(x, y, z)

# x = y = z = 2
# print(x)


#unpacking

# fruits = ["cashew", "apple", "melon"]
# x,y,z = fruits
# print(x,y,z)

# x = 5
# y = "Ade"
# print(x + y)
# x = 5
# y = "Ade"
# print(x,y)

#global variables

# x = "Ade"

# def fullName():
#     print("My name is Shola" + " " +  x)

# fullName()

# import random

# print(random.randrange(1, 10))

#multi line string
# a = """
# lorem ipsum,
# lorem ipsum dolor sit amet,
# lorem ipsum dolor sit amet sed diam,
# """

# print(a)

# string are array
# a = "Hello world"
# print(a[7])
# print(len(a))

# for x in a :
#     print(x.upper())

# check for a phrase in a string
# phrase = "the brown big fox"
# extractedString = "brown" in phrase

# if(extractedString):
#     upperPhrase = phrase.upper()
#     print(upperPhrase)

# slice a string
# x = "big brown fox"
# sliceX = x[4:9]  # get a part of the string
# sliceX = x[:9]   #get the slice from the beginning
# sliceX = x[10:]   #get the slice to the end
# sliceX = x[10:-1]   #get slice using negative value to start from the end of the string
# sliceX = x[-13:-1]   #get slice using negative value
# print(sliceX)

# remove white space from a string
# y = " Hi "
# y = " Hi Python"
# whiteSpaceRemoved = y.strip()
# print(whiteSpaceRemoved)

# replace a character in a string

# stringReplaced = y.replace("i", "ello")
# print(stringReplaced)


# the split method 


# splitString = y.strip().split(" ")

# print(splitString)

# using the format method on a string

# age = 28
# details = "My name is John Doe, I am {} years old."
# fullDetails = details.format(age)
# print(fullDetails)

# firstName = "Ibrahim"
# lastName = "Zayd"
# age = 28
# institution = "Unilag"
# description = "My name is {} {},  I am {} years old. I am a student of {}."
# fullDescription = description.format(firstName, lastName, age, institution)
# print(fullDescription)


# escape character
# items = "these are \"food\" items"
# print(items)

# String Method
# capitalize
# address = "moloney junction"
# capitalizedAddress = address.capitalize()
# countAddress = address.count('j')
# print(capitalizedAddress, countAddress)

# find method
# y = 'Moloney'
# findY = y.find('y')
# print(findY)

# endswith method
# rate = "This is a high rate"
# if(rate.endswith('b')):
#     print('This is a low rate')
# print('This is a high rate')

# not

ageShola = 89
ageShade = 30

if(ageShola != ageShade):
    print('Shade is younger than Shola')
else:
    print('This is an old man')