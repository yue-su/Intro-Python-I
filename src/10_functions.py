# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def check_even(x):
    if x % 2 == 0:
        return True
    return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
result = check_even(num)
print(result)


# Print out "Even!" if the number is even. Otherwise print "Odd"

def check_even_se(x):
    if x % 2 == 0:
        print("even!")
    else:
        print("Odd!")

num = input("enter another number: ")
num = int(num)
print(check_even_se(num))
# YOUR CODE HERE
