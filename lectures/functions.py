'''
FUNCTIONS

def function_name(input):
# python does stuff
return output
'''

name = "Shreya"
print("Hello,", name)


def say_hello(name):
    print("Hello,", name)
say_hello(name)


def add(a,b):
    return a+b

print(add(7,8))



'''
IF ELIF ELSE CONDITIONALS

if = checks if conditiion is True
elif = checks if first "if" was False (additional condition)
else = catches everything else, very last resort

**program follows what's true

if main condition:
    do something
elif secondary condition:
    do something
else:
    do something

'''

def check_num(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "0"

print(check_num(3))



'''
AND OR CONDITIONALS

and = both conditions must be true
or = only one condition must be True

note: == is equal to, != is not equal to
'''

print(True and True)
print(True or True)
print(False and False)
print(False or False)
print(True and False)
print(True or False)

def can_vote(age, is_citizen):
    if age >= 18 and is_citizen:
        print("You can vote!")
    else:
        print("You cannot vote.")

can_vote(19, True)

def is_weekend(day):
    if day == "Saturday" or day == "Sunday":
        return "It is the weekend!"
    else:
        return "It is not the weekend."

print(is_weekend("Tuesday"))



'''
FOR WHILE LOOPS

for loop: 
while loop: 

'''

for i in range(10):
    print(i)
#first one you want, second one you don't want

fruit_basket = ["lychee", "mango", "nectarines"]

for fruit in fruit_basket:
    print(fruit)

def countdown(start):
    while start >= 0:
        print("T-",start)
        start -= 1
    print("Blast off!")

countdown(5)


def weather_check(temp):
    if temp > 85:
        return "It's hot today"
    elif temp >= 65 and temp <= 85:
        return "It's warm today"
    else:
        return "It's cold today"

print(weather_check(85))