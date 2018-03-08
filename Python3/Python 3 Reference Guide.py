### Functions

## Default function arguments are defined only once
def fDefaultVal(a, L=[]):
    L.append(a)
    return L

#print(fDefaultVal(1))
#print(fDefaultVal(2))
#print(fDefaultVal(3))

# To prevent this, write the function like this:
def fDefaultVal2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

#print(fDefaultVal2(1))
#print(fDefaultVal2(2))
#print(fDefaultVal2(3))


## Keyword arguments
def fKeywordArgs(normArg, *arguments, **keywords):
    print("Normal Argument: ", normArg)
    print("-" * 25)
    print("Argument List:")
    for arg in arguments:
        print(arg)
    print("-" * 25)
    for kw in keywords:
        print(kw, ":", keywords[kw])

#fKeywordArgs("Hi", "Hello", "World", firstword = "Hej", secondword = "Hej")

## Unpacking Argument Lists

rangeNumbers = [1, 6]
list1 = list(range(*rangeNumbers)) # Equal to list(range(1, 6))
#print(list1)

## Lambda Functions
def callLambda(n):
    return lambda x: x + n

usesCallLambda = callLambda(5)
#print(usesCallLambda(0))
#print(usesCallLambda(5))

## 2 ways of documenting functions

# Doc string that is accessible by funcName.__doc__ and defined by """ blah """ right under def funcName():
def funcWithDocstring():
    """ I'm a docstring """
    pass
#print(funcWithDocstring.__doc__)

def funcWithAnnotations(string: str) -> str:
    print("Annotations: ", funcWithAnnotations.__annotations__)
    return string

#funcWithAnnotations("Hello")

### Lists

## List Comprehensions

# Can turn this:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

# Into this:
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# You can nest comprehensions too
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposedRowsAndColumns = [[row[i] for row in matrix] for i in range(4)]

### Classes

class Dog:
    tricks = [] # Class variable that is shared between ALL instances of the class (like static class variables in C#)

    def __init__(self, name):
        self.name = name # All class functions are given self automatically when invoked, and you use it to create instance variables

## Can add iterator behavior to your own classes:

# Manual way
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self # Can return any object that implements __next__()

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1;
        return self.data[self.index]

#rev = Reverse('spam')
#for char in rev:
#    print(char)

# Using Generators (the simpler, preferred way)
def reverse2(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index] # Regular functions that 'yield' are Generators (I.E. They save their last state so they can return the next item)

#for char in reverse2('spam'):
#    print(char)

## Generator Expressions (Like list comprehensions but use parentheses)
# Less versatile than full generators but more memory efficient than list comprehensions

#print(sum(i*i for i in range(10)))

