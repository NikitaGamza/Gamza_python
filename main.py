# TASK 1
try:
    # 1.1 Enter a number
    num = int(input("Enter a number: "))

    # 1.2 Check entered number
    if num > 7:
        print("Hello")
except ValueError:
    pass


# 1.3 Enter name
name = input("Enter a name: ")

# 1.4 Check entered name
if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

try:
    # 1.5 Enter items for array
    numbs = list(map(int, input("Enter items for array (space is a separator): ").split()))
    new_numbs = []

    # 1.6 Check items
    for numb in numbs:
        if numb % 3 == 0:
            new_numbs.append(numb)
    print(f"array elements that are multiples of 3: {new_numbs}")
except ValueError:
    print("Invalid input")


# TASK 2
sequence = input("Enter a sequence: ")
buff = []
brackets = {')': '(', ']': '[', '}': '{'}
err = False

for sign in sequence:
    if sign in "([{":
        buff.append(sign)

    elif sign in "}])":
        if not buff or buff[-1] != brackets[sign]:
            err = True
        buff.pop()

if err:
    print("The sequence is invalid")
else:
    print("The sequence is valid")

print("In task example [((())()(())]] item at 1st index should be [, not (")