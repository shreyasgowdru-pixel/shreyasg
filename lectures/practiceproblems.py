#PRACTICE PROBLEMS


# 1. print the minimum and maximum value in the given list

list = [40, 80, 10, 30, 50, 20]

def minimum(list, min):
    return min(list)

def maximum(list, max):
    return max(list)

print (min(list))
print (max(list))


# 2. create a function to determine if a positive integer is a prime number

def isprime(num):
    if num<=0 and type(num) != int:
        return "try again"
    else:
        if num == 1:
            return "neither"
        elif num == 2:
            return "prime number"
        else:
            if num % 2 == 0:
                return "composite number"
            else:
                for i in range(1,num):
                    if num % i == 0:
                        return "not prime"
                    else:
                        return "prime"
print(isprime(21))