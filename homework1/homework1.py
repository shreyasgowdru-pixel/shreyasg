# File: homework1.py

# ---  VARIABLES AND DATA TYPES
a = 10
print(a)
print(type(a)) # a is an integer, whole number without decimals

b = 1.5
print(b)
print(type(b)) # b is a float, number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, used in advanced math/science (like vector??)

d = "hello"
print(d)
print(type(d)) # d is a string, sequence of characters (text) that can be changed

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, collection of ordered items that can be modified

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, collection of key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is tuple, collection of immutable (cannot be modified after making) ordered items

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, collection of ordered items that can be modified

i = True
print(i)
print(type(i)) # i is a boolean, gives True or False values

j = None
print(j)
print(type(j)) # j is NoneType, represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, collection of ordered items that can be modified, can contain different data types

l = str(14)
print(l)
print(type(l)) # l is a string, sequence of characters (text) that can be changed

m = 1e4
print(m)
print(type(m)) # m is a float, number with decimals (1e4 is scientific notation for 10000.0??)

'''
Questions:
1. 9 different data types
2. int, float, complex, str, list, dictionary, tuple, bool, NoneType
3. b & m (floats), d & l (strings), e & h & k (lists)
4. l was a string, it wasn't an integer because it was in the str() function which converts it to a string data type
5. look below
'''

new_type_range = range(10)
print(new_type_range)
print(type(new_type_range)) # new_type_range is a range object data type, represents an immutable sequence of numbers between 0 and 10 (not including 10)



# --- BOOLEANS
print(10 > 9) # true
print(10 == 9) # false
print(10 <= 9) # false
print(bool("abc")) # true
print(bool(123)) # true
print(bool(["apple", "cherry", "banana"])) # true
print(bool(True)) # true
print(bool(False)) # false
print(bool(0)) # false
print(bool("")) # false
print(bool(" ")) # true
print(bool(())) # false
print(bool([])) # false
print(bool({})) # false
print(bool(True and False)) # false
print(bool(True and True)) # true
print(bool(False and False)) # false
print(bool(True or False)) # true
print(bool(True or True)) # true
print(bool(False or False)) # false
print(bool(not False)) # true
print(bool(not True)) # false

'''
Questions:
1. empty functions return false, non-empty functions return true, t and f returns false, t or f returns true
2. why a nonempty function returns true and why an empty function returns false
3. bool(1) returns true because 1 is a non-zero number, which is considered true in boolean context
4. bool(5 != 5) returns false because it states 5 is not equal to 5, which is false
'''



# --- OPERATORS

# Arithmetic Operators
print(10 + 5) # 15, performs addition
print(10 - 5) # 5, performs subtraction
print(2 * 4) # 8, performs multiplication
print(6 / 3) # 2.0, performs division (returns a float)
print(5 % 2) # 1, performs modulus (returns the remainder)
print(3 ** 2) # 9, performs exponents
print(15 // 2) # 7, performs floor division (returns the quotient without the remainder)


# Comparison Operators
print(5 == 2) # returns false
print(10 != 10) # returns false
print(2 < 5) # returns true
print(12 > 5) # returns true
print(5 <= 6) # returns true
print(1 >= 10) # returns false


# Assignment Operators
x = 5
x += 5
print(x) # assigns x the value of itself plus 5 (x = x + 5) and prints 10
x -= 4
print(x) # assigns x the value of itself (now 10)minus 4 (x = x - 4) and prints 6
x *= 3
print(x) # assigns x the value of itself (now 6) times 3 (x = x * 3) and prints 18


# Logical Operators
# 1. and operator checks both conditions, if they are BOTH true it returns true, else false
y = 10
print(y > 5 and y < 15) # returns true
print(y > 5 and y < 9) # returns false
# 2. or operator checks both conditions, but if only one is true it stops there and returns true
print(y > 5 or y < 9) # returns true
print(y < 5 or y < 9) # returns false
# 3. not operator reverses the bool value
print(not False) # returns true
print(not True) # returns false


'''
Questions:
1. / returns a float, // returns an integer
2. % returns remainder (modulus), // returns quotient without remainder
3. % mod operator: print(5 % 2) returns 1
4. they reassign the variable to a new variable by performing arithmetic; x += 5 gives x = x + 5
'''



#STRINGS
my_string = "hello"
print(my_string) # prints the string "hello"
print(my_string[0]) # prints the first character of the string, which is "h"
print(my_string[1]) # prints the second character of the string, which is "e"
print(my_string[2]) # prints the third character of the string, which is "l"
print(my_string[3]) # prints the fourth character of the string, which is "l"
print(my_string[4]) # prints the fifth character of the string, which is "o"
print(my_string[-1]) # prints the last character of the string, which is "o" -- goes backwards
print(my_string[1:3]) # prints the range of characters from 1 to 3, excluding the last index, which is "el"
#print(my_string[0:5:2]) # prints the range of characters from 0 to 5, stepping by 2, which is "hlo"
print(len(my_string))
print(my_string + "goodbye")
print(my_string * 7)

'''
Questions:
1. Slicing is when you are able to extract particular parts of a string by using the index values, like in #8 and #9
2. see below: result gives "Hello, my name is Oski", it concatinated "Hello, my name is " with the variable name which is "Oski". How did it add a space before Oski though?
3. see below: result also gives "Hello, my name is Oski", How did it add a space before Oski though?
4. There is no difference in the results, but f-strings are meant to be a cleaner and more readable way to format strings, especially when you have multiple variables to include in the string.
'''

name = "Oski"
print("Hello, my name is", name)
print(f"Hello, my name is {name}")



# --- TERMINAL COMMANDS

'''
1. cd
 - changes directory, use it to move between folders
 - example: cd python_decal_f26
2. ls
 - lists files within current directory, use it to see what files/folders are in current directory
 - example: ls (whenever you are already in a directory and want to see what to move into)
3. ls -a
 - 
 - 
4. mkdir
 - makes a new directory, use it to create a new folder
 - example: mkdir new_project
5. cat
 - displays the contents of a FILE, use it to see what you have in the file
 - example: cat homework1.py
6. pwd
 - it prints working directory, meaning it displays the name of the directory you are currently in, use it to see where you are in the file system
 - example: pwd
7. cd ..
 - 
 - 
8. cd .
 - 
 - 
9. cd ∼
 - 
 - 
10. cp
 - 
 - 
11. mv
 - 
 - 
12. rm (be careful with this one)
 - 
 - 
13. clear
 - clears the terminal screen NOT THE CONTENTS, just makes it look clean and gets rid of the words, use it to clear workspace
 - example: clear
14. grep
 - 
 - 
'''