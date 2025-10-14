import random

a = {"a", 1}
type(a)

id(a)

# These do nothing as add is a mutating function
a.add(True)
b = a.add(True)
type(b)

# Hasherror unhashable type: 'list'
a.add([1])

# what we use hash for:
# check sums
# digests

# sets use hash to check for membership
# sets of combined integers and bools can get very confusing
# its good practice to not mix bools and ints in coding, because True == 1 and False == 0
isinstance(True, int)  #returns True
isinstance(False, int) #returns True

# 
hash("hello") #original hash
hash("hello!") #different hash
hash("hello")  #same as first hash
hash("Hello")  #different hash
hash("hello ") #different hash

# hashing the same value will always return the same hash value
# hashing a value in one session may not return the same hash value in another session
# hash values are not guaranteed to be consistent across different versions of Python
# hash values are not guaranteed to be consistent across different machines
# hash is a one way function, you cannot get the original value back from the hash
# hash values are not unique, different values can have the same hash value (collision)

def alphabetaHash(string):
    return str.lower()[0]

alphabetaHash("apple")      #returns 'a'
alphabetaHash("Apple")      #returns 'a'
alphabetaHash("banana")     #returns 'b'
alphabetaHash("Banana")     #returns 'b'
alphabetaHash("cherry")     #returns 'c'
alphabetaHash("Cherry")     #returns 'c'

alphabetaHash([123])    #returns error, unhashable type: 'list'
alphabetaHash((123,))   #returns 123
alphabetaHash((True,))  #returns True
alphabetaHash((1,))     #returns 1

#dictionaries are mapping types
#dictionaries are mutable
#dictionaries are unordered
#dictionaries are indexed by keys
#dictionaries are defined by curly braces {}
#dictionaries are collections of key-value pairs
#keys must be unique and immutable (hashable)
#values can be of any type and can be duplicated
# allow us to have a consistent association between a key and a value
# allow us to look up a value by its key

driversToVehicles = {
    "nick":"ram,",
    "matt":"tacoma"
}

driversToVehicles["nick"]  #returns 'ram'
driversToVehicles["matt"]  #returns 'tacoma'
driversToVehicles["john"]  #returns KeyError: 'john'
"nick" in driversToVehicles  #returns True
"john" in driversToVehicles  #returns False
"ram" in driversToVehicles.values()  #returns True
"tacoma" in driversToVehicles.values()  #returns True
"ford" in driversToVehicles.values()    #returns False

driversToVehicles["john"] = "ford"  #adds key-value pair to dictionary

dot= {
    "cx": 100,
    "cy": 200,
    "r": 50,
    "color": "red"
}
dot["cx"]  #returns 100
dot["cy"]  #returns 200
dot["r"]   #returns 50
dot["color"]  #returns 'red'
dot["border"] = "black"  #adds key-value pair to dictionary
dot["cx"] = 150  #updates value of key 'cx' to 150
locals()["dot"]  #returns the entire dictionary
dot.get("cx")  #returns 150

students = ("bushra", 
            "nick", 
            "matt", 
            "tom", 
            "renny", 
            "max", 
            "vicky", 
            "lane", 
            "samuel", 
            "vani"
)

len(students)  #returns 10
random.shuffle(students) #returns None, shuffles the tuple in place
target = "vicky"
count = 0
for student in students:
    count += 1
    print(student)
    if student == target:
        print(f"Found {target} after {count} iterations")
        break
else: #no break
    print(f"{target} not found in list")

# best case vicky is first, 1 iteration
# worst case vicky is last, 10 iterations
# average case vicky is in the middle, 5 iterations
# O(n) linear time complexity, n is the number of students  

def findDuplicateStudentsList(students):
    seen =[]
    duplicates = []
    for student in students:
        if student in seen:
            duplicates.append(student)
        else:
            seen.append(student)
    return duplicates

findDuplicateStudentsList(students)  #returns list[]
students = students + ("vicky", "matt", "nick")
findDuplicateStudentsList(students)  #returns ['vicky', 'matt', 'nick']
# O(n^2) quadratic time complexity, n is the number of students

def findDuplicateStudentsSet(students):
    seen = set()
    duplicates = set()
    for student in students:
        if student in seen:
            duplicates.add(student)
        else:
            seen.add(student)
    return list(duplicates)

findDuplicateStudentsSet(students)  #returns ['vicky', 'matt', 'nick']
# O(n) linear time complexity, n is the number of students
# sets are implemented as hash tables, so membership checks are O(1) on average
# lists are implemented as arrays, so membership checks are O(n) on average

def containsDuplicateStudents(students):
    for i, a in enumerate(students):
        for j, b in enumerate(students):
            if i != j and a == b:
                return True
    return False

containsDuplicateStudents(students)  #returns True
# O(n^2) quadratic time complexity, n is the number of students
# nested loops, each loop iterates over n students, so n * n = n^

def containsDuplicateStudentsExample(students):
    buckets = {}
    for student in students:
        bucket_key = alphabetaHash(student)
        if bucket_key in buckets:
            return True
        buckets[bucket_key] = student
    return False

containsDuplicateStudentsExample(students)  #returns True
# O(n) linear time complexity, n is the number of students
# using a dictionary to store seen students, so membership checks are O(1) on average

