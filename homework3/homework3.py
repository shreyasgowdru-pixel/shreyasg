def say_goodbye(name):
    print("Goodbye,", name)

say_goodbye("Shreya")


def area_of_circle(radius):
    # A = pi(r)^2
    A = 3.14*radius**2
    print("the area of this circle is", A)

area_of_circle(4)


def subtract(a, b):
    sub = a - b
    return sub

def multiply(a, b):
    mult = a*b
    return mult

def divide(a, b):
    div = a/b
    return div


def min_max(list, min, max):
    return min(list)
    return max(list)

list = [15, 14, 17, 20, 23, 28, 20]
print ("(", min(list), ", ", max(list), ")")


def day_of_week(day_num):
    if day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    elif day_num == 4:
        return "Thursday"
    elif day_num == 5:
        return "Friday"
    elif day_num == 6:
        return "Saturday"
    elif day_num == 7:
        return "Sunday"
    else:
          return "not a day silly"

print(day_of_week(4))


def fuel_efficiency(dist, fuel_used):
    efficiency = dist/fuel_used
    return efficiency

print(fuel_efficiency(21, 50))


def secret(integer):
    x = integer // 10
    y = integer % x
    integer -= y
    integer //= 10
    integer = str(y) + str(integer)
    return integer

print(secret(3456))


def exp(x, y):
    z = x
    for i in range(y-1):
        z *= x 
    return z

print(exp(2, 5))


def min_for(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

list = [1, 2, 0, 2, 5, 6, 7]
print(min_for(list))

def max_for(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

list = [1, 2, 0, 2, 5, 6, 7]
print(max_for(list))


def min_while(list):
    min = list[0]
    i = 0
    while i < len(list):
        if list[i] < min:
            min = list[i]
        i+=1
    return min

list = [1, 2, 0, 2, 5, 6, 7]
print(min_while(list))


def max_while(list):
    max = list[0]
    i = 0
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i+=1
    return max

list = [1, 2, 0, 2, 5, 6, 7]
print(max_while(list))


def sum(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        a = num[i]
        sum += int(a)
    return sum

print(sum(1021))
