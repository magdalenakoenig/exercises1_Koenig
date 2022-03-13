## beispiel 1
age = input("Enter you age here: ")
name = input("Enter your name here: ")

def name_age(name, age):
    return(name+age)

print("Hello " + name + ". Your age is " + age + ".")
print("\n")



## beispiel 2
num1 = 4
num2 = 10

print("x = ", num1)
print("y = ", num2)

def swap_integers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    print("After swap: ")
    print("x = ", num1)
    print("y = ", num2)
    return(str(num1) + str(num2))

c = swap_integers(num1, num2)
print("Return value: " + c)
print("\n")


## beispiel 3
def check_numbers(num1,num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
                return True
    else:
        return False

print(check_numbers(60,50))
print("\n")


## beispiel 4
def sum_up(num1, num2):
    if (num2 >> num1 and num1 >> 0 and num2 >> 0):
        return(sum(range(num1, num2+1)))
    else:
        return False


print(sum_up(1,6))
print("\n")


## beispiel 5
pi = 3.141

def circle_area(r1, r2, r3):
    x = pi * r1**2
    y = pi * r2**2
    z = pi * r3**2
    sum = x + y + z
    return sum

print(circle_area(1,2,3))
print("\n")



## beispiel 6
def check_string(text):
    x = ("a", "A")
    if(text.endswith(x)) or (text.startswith(x)):
        return True
    else:
        return False


print(check_string("magda"))
print("\n")



## beispiel 7
def triangle(rows):
    for x in range(rows):
        for y in range(x + 1):
            print("* ", end="")
        print("\n")


print(triangle(5))