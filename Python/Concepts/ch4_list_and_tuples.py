list1 = [] #how u can define empty list
list2 = [1, 2, 3, 4, 5] #list of integers
list4 = ["apple", "banana", "cherry"] #list of strings
list5 = [1, "hello", 3.14, True] #list of mixed data types
list6 = [[1, 2], [3, 4], [5, 6]] #list of lists (nested list)

"""
can be mutable
can contain duplicate values
can contain different data types
can be indexed and sliced
can be modified (add, remove, change elements)
"""
list3 = list(range(1, 10)) #list of numbers from 1 to 9
"""

we can use built-in constractors like list() to create lists from other iterables (like strings, tuples, etc.)
we can use "in" operator to check if an element is in the list
"""
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(type(list1))
""""
same negative indexing and slicing as strings 
"""

#list methods

list1.append(10) #Add an element to the end of the list
list1.clear() #Remove all elements from the list
list1.count(10) #Return the number of occurrences of a specified element in the list
list1.extend([20, 30, 40]) #Add elements from another iterable (like a list) to the end of the list
list1.index(20) #Return the index of the first occurrence of a specified element in the list
list1.insert(1, 15) #Insert an element at a specified index in the list
list1.pop() #Remove and return the last element of the list (or an element at a specified index)
list1.remove(15) #Remove the first occurrence of a specified element from the list
list1.reverse() #Reverse the order of the elements in the list
list1.sort() #Sort the elements of the list in ascending order (or in a specified order)
list1.sort(reverse=True) #Sort the elements of the list in descending order

list1.copy() 
'''Return a shallow copy of the list (creates a new list with the same elements)
insted of this use list(list1) to create a copy of the list
'''





tuple1 = () #how u can define empty tuple
tuple2 = (1, 2, 3, 4, 5) #tuple of integers
tuple4 = ("apple", "banana", "cherry") #tuple of strings
tuple5 = (1, "hello", 3.14, True) #tuple of mixed data types
tuple6 = ((1, 2), (3, 4), (5, 6)) #tuple of tuples (nested tuple)
"""
can be immutable
can contain duplicate values
can contain different data types
can be indexed and sliced
cannot be modified (add, remove, change elements)
"""
tuple3 = tuple(range(1, 10)) #tuple of numbers from 1 to 9
"""
we can use built-in constractors like tuple() to create tuples from other iterables (like strings, lists, etc.)
we can use "in" operator to check if an element is in the tuple
"""
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
print(tuple6)
print(type(tuple1))
"""same negative indexing and slicing as lists 
""" 
# tuple methods
"""
Same as the List methods but without the ones that modify the tuple (like append, clear, extend, insert, pop, remove, reverse, sort)

to do all this method need to convert to list first and then perform the operation and then conver back into tuple

"""
tuple8 = (1,2,3,4,5,6,7,8,9)
# tuple8.append(10) #AttributeError: 'tuple' object has no attribute 'append'
# Wrong: list.reverse() returns None, so wrapping it causes a NoneType error.
# Correct way:
temp_list = list(tuple8)
temp_list.reverse()
tuple8 = tuple(temp_list)
print(tuple8)