#3.1

food = ["pasta", "avocado", "taco bell"]
print(food[1])
print(food[-1])
food.append("chocolate")
food.insert(0, "apple")
food.remove("avocado") #OR food.pop(2)
print(len(food))
print(food)

for i in range(len(food)):
    food[i] = food[i].upper()
    print(food[i])

new_food = food[0:5:3]
print(new_food)

if "potato" in food:
    print("A potato!")
else:
    print("No potato!")


#3.2

numbers = range(0, 21)
for i in numbers:
    print(i)

def get_first_15(number):
    list_of_numbers = []
    for i in numbers:
        if i < 15:
            list_of_numbers.append(i)
    return list_of_numbers

print(get_first_15(numbers))

def get_every_5th(list_of_numbers):
    every5th = []
    for i in range(4, len(list_of_numbers), 5):
        every5th.append(list_of_numbers[i])
    return every5th

print(get_every_5th(numbers))

def reverse_list(numbers):
    rev = []
    for i in numbers[::-1]:
        rev.append(i)
    return rev[::3]

print(reverse_list(numbers))


#3.3

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
numbers = [list1, list2, list3]
numbers2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(numbers[2])
#print(numbers2[2][1])
numbers2.append([10, 11, 12])

def sum_nested(numbers2):
    total = 0
    for i in numbers2:
        for j in i:
            total += j
    return total
print(sum_nested(numbers2))


#3.4
def create_grid():
    fivebyfive = []
    val = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(val)
            val += 1
        fivebyfive.append(row)
    return fivebyfive

print(create_grid())

def replace_in_grid(fivebyfive):
    grid2 = []
    for i in fivebyfive:
        row = []
        for j in i:
            if j % 3 == 0:
                row.append("?")
            else:
                row.append(j)
        grid2.append(row)
    return grid2

print(replace_in_grid(create_grid()))

def sum_else(grid2):
    total = 0
    for i in grid2:
        for j in i:
            if j != "?":
                total += j
    return total

print(sum_else(replace_in_grid(create_grid())))


#4.1

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for person in ages:
    print(person, ages[person])