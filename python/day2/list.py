"""
List is a built in data type that store set of values 
it can store elements of diffrent type (int, float, string, etc)

"""

data = ["Name", 23, "adress", 34, 34.67]

print(data)

data[0] = "Aman"

print(data)

# we can also perfor slicing in list also

print(data[0:2]) 

list = [1,3,2]

# predefine methods in list 

"""
append(4) -> adds one element at the end [1,3,2,4]

sort() -> sort in ascending order [1,2,3]

sort(reverse=True) -> sorts in descending order

reverse()  reverse the list

insert(ind, el) -> insert element at index

remove(1) -> removes first occurence of element:  [1,2,3,1] it removes 1 at index 0

pop(ind) -> remove elements at particulaer index


mutation is allowed in list
"""

list.insert(1,4)
print(list)

list.reverse()

print(list)
