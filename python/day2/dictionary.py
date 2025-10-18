"""
dictionary are used to store the data in key value pairs 

they are unordered, mutable(changeable) & don't allow duplicate keys

"""

dict = {
    "name": "Aman",
    "age": 23,
    "dob": "20-07-2004",
    "subjects": ["python", "C", "java", "javascript"],
    "topic": ("dict", "set")
}

print(dict["subjects"][0])

data = {
    "students": [
        {"name": "Ajitesh", "age": 22, "subjects": ["Maths", "Science"]},
        {"name": "Riya", "age": 21, "subjects": ["English", "History"]},
        {"name": "Karan", "age": 23, "subjects": ["Physics", "Chemistry"]}
    ]
}


for student in data["students"]:
    print(f"{student['name']} - {student['age']}")


# nested dictionary 

student1 = {
    "name": "Aman",
    "score": {
        "math": 89,
        "phy": 90,
        "che": 91
    }
}

print(student1["score"]["math"])

"""
predefine methods of dictionary 

.keys() -> return all keys of dict

.values() -> returm all values of dict

.items() -> return all (key, val) pairs as tuple

.get("key") -> returns the key accordings to value 

.update(newDict) -> insert the specified item to the dict

"""


student2 = {
    "name": "Aman Mishra",
    "age": 23,
    "score": {
        "math": 89,
        "phy": 90,
        "che": 91
    },
    "Grade": "A"
}

student1.update(student2)

print(student1.items())


