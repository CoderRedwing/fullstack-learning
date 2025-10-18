# string is data type that store a sequence of characters
"""
str2 = "dd"
str1 = "Mishra"

# various operation on strins like (len, concatinate, indexing, slicing)

# print(str2+" "+str1)
# print(len(str2), len(str1))

print(str2[0])  # indexing

print(str2[0:]) # slicing  [starting index, ending index]-> ending inedex not included it also supports negative indexing 
#str[2] = 'a'    TypeError: 'str' object does not support item assignment

# some string predefine functions 

str = "ajitesh"
"""

"""
endsWith("sh")-> returns true if string ends with substr

capitalize() -> Capitalizes 1st char


replace(old, new) -> replace all occurence of old with new

find(word) -> return first index of 1st occurence

count("ab") -> counts the occurence of substr in string


print(str.endswith("sh"))

print(str.capitalize())

print(str.replace("a","l"))

print(str.find("h"))

print(str.count("sh"))


"""

# problem 1 

name = input("Enter user first name: ")

print("the length of user first name is: ",len(name))

print(name.count("a"))


# conditional statements 

age = int(input("Enter the age of the user: "))

if(age>=18):
    print("User eligible for voting")

else:
    print("User not eligible for voting")


# problem grade system for students

marks = int(input("Enter the marks of the student: "))

if(marks>=90):
    print("Grade = A")
elif(90>marks>=80):
    print("Grade = B")
elif(80>marks>=70):
    print("Grade = C")
elif(marks<70):
    print("Grade = D")
else:
    print("Fail")


# poroblem number is odd or even

num = int(input("Enter a number: "))

if(num%2==0):
    print("Number is Even")
else:
    print("Number is Odd")


# gretest number between 3 num

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if(num1>num2 and num1>num3):                   # 7  9  2 10
    print("First number is grether", num1)
elif(num2> num3):
    print("Second number is grether", num2)
else:
    print("Third number is grether", num1)


num4 = int(input("Enter a number: "))

if(num%7==0):
    print("Number is Multiple of 7: ", num4)
else:
    print("Number is not Multiple of 7: ",num4)
