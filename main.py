import math
import string

x = 5 #int
temp = 36.89 #float
isPresent = True #boolean
name = "harol" #string
grades = [90,80,70] #arrays
record = ("harol","rojas",29,True) #tuple
y,z = (6,7) #tuple with unpacking
colors = {"red","blue","green"} #sets
user = {
    "name": "harol",
    "age": 29,
    "is_admin": True
}

def listMethods():
    print(
        grades[1:3], #slicing
        grades.append(100),
        grades.pop(),
        grades.remove(80),
        grades.clear(),
        grades.sort(),
        grades.reverse()
    )


# creating a new string with the next following charcter from another tring
def messingWithStrings(valString: string) -> string:
    changed = ""
    for i in range(len(valString)):
        changed += chr(ord(valString[i]) + 1)
    return changed

def loopingList(listVal: list):
    for i in listVal:
        print(i)

def whatever():
    for i in range(10):
        if 5 > i > 2:
            continue
        print(i)


def isEven(n):
    return n % 2 == 0


def test_func():
    print(x, y, z)
    print(type(temp))
    print(name + "\n" + str(temp))
    print(name[3])

def hyp(a,b):
    return math.sqrt(a**2 + b**2)


class Person:
    def __init__(self, first_name: str, last_name: str, age: int, is_employed: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_employed = is_employed

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age}, {'Employed' if self.is_employed else 'Unemployed'})"

# Create Person objects
person1 = Person("John", "Doe", 25, True)
person2 = Person("Jane", "Smith", 17, False)
person3 = Person("Alice", "Johnson", 30, True)

if __name__ == '__main__':
    test_func()
    print(hyp(3, 4))
    print(isEven(5))
    print(type(isPresent))
    print(messingWithStrings(valString="hello"))
    print(len(name))
    print(user["name"])
    loopingList(grades)

    # Print details of Person objects
    print(person1.full_name(), person1.is_adult())
    print(person2.full_name(), person2.is_adult())
    print(person3.full_name(), person3.is_adult())
