# Control flow(if,elif,else)

#Example 1:
x = 10 
if x > 0 :
    print("positive number")
elif x < 0:
    print("negative number")
else:
    print("zero")

#Example 2:(Checking Even or Odd)
num = 6
if num % 2 == 0:
    print("Even number")
else:
    print("odd number")

#Example 3: (Grading system)
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 2)loops(for loop and while loop)

#Example 1:
for i in range(5):
    print(i)

#Example 2:Iterating through a list
fruits = ["apple","cherry","banana"]
for fruit in fruits:
    print(fruits)

#Example 3:Printing multiple table
num = 5
for i in range(1,11):
    print(f"{num}*{i} = {num* i}")

#while loop
#Example 1
count = 0 
while count < 5:
    print(count)
    count += 1

#Example 2(countdown)
count = 5
while count > 0:
    print(count)
    count -= 1

#Example 3 (using break)
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

# 3) List 
#Example 1:
vegetables = ["potatoes","onion","brinjal"]
print(vegetables[1])
vegetables.append("ladyfinger") #adding an element
print(vegetables)

#Example 2:(list operation)
numbers = [1,2,3,4,5]
numbers.append(6)
numbers.remove(3)
numbers.reverse()
print(numbers)

#Example 3:(List Comprehension)
squares = [x ** 2 for x in range(1,6)]
print(squares)

# 4)Tuple
#Example 1:
colors = ("red","green","blue")
print(colors[0])

#Example 2:(Accessing Elements)
coordinates = (10,20,30)
print(coordinates[1])

#Examples 3:(Tuple Unpacking)
person = ("Alice","25","Engineer")
name ,age ,profession = person
print(name)
print(age)
print(profession)
print(person)

# 5) Dictionary
#Example 1:
person = {"name":"Habiba","age":"23","city":"karachi"}
print(person["name"])
print(person)

#Example 2:(Adding & Updating Elements)
student = {"name":"john","age":"20","course":"python"}
student["age"] = 21 # update age
student["Grade"] = "A" #Add a new key value pair
print(student)

#Example 3:(iterating through dictionary)
for key,value in student.items():
    print(f"{key}:{value}")

# 6)set(ordered & unique elements)
#Example 1 : set operation
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 | set2)  #union{1,2,3,4,5}
print(set1 & set2) # intersection: 3
print(set1 - set2) # difference:1,2

#Example 2:(Checking for an element)
numbers = {10,20,30}
print(20 in numbers)  #output true

#Example 3:
numbers = {1,2,3,4,4,5}
print(numbers)
numbers.add(6)
print(numbers)

# 7) Frozen set(immutable)
#Example 1:
frozen_numbers = frozenset([1,2,3,4])
print(frozen_numbers)

#Example 2:Creating a frozen set
frozen_nums = frozenset([1,2,3,4,5,6])
print(frozen_nums)

#Example 3: using frozen set in a dictionary key
data = {frozenset(["a","b","c","d"]):"letters"}
print(data)