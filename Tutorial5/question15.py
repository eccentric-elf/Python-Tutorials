import os
cwd = os.getcwd()
items = os.listdir(cwd)
print("Items in the Current Working Directory:")
for item in items:
    print(item)
