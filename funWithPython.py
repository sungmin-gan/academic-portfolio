#2 Boolean Expressions
print("\n#2 Boolean Expressions\n")
true = True
false = False
if true == True:
  print("'true' is True!")
if false != True:
  print("'false' is False!")

#3 Short Circuit Evaluation
print("\n#3 Short Circuit Evaluation\n")
def true():
  print("I'm in true!")
  return True
def false():
  print("I'm in false!")
  return False

print("OR")
if true() or false():
  print("false should not execute")
print("\nAND")

if false() and true():
  print("Nothing will print :(")

#4 Numerical Types
print("\n#4 Numerical Types\n")
print(int(4.568))
print((1+2j)+(1+2j))

#5 Strings
print("\n#5 Strings\n")
hello = "Hello"
test = 'Does This Work?'
print(hello.replace("He","'E") + ", " + test.lower())
response = "Yes it does!"
print(response[0:3]+"!")

#6 Arrays
print("\n#6 Arrays\n")
array = [1,2,0,5,4,3]
array.sort()
array.append('A')
array.append('B')
array.append('C')
for x in array:
  print(x)
print("The letter 'A' appears ", array.count('A'), " time(s) in 'array'.")

#7 Lists
print("\n#7 Lists\n")
languagesMastered = ["Python","Java","C++"]
if "HTML" in languagesMastered:
  print("This is a candidate.")
else:
  print("Not qualified.")
languagesMasteredUpdated = languagesMastered.copy()
languagesMasteredUpdated.append("Swift")
print(languagesMasteredUpdated)

#8 Tuples
print("\n#8 Tuples\n")
testTuple = ("apples","bananas", "cherries", "bananas")
if testTuple.count("bananas") > 0:
  print("There are multiple instances of 'bananas' in 'testTuple'.")

#9 Slices
print("\n#9 Slices\n")
newArray = [0,1,2,3,4,5,6]
newSlice = slice(0,7,2)
print(newArray[newSlice])

#10 Index Range Checking & #1 Interpretation
print("\n#10 Index Range Checking & #1 Interpretation\n")
newList = [0,1,2,3,4,5]
#print(newList[7])
#Above line throws 'IndexError: list index out of range'
#for x in range(7):
#  print(newList[x])
#Interestingly, the above two lines of code output the numbers 0-5, or newList[0] to newList[6] but throws an 'IndexError: list index out of range' once it reaches newList[7]
#This shows how Python is an interpreted languages, meaning the lines of code are execuited dynamically

#11 Dictionaries
print("\n#11 Dictionaries\n")
car = {"Make": "Porsche",
        "Model": "Carrera",
        "Year": 1997}

print("Make: ", car["Make"])
print("Model: ", car.get("Model"))
car["Year"] = 1998
print("Year:", car["Year"],"\n")

for x in car:
  print(x,": ", car[x])
print("\n")

for x,y in car.items():
  print(x,": ",y)
print("\n")

for x in car.values():
  print(x)
print("\n")

if "VIN" in car:
  print("The VIN is a key in this dictionary")
else:
  print("The VIN is not a key in this dictionary")
car["VIN"] = 1234
car["Registered"] = True
print(car)

car.pop("VIN")
del car["Registered"]
print(car)
car.popitem()
print(car)

#12 If Statement
print("\n#12 If Statement\n")
usingPython = "Fun"
if usingPython == "Fun":
  print("Python is indeed very fun.")
elif usingPython == "Easy":
  print("Yes, Python is very easy.")
else:
  print("To you, Python is " + usingPython + ".")

#13 Switch Statement
print("\n#13 Switch Statement\n")
#Switch statements do not exist in Python
#However, an equivalent can be implemented using
#a dictionary:
def intToMonth(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(argument, "Invalid Month")
print(intToMonth(4))
print(intToMonth(13))
#This implementation even returns a default statement if an inappropriate input is given.
#An explicit switch statement probably wasn't implemented in Python because a dictionary basically acts as a switch statement, or vice versa.

#14 For Loop
print("\n#14 For Loop\n")
list = [0,1,2,3,4,5]
for x in list:
  print(x)
  if x == 3:
    break
print("\n")

for x in list:
  if x == 3:
    break
  print(x)
print("\n")

for x in list:
  if x == 3:
    continue
  print(x)
else:
  print("Loop Ended")

#15 While Loop
print("\n#15 While Loop")
capacity = 5
while capacity > 0:
  capacity -= 1
  if capacity == 3:
    continue
  print(capacity)

#16 Indentation to Denote Code Blocks
#Indentation in Python is extremely important as they serve as the equivalent of curly brackets in other languages such as C++

#17 Type Binding
#Python uses dynamic type binding, as this is an interpreted language and not a compiled language. This makes it so much easier to write generic programs that otherwise would take much more time to write in compiled languages. The main disadvantage of this; however, is that it lacks the level of protection from errors that static type binding can offer. 

#18 Type Checking
print("\n#18 Type Checking\n")
# For a long time, static type checking did not exist in Python. As mentioned in the previous section, this made programs written in Python more prone to errors. However, in Python 3.6, we can now declare variable types like so:

name: str = "Sung"

#So if I try to do something like:

def helloName(name:str) -> str:
  print("Hello, " + name)
# with helloName(7),
#Python will throw "TypeError: must be str, not int"
#P.S. the -> str after the function name and parameters declares the return type of the function
helloName("Sung")

#19 Functions
print("\n#19 Functions\n")

def printCountry(country = "the USA"):
  print("I am from " + country, "\n")
printCountry("France")

fruits = ["apples", "bananas", "cherries"]
def printGroceryList(category):
  for x in category:
    print(x)
printGroceryList(fruits)

def factorial(k):
  if k > 1:
    result = k * factorial(k-1)
  else:
    result = 1
  return result

print(factorial(5))

#20 Enumerations
print("\n#20 Enumerations\n")
#Enumerations were implemented in Python v3.4
#It is implemented as a class with several member functions; however, here we will only the most basic enumeration nomenclature and member functions:

from enum import Enum
class Color(Enum):
  RED = 1
  BLUE = 2
  GREEN = 3

#Enum members are iterable, in defition order:
for color in Color:
  print(color)

#Enum members are hashable, and can be used in dictionaries:
popsicles = {}
popsicles[Color.RED] = "Tart Cherry"
popsicles[Color.BLUE] = "Sweet Blueberry"
popsicles[Color.GREEN] = "Sour Apple" 
for x,y in popsicles.items():
  print(x,": ",y)
print("\n")
