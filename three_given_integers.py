x = int(input("Enter a number X: "))
y = int(input("Enter a number Y: "))
z = int(input("Enter a number Z: "))
if x != y and y != z and x != z:
    sum = x + y + z
    print(sum)
elif x == y or y == z or x == z:
    sum = 0
    print(sum)