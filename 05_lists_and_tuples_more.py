# List (Mutable)
my_list = ["Apple", "Banana", "Cherry"]
my_list.append("Mango")
print("List:", my_list)

# Tuple (Immutable)
my_tuple = (10, 20, 30)
prfruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
popped_item = fruits.pop()
print("List:", fruits)
print("Length:", len(fruits))

colors = ("red", "green", "blue", "red")
print("Tuple:", colors)
print("Count:", colors.count("red"))
print("Index:", colors.index("blue"))
# dict
student = {"name": "Gyan", "age": 21, "course": "B.Tech CSE"}
print("Name:", student["name"])
student["age"] = 22
student["city"] = "Jabalpur"
student.pop("course")
print("Keys:", student.keys())
print("Values:", student.values())
# sets
set_a = {1, 2, 3, 4, 4, 5}
set_b = {4, 5, 6, 7}
print("Set A:", set_a)
set_a.add(10)
set_a.remove(2)
print("Modified Set A:", set_a)
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))int("Tuple:", my_tuple)
