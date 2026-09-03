# zip() combines items from multiple iterables
names = ["Asha", "Rahul", "Mira"]
marks = [80, 90, 85]

print("zip():")
for name, mark in zip(names, marks):
    print(name, mark)

# enumerate() gives index and value
print("\nenumerate():")
for index, name in enumerate(names):
    print(index, name)
