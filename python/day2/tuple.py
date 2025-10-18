"""
Tuples in python: A built in data type that lets us create immutable sequences of values.

tup = (2,3,45,6) -> tup[0], tup[1]

tup[0]=42  -> Not allowed in python gives error

"""

tup = (1,2,3,1,1)

print(type(tup), tup)

tup1 = (1)  # -> python treats as an integer
tup2 = (1,) # -> ryt way to assign single value on touple

# methods in tuple:  index() -> return index of first occurence 
#  count(el) -> count total occurence

print(tup.index(3))

print(tup.count(1))


# problem 1
l = []
movie = input("Enter first movie name: ")
l.append(movie)
movie = input("Enter second movie name: ")
l.append(movie)
movie = input("Enter third movie name: ")
l.append(movie)

print(l)

# prob 2

a = [1,2,1,2]
b = a.copy()
a.reverse()

if(a==b):
    print("Yes")
else:
    print("No")

# problem 3 



t = ("C", "D", "D", "A", "A", "B", "B", "A")

print(t.count("A"))

c = ["C", "D", "D", "A", "A", "B", "B", "A"]

c.sort()

print(c)