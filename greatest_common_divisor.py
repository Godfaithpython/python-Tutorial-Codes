a = int(input("Enter a positve number: "))
b = int(input("Enter another positive number: "))
x = 1
if x % a == 0:
  if x % b == 0:
    print("The LCM is: ", x)
GCD = (a*b)/x
print("The GCD is: ",GCD)