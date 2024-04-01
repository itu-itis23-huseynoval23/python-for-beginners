dogs = ["Ali", 1, "Yunus", True, "Fatih", "Orcun"]

print("Ali" in dogs)  # we can define 0 lists
print(dogs[2])  # Yunus
#if we want to change 
dogs[2]= "Yunus Korkmaz"
print(dogs)

print(dogs[2:])

dogs.append("Ekber")
print(dogs)# this code add Ekber to the list

dogs.extend(["Fatih"])
print(dogs)

dogs.insert(2, "Test")# add Test among 1 and Yunus
print(dogs)

dogs[1:1] = ["Test1", "Test2"] # add names to the list
print(dogs)


items= ["Ali", "Yunus", "Fatih", "Orcun", "ekber"]

itemscopy = items[:]
print(itemscopy)

print(sorted(items, key = str.lower))

#OR

items.sort()
print(items) #This numerate lists for upper and alphapetic
# But we see that ekber is fully lower and this will be auto last word

#if we want to fix that
items.sort(key = str.lower)
print(items)