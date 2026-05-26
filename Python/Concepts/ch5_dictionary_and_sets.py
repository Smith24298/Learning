a={
    "name":"John",
    "age":30,
    "city":"New York"
}

"""
it is unordered collection of key-value pairs
it is mutable (can be changed after creation)
it does not allow duplicate keys (but can have duplicate values)
it is indexed by keys (not by position like lists and tuples)
it can be created using curly braces {} or the dict() constructor
"""

print(a)

a.items() #Return the tuple of keys present in the dictionary

a.keys() #Return the tuple of keys present in the dictionary

a.values() #Return the tuple of values present in the dictionary

a.update({"country":"USA"}) #Update the dictionary with the key-value pairs from another dictionary (or from an iterable of key-value pairs)

a.get("name","Default Value") #Return the value of a specified key in the dictionary (or a default value if the key is not found)

a.pop("age") #Remove and return the value of a specified key from the dictionary (or a default value if the key is not found)

a.clear() #Remove all key-value pairs from the dictionary
a.copy() #Return a shallow copy of the dictionary (creates a new dictionary with the same key-value pairs)
a.fromkeys(["name", "age"], "Unknown") #Create a new dictionary with specified keys and a default value
a.setdefault("name", "Unknown") #Return the value of a specified key in the dictionary (or set it to a default value if the key is not found)
a.popitem() #
"""

Remove and return an arbitrary key-value pair from the dictionary (raises KeyError if the dictionary is empty)

NOTE that the order of key-value pairs in a dictionary is not guaranteed to be the same as the order in which they were added (especially in older versions of Python), so the item returned by popitem() may not be the last item added to the dictionary.
"""






b= {"apple", "banana", "cherry"}

"""
it is an unordered collection of unique elements
it is mutable (can be changed after creation)
it does not allow duplicate values
it is not indexed (cannot be accessed by position like lists and tuples)
it can be created using curly braces {} or the set() constructor
"""

print(b)
b.add("orange") #Add an element to the set
b.remove("banana") #Remove a specified element from the set (raises KeyError if the element is not found)
b.discard("banana") #Remove a specified element from the set (does not raise an error if the element is not found)
b.pop() #Remove and return an arbitrary element from the set (raises KeyError if the set is empty)
b.clear() #Remove all elements from the set
b.copy() #Return a shallow copy of the set (creates a new set with the same elements)
b.union({"grape", "melon"}) #Return a new set that is the union of the set and another set (or iterable)
b.intersection({"grape", "melon"}) #Return a new set that is the intersection of the set and another set (or iterable)
b.difference({"grape", "melon"}) #Return a new set that is the difference of the set
# and another set (or iterable)
b.symmetric_difference({"grape", "melon"}) #Return a new set that is the symmetric difference of the set and another set (or iterable)
b.issubset({"grape", "melon"}) #Return True if the set is a subset of another set (or iterable)
b.issuperset({"grape", "melon"}) #Return True if the set is a superset of another set (or iterable)
b.isdisjoint({"grape", "melon"}) #Return True if the set has no elements in common with another set (or iterable)

frozenset1 = frozenset([1, 2, 3, 4, 5]) #frozenset of integers
frozenset2 = frozenset(["apple", "banana", "cherry"]) #frozenset of strings
frozenset3 = frozenset([1, "hello", 3.14, True]) #frozenset of mixed data types
"""
it is same as the set but it is immutable 
"""





