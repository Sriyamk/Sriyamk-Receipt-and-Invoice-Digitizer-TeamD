a = ["S", "for", "Sriya"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a list of tuples
print(list(enumerate(a)))

fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(index, value)


#isinstance
x = 10
print(isinstance(x, str)) #10 is not a string, returns False
y= "Hello"
print(isinstance(y,str)) #y is a strigng

#issubclass
class animal:
    pass
class dog(animal):
    pass
print(issubclass(dog, animal))

#testing enumerate
K = "bobby", "sally", "josh"
for i, name in enumerate(K):
    print(i,name)
    

# delattr
class student:
    name = "Sriya"
    age = 20
delattr(student,"name")

#purposefully trying to access the deleted attribute to show that it has been removed
try:
    print(student.name)
except AttributeError:
    print("The attribute 'name' has been deleted.")
