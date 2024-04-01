# Loops

condition = True
while condition == True:
    print("The condition is True")
    condition = False


count = 0
while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range (15):
    print(item)


items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(item)

#Break and Continue
items = [1,2,3,4]
for item in items:
    if item ==2:
        continue
    print(item) # 1 3 4

items = [1,2,3,4]
for item in items:
    if item ==2:
        break
    print(item) # 1
