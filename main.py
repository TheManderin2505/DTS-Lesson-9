stack = []


def pop(): 
    stack.pop(-1)

stack.append("Hello")
print(stack)

u1 = str(input("Please enter a word : "))

stack.append(u1)
print(stack)

u2 = input("Would you like to undo this? ")
if u2 == "yes" or u2 == "Yes" or u2 == "y" or u2 == "Y":
    pop()
    print(stack)
else:
    print("")