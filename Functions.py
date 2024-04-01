# Functions


def hello(name):
    print("Hello " + name)


hello("Ali")
hello("Yunus")

#if we want that hello() is also work we mast write:
def hello(name = "my friend"):
    print("Hi " + name)
hello("Ali")
hello() #Hi my friend

def hello(name, age):
    print("Hello " + name + ", you are " + str(age)+ " years old!")
hello("Ali", 18)

def change(value):
    value = 2

val = 1
change(val)
print(val)

def change(value):
    value["name"] = "Ali"

val = {"name": "Yunus"}
change(val)
print(val)
