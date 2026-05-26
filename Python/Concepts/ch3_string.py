from sqlite3 import Date


x="smith faldu"

print(x.capitalize()) #Capitlize the first letter of the string
print(x.upper()) #Convert the string to uppercase
print(x.lower()) #Convert the string to lowercase
print(x.title()) #Capitalize the first letter of each word in the string
print(x.swapcase()) #Swap the case of each letter in the string
print(x.center(20)) #Center the string within a specified width
print(x.ljust(20)) #Left justify the string within a specified width
print(x.rjust(20)) #Right justify the string within a specified width
print(x.strip()) #Remove leading and trailing whitespace from the string
print(x.replace("smith", "john")) #Replace a specified substring with another substring
print(x.split()) #Split the string into a list of substrings based on whitespace
print(x.split("a")) #Split the string into a list of substrings based on a specified delimiter
print(x.join(["hello", "world"])) #Join a list of strings into a single string using a specified separator
print(x.find("faldu")) #Find the index of the first occurrence of a specified substring in the string
print(x.count("a")) #Count the number of occurrences of a specified substring in the string
print(x.startswith("s")) #Check if the string starts with a specified substring
print(x.endswith("u")) #Check if the string ends with


letters = f"Dear {x},\nYou are invited to the party on Saturday.\n {Date.today().strftime("%B %d, %Y")}"
print(letters)