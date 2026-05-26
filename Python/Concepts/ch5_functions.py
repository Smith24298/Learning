# def my_function( arguments ):

# can use pass to create en empty function other wise it gives the error

# Arguments and Parameters

def my_function(fname): #here fname is the parameter
  print(fname + " Refsnes")

my_function("Emil") # here "Emil" is the argument

# we can give parameters default values
def my_function(fname, lname = "Refsnes"):
  print(fname + " " + lname)

my_function("Emil") 
# here "Emil" is the argument and lname takes the default value "Refsnes"



#  *args and **kwargs

"""
*args --> allow function to use multiple arguments can accees as the list
it only aalows the positional arguments


**kwargs --> allow function to use  mutltiple keyword arguments can access as the dictionary
it only allows the keyword arguments

def my_function(**args):
    print("args['fname']", args['lname'])

my_function(fname = "Emil", lname = "Refsnes")
"""


"""

we can use args and kwargs in the wise versa manner also 

"""
num1 = [1,2,3]
my_function(*num1) # it will unpack the list and pass the values as arguments to the function

dict1 = {"fname": "Emil", "lname": "Refsnes"}
my_function(**dict1) # it will unpack the dictionary and pass the values as keyword arguments







# GLobal and local Scope

def my_function():
    x = 300 # local variable
    print(x)
my_function()
print(x) # it will give an error because x is a local variable and cannot be accessed

def my_function():
    global x
    x = 300 # global variable
    print(x) # it will print 300 because x is a global variable and can be accessed
my_function()
print(x) # it will print 300 because x is a global variable and can be accessed


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 

"""

The LEGB Rule

Python follows the LEGB rule when looking up variable names, and searches for them in this order:

    Local - Inside the current function
    Enclosing - Inside enclosing functions (from inner to outer)
    Global - At the top level of the module
    Built-in - In Python's built-in namespace


"""



# Decorators

# A decorator is a function that takes another function as input and returns a new function.

"""
Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.
"""
#  custom decorator to change the case of the output of a function
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# this s decorator can access the arguments also
# @changecase(1)
"""
we can give multiple decorators to a function

the execution is from bottom to top that means which decorators is closer to the function will execute first
"""
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())


"""
Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

Normally, a function's name can be returned with the __name__ attribute:


"""

# But, when a function is decorated, the metadata of the original function is lost.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

"""
output :
myinner  --> Try returning the name from a decorated function and you will not get the same result:
"""
"""
To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
"""

# mport functools.wraps to preserve the original function name and docstring.
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)



# lambda functions
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is defined using the lambda keyword.


"""
Syntax
lambda arguments : expression 



"""

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5)) 


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)  # now this mydoubler is a function that takes one argument and multiplies it by 2 it is lambda fnction now

print(mydoubler(11))


doubled = list(map(lambda x: x*2 , map(int, input().split()))) # we can use lambda function or int at a time so like in the ca se of the user input we have to use another map to conver string into int then we can use lambda function to dounle the numbers and then we can convert the map object into list usig list() function



"""

Using Lambda with filter()

The filter() function creates a list of items for which a function returns True:
Example

Filter out odd numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

output:
[1, 3, 5, 7]


"""


"""
The sorted() function can use a lambda as a key for custom sorting:
Example

Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

output:
[('Tobias', 22), ('Emil', 25), ('Linus', 28)]

for string we ca use len(x[0]) insted of x[1] to sort by the length of the name instead of the age
"""

# Generator Expressonsions

"""
recursion is restart the function execution and the generator function pauses the function execution and return the value and can be resumed later on it saves the memory because it does not store the entire seqence in the memory it generates the values on the fly
"""

"""

Generators allow you to iterate over data without storing the entire dataset in memory.

Instead of using return, generators use the yield keyword.

The yield keyword is what makes a function a generator.

When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.

"""

# we can use next() function to get the nexr geneerated value from the generator and when the values are wxausted then it raise the error of StopIteration

"""
close() --> to stop the generator and raise the error of StopIteration
send() --> to send a value to the generator and it will be returned by the yield expression
throw() --> to raise an exception inside the generator
"""

